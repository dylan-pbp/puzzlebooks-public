# ExtendedSurface

The ExtendedSurface class is intended to replace the need for a pycairo.ImageSurface object, extending its functionality by providing methods that can do in one line what might take several lines to do.

## Basic Functionality
ExtendedSurface depends on pycairo and Pillow:
```
python3 -m pip install --user pycairo Pillow
```
You can read more detailed installation instructions [here](https://pycairo.readthedocs.io/en/latest/getting_started.html) and [here](https://pillow.readthedocs.io/en/stable/installation.html).

From the ExtendedSurface root folder, open a terminal and start up the Python Interpreter:
```
python3
```
Import the ExtendedSurface module:
```
from src.ExtendedSurface import ExtendedSurface
```
Initialize an ExtendedSurface object by sending in its width and height (in pixels), along with optional image_format parameter (default cairo.FORMAT_ARGB32):
```
es = ExtendedSurface(600, 800)
```
The background can be set to a given RGB(A) color, or to a default of opaque white:
```
es.set_background()
```
From here you can draw basic shapes using the DrawSurface attribute:
```
es.draw.rectangle(x=100, y=200, width=300, height=400, color=(255, 0, 0))
```
The available drawing methods are:
- dot()
- ellipse()
- line()
- polygon()
- rectangle()
- rounded_rectangle() (i.e., a rectangle with rounded corners)

You can also write text using the TextSurface attribute:
```
es.text.write("Hello World!", "center", "center", "arial.ttf", font_size=25)
```
The write() method contains many options for customization, including:
- specifying the maximum width and height of the text box
- text alignment (right, center, left, justified)
- setting the location of the text box using a string (e.g., top, bottom, left, right, center)
- text box padding
- text outline with a desired outline width and color
- automatic resizing of the text to fill the text box if a font size is not specified
- support for newlines ('\n') within the text string, including successive newlines (e.g., '\n\n\n')
- automatic line breaks for long lines of text at a specified font size (newlines are still taken into account in this case)

To save the ExtendedSurface object as a PDF or PNG file, simply run:
```
es.write_to_pdf("image.pdf")
```
or
```
es.write_to_png("image.png")
```

# How To Run Examples
There are several examples showcasing the functionality of ExtendedSurface. They are all located in the examples/ folder.
To run one, simply open up a terminal in the ExtendedSurface root folder and run:
```
python3 -m examples.example_*
```
where 'example_*' is the name of an example. When run, it will save the resulting image in the root folder.
Play around and have fun! If you have any comments, questions, or general feedback, feel free to contact me at dylan@puzzlebookspress.com
Have a great day!
