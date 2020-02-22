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

img.size # returns a tuple with (width, height)
img.resize((new_width, new_height)) # returns a new scaled image with the new dimensions that are passed as arguments
img.show() # displays the temporary image 
img.save("new_filename_for_image.png") # saves the newly scaled image to the working directory with the new filename with extension .png
```
## Execution

To Run image_squarifier.py:

1. Ensure the library pillow is installed on your system
2. Clone repository from github.
3. cd to (your) correct directory with the provided code
4. Run python image_squarifier.py
5. Provide the path for the image that needs to be scaled to a square
6. An outputted squarified image will be displayed and then saved to your working directory with the new filename provided by the executor

## Contributing
This project was done in collaboration with Michael Kochera.
