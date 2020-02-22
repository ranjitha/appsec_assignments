# Application Security Assignment 1

Pillow is a Python library for dealing with imaging .

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pillow.

```bash
pip3 install pillow
```

## Usage

```python
from PIL import Image

# input image from user via terminal/command line 
# initialize this file to a variable, say img

Image.new(mode, size, color) 
# returns a new image object
# mode: The mode to use for the new image (eg., it could be RGB, RGBA)
# size: A 2-tuple containing (width, height) in pixels
# color will decide the color scheme for the pads for the image, if any

img.paste(im, box, mask=None)
# pastes another image into this image
# im is the source image or pixel value
# box is an optional 4-tuple giving the region to paste into. 
# If a 2-tuple is used instead, it’s treated as the upper left corner
# If omitted or None, the source is pasted into the upper left corner
# If an image is given as the second argument and there is no third, the box defaults to (0, 0), and the second argument is interpreted as a mask image.
# mask is an optional mask image

img.size # returns a tuple with (width, height)

img.resize((new_width, new_height)) # returns a new scaled image with the new dimensions that are passed as arguments

img.show() # displays the temporary image 

img.save("new_filename_for_image.png") # saves the newly scaled image to the working directory with the new filename and an extension, as specified
```
## Execution

To Run image_squarifier.py:

1. Ensure the library pillow is installed on your system
2. Clone repository from github.
3. cd to (your) correct directory with the provided code
4. Run python image_squarifier.py
5. Provide the path for the image that needs to be scaled or padded to a square
6. In case of a padded image, choose the colours from RGB for the pad
7. An outputted squarified image will be displayed and then saved to your working directory with the new filename and extension provided by the executor

## Contributing
This project was done in collaboration with Michael Kochera.
