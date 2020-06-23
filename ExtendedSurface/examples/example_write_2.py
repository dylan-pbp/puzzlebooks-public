#!/usr/bin/env python3
"""Examples of text written with typical parameters sent in."""

from src.ExtendedSurface import ExtendedSurface

# Create the ExtendedSurface object and set the background to white
es = ExtendedSurface(600, 800)
es.set_background()

# Write left-aligned text in the top-left quadrant
x, y = "left", "top"
bb_width, bb_height = es.text.write(
	("This text has the default alignment (left) and is bound by the "
	 "parameters max_width and max_height to be contained to this quadrant of "
	 "the page. It has the line spacing set to 2.0, but the font size isn't "
	 "specified so this text will fill up as much space as it's allowed."),
	x, y,
	font="arial.ttf",
	line_spacing=2.0,
	max_width=es.get_width()/2,
	max_height=es.get_height()/2
	)
es.draw.rectangle(x, y, bb_width, bb_height, fill=False)

# Write right-aligned text in the top-right quadrant with a font size of 25 pts
x, y = "right", "top"
bb_width, bb_height = es.text.write(
	("This text is right-aligned. Its font size is set to 25 pts so it will "
	 "not automatically adjust, even if the text goes off the page."),
	x, y,
	font="arial.ttf",
	font_size=25,
	max_width=es.get_width()/2,
	max_height=es.get_height()/2,
	alignment="right"
	)
es.draw.rectangle(x, y, bb_width, bb_height, fill=False)

# Write center-aligned blue text in the bottom-left quadrant with a different
# font and padding on all sides
text_buffer = 15
x, y = text_buffer, es.get_height()/2 + text_buffer
bb_width, bb_height = es.text.write(
	("Here is some center-aligned text. This text is blue, in a different "
	 "font, and has padding on all sides\n"
	 "(top:10, right:20, bottom:30, left:40).\n\n"
	 "The boxes drawn around all the examples represent the bounding boxes "
	 "containing the text and padding. The width and height of a bounding "
	 "box are returned and can be used to draw bounding boxes or dynamically "
	 "stack text blocks, like in the example to the right."),
	x, y,
	font="Boogaloo-Regular.otf",
	max_width=es.get_width()/2 - 2*text_buffer,
	max_height=es.get_height()/2 - 2*text_buffer,
	color=(0, 0, 255),
	padding={"top":10, "right":20, "bottom":30, "left":40},
	alignment="center"
	)
es.draw.rectangle(x, y, bb_width, bb_height, fill=False)

# Write two justified blocks of text: one to show the last line being
# justified, and one to show it not being justified
x, y = es.get_width()/2, es.get_height()/2
bb_width, bb_height = es.text.write(
	("This text is justified. Notice how it stretches to each side of its "
	 "container within the padding. For this example, the last line will be "
	 "left to not be justified:\nhere is the last line."),
	x, y,
	"arial.ttf",
	max_width=es.get_width()/2,
	alignment="justified",
	justify_last_line=False,
	padding={"top":5, "right":5, "bottom":5, "left":5},
	font_size=20
	)
es.draw.rectangle(x, y, bb_width, bb_height, fill=False)

x = es.get_width()/2
y += bb_height + 10
bb_width, bb_height = es.text.write(
	("This text is justified. Notice how it stretches to each side of its "
	 "container within the padding. For this example, the last line will be "
	 "left to be justified:\nhere is the last line."),
	x, y,
	"arial.ttf",
	max_width=es.get_width()/2,
	alignment="justified",
	justify_last_line=True,
	padding={"top":5, "right":5, "bottom":5, "left":5},
	font_size=20
	)
es.draw.rectangle(x, y, bb_width, bb_height, fill=False)

# Write our drawing to a PNG file
es.write_to_png("example_write_2.png")
