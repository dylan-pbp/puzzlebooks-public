#!/usr/bin/env python3
"""Examples of text written with more specialized parameters sent in."""
from src.ExtendedSurface import ExtendedSurface

# Create the ExtendedSurface object and set the background to white
es = ExtendedSurface(600, 800)
es.set_background()

# Write text to demonstrate automatic line breaks
text_buffer = 30
x = "center"
y = 10
text = ("This is an example of text that has line breaks automatically put "
		"into it in order to best fit its constraints.\n\n"
		"This is useful if you know the area that you want the text to stay "
		"within, but you don't know what size to make the font. This default "
		"makes the text look as nice as possible.")
bb_width, bb_height = es.text.write(
	text,
	x, y,
	font="arial.ttf",
	max_height=es.get_height()/6,
	padding={"top":5, "right":5, "bottom":5, "left":5}
	)
es.draw.rectangle(x, y, bb_width, bb_height, fill=False)

# Write text to demonstrate what happens without automatic line breaks
y += bb_height + text_buffer
text = ("This is an example of text that does not have line breaks "
		"automatically put into it.\n\n"
		"The font size is not specified, which means it will be adjusted for "
		"the longest line of text.\n\n"
		"This is good for things like titles or headlines that you want as "
		"big as possible while still remaining on one line.")
bb_width, bb_height = es.text.write(
	text,
	x, y,
	font="arial.ttf",
	max_height=es.get_height()/6,
	break_up_lines=False,
	padding={"top":5, "right":5, "bottom":5, "left":5}
	)
es.draw.rectangle(x, y, bb_width, bb_height, fill=False)

# Write text to show what happens with a specified font size and no automatic
# line breaks
y += bb_height + text_buffer
text = ("In this example, a font size is specified but line breaks are not "
		"automatically put in.\n\nThe result is that a line of text goes off "
		"the page if we keep typing more and more and more and more.")
bb_width, bb_height = es.text.write(
	text,
	"center", y,
	font="arial.ttf",
	max_height=es.get_height()/6,
	break_up_lines=False,
	font_size=15,
	alignment="center",
	padding={"top":5, "right":5, "bottom":5, "left":5}
	)
es.draw.rectangle("center", y, bb_width, bb_height, fill=False)

# Draw a line to separate the two example sections
y_line = y + bb_height + text_buffer/2
es.draw.line("left", y_line, "right", y_line)

# Write white text with a black outline
y += bb_height + text_buffer
bb_width, bb_height = es.text.write(
	"This is an example of white text with a black outline.",
	"center", y,
	"arial.ttf",
	max_height=es.get_height()/4,
	color=(255, 255, 255),
	outline=2,
	outline_color=(0, 0, 0),
	alignment="center",
	padding={"top":5, "right":5, "bottom":5, "left":5}
	)

# Write green text with a red outline
y += bb_height + text_buffer
es.text.write(
	"And this is an example of green text with a thick red outline.",
	"center", y,
	"arial.ttf",
	max_height=es.get_height()/4,
	color=(0, 255, 0),
	outline=5,
	outline_color=(255, 0, 0),
	alignment="center",
	padding={"top":5, "right":5, "bottom":5, "left":5}
	)

# Write our drawing to a PNG file
es.write_to_png("example_write_3.png")
