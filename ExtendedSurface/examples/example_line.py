#!/usr/bin/env python3
"""Examples of various ways to draw a line."""
import cairo

from src.ExtendedSurface import ExtendedSurface

# Create the ExtendedSurface object and set the background to white
es = ExtendedSurface(600, 800)
es.set_background()

# Draw a black line from (50, 250) to (200, 50)
es.draw.line(50, 250, 200, 50)

# Draw a blue line 10 pixels thick from (350, 350) to (500, 100)
es.draw.line(350, 350, 500, 100,  color=(0, 0, 255), line_width=10)
	
# Draw a red line 20 pixels thick from (50, 500) to (250, 700) with a rounded 
# line cap.
es.draw.line(50, 500, 250, 700, 
	line_cap=cairo.LINE_CAP_ROUND, color=(255, 0, 0), line_width=20)
	
# Draw an X in the bottom-right quadrant
es.draw.line("center", "center", "right", "bottom")
es.draw.line("center", "bottom", "right", "center")
	
# Draw gridlines for reference (outline + vertical/horizontal center lines)
es.gridlines()

# Write our drawing to a PNG file
es.write_to_png("example_line.png")

