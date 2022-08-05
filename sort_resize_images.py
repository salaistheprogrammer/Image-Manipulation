from genericpath import isdir
import os
import shutil
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from PIL import Image
from colorthief import ColorThief


SOURCE_DIR = "X:\Pixel&Mortar\PxM Design Studio\\"
PATH = "F:\Export\\"
DEST_PATH = "F:\Export\\square\\"
PORTRAIT_PATH = os.path.join(PATH, "portrait")
LANDSCAPE_PATH = os.path.join(PATH, "landscape")
EXTNS = ["png", "jpg", "jpeg"]

DEFAULT_BRAND = ""


def get_brand_dir(brand):
    BRAND_DIR = f"{SOURCE_DIR}\\3DModels_Onboarded\{brand}"

    return BRAND_DIR


def create_img(img, file_name, img_dimensions, size, dominant_color):
    # Resize image to 1:1 aspect ratio and move to dest folder
    new_img = Image.new("RGB", (size, size), dominant_color)
    new_img.paste(img, img_dimensions)
    new_img.save(os.path.join(DEST_PATH, file_name))

    return new_img


def sort_images(img_path, file_name, width, height):
    if (height > width):
        # portrait
        print(f"Copying {file_name} to {PORTRAIT_PATH}")
        shutil.copy(img_path, os.path.join(
            PORTRAIT_PATH, file_name))

    if (width > height):
        # landscape
        print(f"Copying {file_name} to {LANDSCAPE_PATH}")
        shutil.copy(img_path, os.path.join(
            LANDSCAPE_PATH, file_name))

    return True

def setup_dir(model_img_path):
    # Create folders for square, portrait and landscape
    DEST_PATH = os.path.join(model_img_path, "square")
    PORTRAIT_PATH = os.path.join(model_img_path, "portrait")
    LANDSCAPE_PATH = os.path.join(model_img_path, "landscape")
    if not os.path.isdir(DEST_PATH):
        os.mkdir(DEST_PATH)

    if not os.path.isdir(PORTRAIT_PATH):
        os.mkdir(PORTRAIT_PATH)

    if not os.path.isdir(LANDSCAPE_PATH):
        os.mkdir(LANDSCAPE_PATH)

    return

def process_images(model_img_path):
    # create dest path
    setup_dir(model_img_path)

    for file_name in os.listdir(model_img_path):
        if not os.path.isdir(os.path.join(model_img_path, file_name)):
            print("Processing", file_name)
            fname, fext = file_name.split(".")
            if fext in EXTNS:
                img_path = os.path.join(model_img_path, file_name)
                with Image.open(img_path) as img:
                    height = img.height
                    width = img.width

                    sort_images(img_path, file_name, width, height)

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
    # Get brand name from command line
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-b", "--brand", default=DEFAULT_BRAND,
                        help="Brand Folder Name to be parsed")
    args = vars(parser.parse_args())

    # Set up parameters
    brand = args["brand"]

    brand_dir = get_brand_dir(brand)

    for dir in os.listdir(brand_dir):
        process_images(brand_dir)
        # # go through each model dir in a brand dir
        # if os.path.isdir(os.path.join(brand_dir, dir)):
        #     # process images in each model dir
        #     process_images(os.path.join(brand_dir, dir))
