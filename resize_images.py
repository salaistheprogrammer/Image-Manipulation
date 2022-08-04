from genericpath import isdir
from xml import dom
from PIL import Image
import os
from colorthief import ColorThief

PATH = "F:\Export\\"
DEST_PATH = "F:\Export\\square\\"
EXTNS = ["png", "jpg", "jpeg"]


def create_img(img, file_name, img_dimensions, size, dominant_color):
    new_img = Image.new("RGB", (size, size), dominant_color)
    new_img.paste(img, img_dimensions)
    new_img.save(os.path.join(DEST_PATH, file_name))

    return new_img

def process_images():
    for file_name in os.listdir(PATH):
        if not os.path.isdir(os.path.join(PATH, file_name)):
            print("Processing", file_name)
            fname, fext = file_name.split(".")
            if fext in EXTNS:
                img_path = os.path.join(PATH, file_name)
                with Image.open(img_path) as img:
                    height = img.height
                    width = img.width

                    if height != width:
                        color_thief = ColorThief(img_path)
                        dominant_color = color_thief.get_color(quality=1)

                        if (height > width):
                            # portrait
                            create_img(img, file_name, img_dimensions=(
                                (height - width) // 2, 0), size=height, dominant_color=dominant_color)

                        if (width > height):
                            # landscape
                            create_img(img, file_name, img_dimensions=(
                                0, (width - height)//2), size=width, dominant_color=dominant_color)

if __name__ == "__main__":
    if not os.path.isdir(DEST_PATH):
        os.mkdir(DEST_PATH)
    process_images()