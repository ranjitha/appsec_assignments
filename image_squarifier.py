from PIL import Image

def make_square(im, min_size=256):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = im.resize((size,size))
    return new_im

if __name__=="__main__":
    done = False
    while(done == False):
        image = input("Please enter a path to an image: ")
        new_image_name = input("Enter new file name for scaled image: ")
        try:
            test_image = Image.open(image)
            new_image = make_square(test_image)
            new_image.show()
            new_image.save("new_image_name")
            done = True
        except:
            raise OSError("Improper Path")