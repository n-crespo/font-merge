This repo contains a python script used to generate versions of the
JetBrainsMono Nerd font with support for legacy symbols.

Created so that my font would play nicely with smear-cursor.nvim.

Credit to [this utility I used](https://github.com/RebeccaRGB/slcgen) and the
original (and patched) JetBrainsMono font.

```bash
# this is from slcgen, no need to re generate (i think)
fontforge -script slcgen.py -o legacy_symbols.sfd
# now we actually merge the fonts
fontforge -script merge.py # change specified *.ttf files as needed
```
