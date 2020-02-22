from PIL import Image

def scale(im, min_size=256):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = im.resize((size,size))
    return new_im

def padding(im, fill_color, min_size=256):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def generate_new_image(image):
    try:
        test_image = Image.open(image)
        choice = input("Would you like to scaled the image or add padding?\n(Type s for scaled and p for transparent padding): ")
        while(choice.lower() != "s" and choice.lower() != "p"):
            print("Didn't enter s or p. Please choose the right option.")
            choice = input("Would you like to scaled the image or add padding?\n(Type s for scaled and p for transparent padding): ")
        if(choice.lower() == "s"):
            new_image = scale(test_image)
        elif(choice.lower() == "p"):
            print("Enter RGB value wanted for pads")
            R_Value = input("Enter R Value(0-255): ")
            while(int(R_Value) > 255 or int(R_Value) < 0):
                R_Value = input("Enter R Value(0-255): ")
            G_Value = input("Enter G Value(0-255): ")
            while(int(G_Value) > 255 or int(G_Value) < 0):
                G_Value = input("Enter G Value(0-255): ")
            B_Value = input("Enter B Value(0-255): ")
            while(int(B_Value) > 255 or int(B_Value) < 0):
                B_Value = input("Enter B Value(0-255): ")
            fill_color = (int(R_Value), int(G_Value), int(B_Value))
            new_image = padding(test_image, fill_color)
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