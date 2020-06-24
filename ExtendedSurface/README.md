# ExtendedSurface

The ExtendedSurface class is intended to replace the need for a pycairo.ImageSurface object, extending its functionality by providing methods that can do in one line what might take several lines to do.

## Basic Functionality
ExtendedSurface depends on pycairo and Pillow:
```
python3 -m pip install --user pycairo Pillow
```
From the ExtendedSurface root folder:
```
from src.ExtendedSurface import ExtendedSurface

es = ExtendedSurface(600, 800)
es.set_background()
es.draw.rectangle(x=100, y=200, width=300, height=400, color=(255, 0, 0))
es.text.write("Hello World!", "center", "center", "arial.ttf", font_size=25)
es.write_to_png("image.png")
```

## Examples
From the ExtendedSurface root folder:
```
python3 -m examples.example_*
```
where 'example_*' is the name of an example. The resulting image will save in the root folder.

If you have any comments, questions, or general feedback, feel free to contact me at dylan@puzzlebookspress.com

Have a great day!
