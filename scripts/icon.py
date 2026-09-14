#!/usr/bin/env python3
"""Iconify icons for generate-presentation decks.

Decks stay self-contained: icons are fetched from the Iconify API while authoring and
inlined as SVG, so a presentation never needs the network.

  icon.py search <query> [--prefix lucide] [--limit 20]   list matching icon ids
  icon.py svg <prefix:name>                                print one inline <svg>
  icon.py inline <deck.html>                               replace every <i data-icon="prefix:name"></i>
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

API = "https://api.iconify.design"
ICON_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*:[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDER = re.compile(r'<i\s+data-icon="([^"]+)"(?:\s+class="([^"]*)")?\s*>\s*</i>')


def fetch_json(url, attempts=4):
    request = urllib.request.Request(url, headers={"User-Agent": "generate-presentation/icon.py"})
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            # The public API rate-limits bursts; back off instead of failing the whole deck.
            if error.code != 429 or attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt * 2)


def load_icons(icon_ids):
    """Fetch every icon in one request per prefix. Returns ({id: svg_parts}, [missing ids])."""
    by_prefix = defaultdict(set)
    for icon_id in icon_ids:
        prefix, name = icon_id.split(":")
        by_prefix[prefix].add(name)

    found, missing = {}, []
    for prefix, names in by_prefix.items():
        query = urllib.parse.urlencode({"icons": ",".join(sorted(names))})
        try:
            data = fetch_json(f"{API}/{prefix}.json?{query}")
        except urllib.error.HTTPError as error:
            missing += [f"{prefix}:{name} ({error.code})" for name in names]
            continue
        if not isinstance(data, dict):
            missing += [f"{prefix}:{name} (unknown set)" for name in names]
            continue
        icons, aliases = data.get("icons", {}), data.get("aliases", {})
        for name in names:
            source = name if name in icons else aliases.get(name, {}).get("parent")
            if source not in icons:
                missing.append(f"{prefix}:{name}")
                continue
            icon = icons[source]
            found[f"{prefix}:{name}"] = {
                "body": icon["body"],
                "left": icon.get("left", data.get("left", 0)),
                "top": icon.get("top", data.get("top", 0)),
                "width": icon.get("width", data.get("width", 16)),
                "height": icon.get("height", data.get("height", 16)),
            }
    return found, missing


def render(icon_id, parts, extra_class=""):
    classes = " ".join(filter(None, ["icon", extra_class]))
    view_box = f'{parts["left"]} {parts["top"]} {parts["width"]} {parts["height"]}'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="{classes}" data-icon="{icon_id}" aria-hidden="true" '
            f'width="1em" height="1em" viewBox="{view_box}">{parts["body"]}</svg>')


def validate(icon_ids):
    bad = [icon_id for icon_id in icon_ids if not ICON_ID.match(icon_id)]
    if bad:
        raise ValueError("invalid icon ids, expected prefix:name (e.g. lucide:database): " + ", ".join(bad))


def cmd_search(args):
    query = urllib.parse.urlencode({"query": args.query, "prefix": args.prefix, "limit": max(args.limit, 32)})
    icons = fetch_json(f"{API}/search?{query}").get("icons", [])[: args.limit]
    if not icons:
        print(f"no icons for {args.query!r} in {args.prefix}", file=sys.stderr)
        return 1
    print("\n".join(icons))
    return 0


def cmd_svg(args):
    validate([args.icon])
    found, missing = load_icons([args.icon])
    if missing:
        print(f"not found: {missing[0]}", file=sys.stderr)
        return 1
    print(render(args.icon, found[args.icon]))
    return 0


def cmd_inline(args):
    deck = Path(args.deck)
    html = deck.read_text(encoding="utf-8")
    matches = list(PLACEHOLDER.finditer(html))
    if not matches:
        print(f"{deck}: no placeholders")
        return 0

    icon_ids = sorted({match.group(1) for match in matches})
    validate(icon_ids)
    found, missing = load_icons(icon_ids)
    if missing:
        print("unresolved icons, file left untouched:\n  " + "\n  ".join(sorted(missing)), file=sys.stderr)
        return 1

    result = PLACEHOLDER.sub(lambda m: render(m.group(1), found[m.group(1)], m.group(2) or ""), html)
    deck.write_text(result, encoding="utf-8")
    print(f"{deck}: {len(matches)} placeholders inlined ({len(icon_ids)} distinct icons)")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="list icon ids matching a query")
    search.add_argument("query")
    search.add_argument("--prefix", default="lucide")
    search.add_argument("--limit", type=int, default=20)
    search.set_defaults(run=cmd_search)

    svg = sub.add_parser("svg", help="print one icon as inline SVG")
    svg.add_argument("icon")
    svg.set_defaults(run=cmd_svg)

    inline = sub.add_parser("inline", help="replace <i data-icon> placeholders in a deck")
    inline.add_argument("deck")
    inline.set_defaults(run=cmd_inline)

    args = parser.parse_args()
    try:
        return args.run(args)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    except urllib.error.URLError as error:
        print(f"cannot reach {API}: {getattr(error, 'reason', error)}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
