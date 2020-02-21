from PIL import Image

def make_square(image, min_size=256):
    x, y = image.size
    size = max(min_size, x, y)
    new_image = image.resize((size, size))
    return new_image

if __name__=="__main__":
    done = False
    while(done == False):
        image_source_path = input("Please enter a path to an image: ")
        try:
            test_image = Image.open(image_source_path)
            generated_square_image = make_square(test_image)
            generated_square_image.show()
            generated_square_image.save("saved_square_image.png")
            done = True
        except:
            raise OSError("Improper Path to file")
