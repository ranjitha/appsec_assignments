from PIL import Image

def stretch(im, min_size=256):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = im.resize((size,size))
    return new_im

def transparent_padding(im, min_size=256,fill_color = (0,0, 0,0) ):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def generate_new_image(image):
    try:
        test_image = Image.open(image)
        choice = input("Would you like to stretch the image or add transparent padding?\n(Type s for stretch and p for transparent padding): ")
        while(choice.lower() != "s" and choice.lower() != "p"):
            print("Didn't enter s or p. Please choose the right option.")
            choice = input("Would you like to stretch the image or add transparent padding?\n(Type s for stretch and p for transparent padding): ")
        if (choice.lower() == "s"):
            new_image = stretch(test_image)
        elif (choice.lower() == "p"):
            new_image = transparent_padding(test_image)
        new_image.show()
        new_image.save(new_image_name)
    except:
        raise OSError("Improper Path")

if __name__=="__main__":
    done = False
    while(done == False):
        image = input("Please enter a path to an image: ")
        new_image_name = input("Enter new file name for scaled image: ")
        generate_new_image(image)
        done = True