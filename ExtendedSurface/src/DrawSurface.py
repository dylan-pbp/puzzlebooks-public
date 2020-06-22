"""
Draw on an ExtendedSurface object.

This class extends existing pycairo drawing functionality and introduces
some new functionality. The code is intended to be clean and accessible,
producing vector drawings that are both predictable and complex.
"""
import functools
import math

import cairo

def polygon_wrapper(func):
	"""
	Wrapper function to perform the setup and teardown of polygon
	attributes before and after creating the polygon.

	Keyword arguments:
		func (function) -- the function to draw the polygon.
	"""
	@functools.wraps(func)
	def draw_polygon(self, *args, **kwargs):
		"""
		Setup the Context, draw the polygon with attributes applied, and
		teardown the environment.
		"""
		# Save the Context so we can restore it when this is done
		self.context.save()

		# Initialize the polygon's attributes
		self.init_attributes(**kwargs)

		# Call the function
		result = func(self, *args, **kwargs)

		# Fill the polygon, if it's being filled
		if self.fill:
			self.context.fill_preserve()

		# Set the outline color and outline the polygon
		self.calling_surface.set_color(self.outline_color)
		self.context.stroke()

		# Restre the Context now that the polygon is drawn
		self.context.restore()

		return result

	return draw_polygon

class DrawSurface():
	"""Draw a polygon on an ExtendedSurface object."""
	def __init__(self, calling_surface):
		"""
		Initialize the DrawSurface object.

		Keyword arguments:
			calling_surface (ExtendedSurface) -- the surface to be drawn onto.

		Class attributes:
			x (int) -- the x-coordinate of the polygon.
			y (int) -- the y-coordinate of the polygon.
			width (int) -- the width of the polygon.
			height (int) -- the height of the polygon.
			color (4-tuple) -- the RGBA color of the polygon.
			fill (bool) -- whether or not the polygon is filled with color.
			line_cap (str) -- the pycairo rendering of the endpoint of a line.
			line_join (str) -- the pycairo rendering for the vertex
				connecting two joined lines.
			outline (int) -- the thickness of the polygon's outline, in pixels.
			outline_color (4-tuple) -- the RGBA color of the polygon's outline.
		"""
		self.calling_surface = calling_surface
		self.context = self.calling_surface.context

		self.x = None
		self.y = None
		self.width = None
		self.height = None

		self.color = None
		self.fill = None
		self.line_cap = None
		self.line_join = None
		self.outline = None
		self.outline_color = None

	@polygon_wrapper
	def dot(self, x, y, radius=1, **kwargs):
		"""
		Draw a dot of a given radius, centered at (x, y).

		Keyword arguments:
			x (int) -- the x-coordinate.
			y (int) -- the y-coordinate.
			radius (int) -- the radius of the dot (default 1).
			color (3- or 4-tuple) -- the RGB(A) color of the dot
				(default (0, 0, 0) (black)).
			fill (bool) -- whether or not to fill the dot with color
				(default True).
			outline (int) -- the thickness of the dot's outline,
				in pixels (default 1).
			outline_color (3- or 4-tuple) -- the RGB(A) color of the
				dot's outline (default 'color').
		"""
		# Draw an ellipse using the dot parameters given
		#self.ellipse(x-radius, y-radius, radius*2, radius*2, **kwargs)

		# Grab the essential attributes
		self.x = x
		self.y = y
		self.width = radius * 2
		self.height = radius * 2

		# Determine the x and y coordinates based on other attributes.
		# NOTE: This sets the attributes based on the top-left corner of a
		# bounding box containing the dot.
		self._determine_xy()

		# Draw the dot by moving to the center and drawing a circle with the
		# given radius, accounting for the width of the outline.
		self.context.arc(
			self.x + self.width/2, self.y + self.height/2,
			radius - self.outline/2,
			0, 2 * math.pi
			)

	@polygon_wrapper
	def ellipse(self, x, y, width, height, **kwargs):
		"""
		Draw an ellipse of a given width and height. The (x, y)-coordinates
		correspond to the top-left corner of the bounding box that would
		contain the ellipse.

		Keyword arguments:
			x (int/str) -- the x-coordinate of the ellipse.
			y (int/str) -- the y-coordinate of the ellipse.
			width (int) -- the width of the ellipse.
			height (int) -- the height of the ellipse.
			color (3- or 4-tuple) -- the RGB(A) color of the ellipse
				(default (0, 0, 0) (black)).
			fill (bool) -- whether or not to fill the ellipse with color
				(default True).
			outline (int) -- the thickness of the ellipse's outline,
				in pixels (default 1).
			outline_color (3- or 4-tuple) -- the RGB(A) color of the
				ellipse's outline (default 'color').
		"""
		# Grab the essential attributes
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		# Determine the x and y coordinates based on other attributes
		self._determine_xy()

		# Draw an ellipse by scaling the Context by the width and height,
		# and drawing a unit circle
		self.context.save()
		self.context.translate(
			self.x + self.width / 2, self.y + self.height / 2)
		self.context.scale(self.width / 2, self.height / 2)
		self.context.arc(0, 0, 1, 0, 2 * math.pi)
		self.context.restore()

	def line(self, x1, y1, x2, y2, **kwargs):
		"""
		Draw a line connecting two points at given sets of coordinates.

		Keyword arguments:
			x1 (int) -- the x-coordinate of the first point.
			y1 (int) -- the y-coordinate of the first point.
			x2 (int) -- the x-coordinate of the second point.
			y2 (int) -- the y-coordinate of the second point.
			color (3- or 4-tuple) -- the RGB(A) color of the polygon
				(default (0, 0, 0) (black)).
			line_cap (cairo.LINE_CAP) -- the cap at the end of the line
				(default cairo.LINE_CAP_SQUARE).
		"""
		# Save the Context so we can restore it after the line is drawn
		self.context.save()

		# Initialize the shape's attributes
		self.init_attributes(**kwargs)

		# Draw a line
		self.context.move_to(x1, y1)
		self.context.line_to(x2, y2)
		self.context.stroke()

		# Restore the Context
		self.context.restore()

	@polygon_wrapper
	def polygon(self, points, **kwargs):
		"""
		Draw a polygon that connects a series of (x, y)-coordinates.

		Keyword arguments:
			points (list) -- a list of xy-coordinates as tuples,
				indicating the vertices of the polygon.
			color (3- or 4-tuple) -- the RGB(A) color of the polygon
				(default (0, 0, 0) (black)).
			fill (bool) -- whether or not to fill the polygon with color
				(default True).
			line_join(cairo.LINE_JOIN) -- the rendering between two
				joining lines (default cairo.LINE_JOIN_MITER).
			outline (int) -- the thickness of the polygon's outline,
				in pixels (default 1).
			outline_color (3- or 4-tuple) -- the RGB(A) color of the
				polygon's outline (default 'color').
		"""
		# Trace a line for each edge of the shape.
		self.context.move_to(points[0][0], points[0][1])
		for x, y in points[1:]:
			self.context.line_to(x, y)
		self.context.close_path()

	@polygon_wrapper
	def rectangle(self, x, y, width, height, **kwargs):
		"""
		Draw a rectangle. The (x, y)-coordinates correspond to the
		top-left corner of the rectangle.

		Keyword arguments:
			x (int) -- the x-coordinate.
			y (int) -- the y-coordinate.
			width (int) -- the width of the rectangle.
			height (int) -- the height of the rectangle.
			color (3- or 4-tuple) -- the RGB(A) color of the rectangle
				(default (0, 0, 0) (black)).
			fill (bool) -- whether or not to fill the rectangle with color
				(default True).
			outline (int) -- the thickness of the rectangle's outline,
				in pixels (default 1).
			outline_color (3- or 4-tuple) -- the RGB(A) color of the
				rectangle's outline (default 'color').
		"""
		# Grab the essential attributes
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		# Determine the x and y coordinates based on other attributes
		self._determine_xy()

		# Draw the rectangle
		self.context.rectangle(self.x, self.y, self.width, self.height)

	@polygon_wrapper
	def rounded_rectangle(self, x, y, width, height, radius, **kwargs):
		"""
		Draw a rectangle with rounded corners. The (x, y)-coordinates
		correspond to the top-left corner of the bounding box that would
		contain the rounded rectangle.

		Keyword arguments:
			x (int) -- the x-coordinate.
			y (int) -- the y-coordinate.
			width (int) -- the width of the rounded rectangle.
			height (int) -- the height of the rounded rectangle.
			radius (int) -- the radius of the rectangle's corners.
			color (3- or 4-tuple) -- the RGB(A) color of the rounded rectangle
				(default (0, 0, 0) (black)).
			fill (bool) -- whether or not to fill the rounded rectangle with
				color (default True).
			outline (int) -- the thickness of the rounded rectangle's outline,
				in pixels (default 1).
			outline_color (3- or 4-tuple) -- the RGB(A) color of the
				rounded rectangle's outline (default 'color').
		"""
		# Grab the essential attributes
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		# Convert the x and y coordinates, if need be
		self._determine_xy()

		# (x, y)-coordinates of the four corners.
		# The four corners are: bottom-right, bottom-left, top-left, top-right.
		# This order is due to the origin and direction that pycairo goes in
		# when it draws an arc (starts at the rightmost point of the circle and
		# moves clockwise).
		corners = [
			[self.x + self.width - radius, self.y + self.height - radius],
			[self.x + radius, self.y + self.height - radius],
			[self.x + radius, self.y + radius],
			[self.x + self.width - radius, self.y + radius]
			]

		# Draw the four corners
		for i, (corner_x, corner_y) in enumerate(corners):
			self.context.arc(
				corner_x, corner_y,
				radius,
				(i%4)*(math.pi/2),
				((i+1)%4)*(math.pi/2)
				)

		# Draw the path connecting them together
		self.context.close_path()

	def _determine_xy(self):
		"""
		Calculate the x, y, width, and height of the object being drawn,
		based on what's sent in and the size of the outline.
		"""
		# Make sure the coordinates are in the correct format
		if isinstance(self.x, str):
			assert self.x in ["left", "center", "right"], \
				(f"parameter 'x' cannot be '{self.x}', must be either a number "
				 "or one of 'left', 'center', or 'right'")
		if isinstance(self.y, str):
			assert self.y in ["top", "center", "bottom"], \
				(f"parameter 'y' cannot be '{self.y}', must be either a number "
				 "or one of 'top', 'center', or 'bottom'")

		# Adjust the width and height to account for half the outline
		# on both sides (so a full outline in total)
		self.width -= self.outline
		self.height -= self.outline

		# Set the x-coordinate
		if self.x == "left":
			self.x = self.outline/2
		elif self.x == "center":
			self.x = (self.calling_surface.get_width() - self.width) / 2
		elif self.x == "right":
			self.x = (self.calling_surface.get_width()
				- (self.width + self.outline/2))
		else:
			self.x += self.outline/2

		# Set the y-coordinate
		if self.y == "top":
			self.y = self.outline/2
		elif self.y == "center":
			self.y = (self.calling_surface.get_height() - self.height) / 2
		elif self.y == "bottom":
			self.y = (self.calling_surface.get_height()
				- (self.height + self.outline/2))
		else:
			self.y += self.outline/2

	def init_attributes(self, **kwargs):
		"""
		Initialize the attributes for the polygon being drawn,
		and set some of those attributes.

		Keyword arguments:
			color (3- or 4-tuple) -- the RGB(A) color of the polygon
				(default (0, 0, 0) (black)).
			fill (bool) -- whether or not to fill the polygon with color
				(default True).
			line_cap (cairo.LINE_CAP) -- the cap at the end of the line
				(default cairo.LINE_CAP_SQUARE).
			line_join(cairo.LINE_JOIN) -- the rendering between two
				joining lines (default cairo.LINE_JOIN_MITER).
			outline (int) -- the thickness of the polygon's outline,
				in pixels (default 1).
			outline_color (3- or 4-tuple) -- the RGB(A) color of the
				polygon's outline (default 'color').
		"""
		# Initialize attributes based on keyword parameters
		self.color = kwargs.get("color", (0, 0, 0))
		self.fill = kwargs.get("fill", True)
		self.line_cap = kwargs.get("line_cap", cairo.LINE_CAP_SQUARE)
		self.line_join = kwargs.get("line_join", cairo.LINE_JOIN_MITER)
		self.outline = kwargs.get("outline", 1)
		self.outline_color = kwargs.get("outline_color", self.color)

		# Update the Context based on the attributes sent in
		self.calling_surface.set_color(self.color)
		self.context.set_line_cap(self.line_cap)
		self.context.set_line_join(self.line_join)
		self.context.set_line_width(self.outline)
