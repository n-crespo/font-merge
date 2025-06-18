import fontforge
import os

font_files = [
    "JetBrainsMonoNerdFont-Bold.ttf",
    "JetBrainsMonoNerdFont-BoldItalic.ttf",
    "JetBrainsMonoNerdFont-Italic.ttf",
    "JetBrainsMonoNerdFont-Light.ttf",
    "JetBrainsMonoNerdFont-LightItalic.ttf",
    "JetBrainsMonoNerdFont-Regular.ttf",
    "JetBrainsMonoNerdFont-Thin.ttf",
    "JetBrainsMonoNerdFont-ThinItalic.ttf",
]

legacy_font_path = "legacy_symbols.sfd"  # Output from slcgen.py

for font_path in font_files:
    if not os.path.isfile(font_path):
        print(f"Base font not found: {font_path}")
        continue
    print(f"Merging legacy symbols into: {font_path}")
    base = fontforge.open(font_path)
    legacy = fontforge.open(legacy_font_path)

    # Get all codepoints in legacy font except .notdef
    legacy_glyphs = [
        g.encoding
        for g in legacy.glyphs()
        if g.isWorthOutputting() and g.glyphname != ".notdef"
    ]

    for codepoint in legacy_glyphs:
        if codepoint not in base:
            base.createChar(codepoint)
        base.selection.select(codepoint)
        legacy.selection.select(codepoint)
        legacy.copy()
        base.paste()

    # Save merged font with -Legacy before extension
    base_name, ext = os.path.splitext(font_path)
    output_font_path = f"{base_name}-Legacy{ext}"
    base.generate(output_font_path)
    print(f"Saved: {output_font_path}")

print("Done.")
