#!/usr/bin/env python3
"""Example of text written with the default parameters."""

from src.ExtendedSurface import ExtendedSurface

# Create the ExtendedSurface object and set the background to white
es = ExtendedSurface(600, 800)
es.set_background()

# Write text with default parameters
es.text.write(
	("This is one text block written with the default parameters.\n\n"
	 "Line breaks are supported and\n"
	 "give\n"
	 "more\n"
	 "control\n"
	 "over how the text looks.\n\n"
	 "With the font size not specified, the text will fill as much of "
	 "the area as it's allowed to (in this case, the entire page)."),
	0, 0,
	"arial.ttf"
	)

# Write our drawing to a PNG file
es.write_to_png("example_write_1.png")
