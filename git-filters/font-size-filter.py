#!/usr/bin/env python3
"""stdin/stdout filter for platform-local font sizes in settings.json.

Registered via .gitattributes (filter=font-size-local) plus local git
config (see git-filters/install.sh, run once per machine). "smudge"
rewrites the committed (canonical) values to this platform's values on
checkout; "clean" rewrites them back to canonical before staging/diffing,
so the working tree never shows a font-size diff against what's committed
and pulls never conflict on these lines.
"""
import platform
import re
import sys

CANONICAL = {
    "ui_font_size": "18.0",
    "buffer_font_size": "18.0",
    "font_size": "17.0",  # terminal.font_size
    "agent_ui_font_size": "17.0",
    "agent_buffer_font_size": "16.0",
    "markdown_preview_font_size": "16.0",
}

PLATFORM_OVERRIDES = {
    "Darwin": {
        "ui_font_size": "16.0",
        "buffer_font_size": "16.0",
        "font_size": "15.0",
        "agent_ui_font_size": "18.0",
        "agent_buffer_font_size": "15.0",
        "markdown_preview_font_size": "15.0",
    },
    # Linux (and anything else) uses the canonical values as-is.
}


def apply(values, content):
    for key, value in values.items():
        content = re.sub(
            r'("%s":\s*)[0-9.]+' % re.escape(key),
            r'\g<1>%s' % value,
            content,
            count=1,
        )
    return content


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("clean", "smudge"):
        sys.exit("usage: font-size-filter.py [clean|smudge]")

    content = sys.stdin.read()

    if sys.argv[1] == "clean":
        content = apply(CANONICAL, content)
    else:
        values = PLATFORM_OVERRIDES.get(platform.system(), CANONICAL)
        content = apply(values, content)

    sys.stdout.write(content)


if __name__ == "__main__":
    main()
