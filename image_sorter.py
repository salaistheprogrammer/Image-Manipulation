import PIL
from PIL import Image
import os
import shutil


FORMATS = [".jpg", ".jpeg", ".png", ".gif",".raw", ".cr2", ".nef", ".orf", ".sr2", ".eps", ".bmp", ".tif", ".tiff"]


def if_folder_exists(path):
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)


def sort_images(path):
    for image in os.listdir(path):
        image_path = os.path.join(path, image)
        
        fname, fext = os.path.splitext(image_path)
        
        if fext in FORMATS:
            with Image.open(image_path) as img:
                width, height = img.size
            
            if height == width:
                path_s = os.path.join(path, "Sqaure")
                if_folder_exists(path_s)
                shutil.move(image_path, path_s)
            
            elif height > width:
                path_p = os.path.join(path, "Potrait")
                if_folder_exists(path_p)
                shutil.move(image_path, path_p)
            
            else:
                path_ls = os.path.join(path, "Landscape")
                if_folder_exists(path_ls)
                shutil.move(image_path, path_ls)
        

sort_images("D:\Saidhu\Images")