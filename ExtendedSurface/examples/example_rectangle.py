#!/usr/bin/env python3
"""Examples of various ways to draw a rectangle."""

from src.ExtendedSurface import ExtendedSurface

# Create the ExtendedSurface object and set the background to yellow
es = ExtendedSurface(600, 800)
es.set_background((255, 255, 0))

# Draw a black rectangle at (50, 50) and measuring 100x200 pixels
es.draw.rectangle(50, 50, 100, 200)

# Draw a blue rectangle at ("left", 650) and measuring 200x100 pixels
es.draw.rectangle("left", 650, width=200, height=100, color=(0, 0, 255))

# Draw an empty rectangle at (200, "top") measuring 200x250 pixels
es.draw.rectangle(200, "top", 200, 250, fill=False)

# Draw a pink rectangle at ("right", "bottom") that fills in the entire
# bottom-right quadrant with a purple outline that is 20 pixels thick
es.draw.rectangle(
	x="right", y="bottom",
	width=es.get_width()/2, height=es.get_height()/2,
	color=(255, 192, 203), outline=20, outline_color=(128, 0, 128)
	)

# Draw a transparent lime-green rectangle at ("center", "center") measuring
# 250x250 pixels and with a red outline
es.draw.rectangle("center", "center", 250, 250,
	color=(50, 205, 50, 128), outline_color=(255, 0, 0))

# Draw gridlines for reference (outline + vertical/horizontal center lines)
es.gridlines()

# Write our drawing to a PNG file
es.write_to_png("example_rectangle.png")
