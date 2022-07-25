from xml import dom
from PIL import Image
import os
from colorthief import ColorThief

PATH = "E:\Images\\"
files = os.listdir(PATH)

for file in files:
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        fname,fext = file.split(".")
        if os.path.isdir(os.path.join(PATH,file)):
            pass
        else:
            file_path = os.path.join(PATH,file)
        color_thief = ColorThief(file_path)
        dominant_color = color_thief.get_color(quality = 1)
        with Image.open(file_path) as img:
            height = img.height
            width = img.width

            if (height > width):
                new_img = Image.new("RGB",(height,height),dominant_color)
                new_img.paste(img,((height - width) // 2,0)) 
                if file.endswith(".jpg"):
                    new_img.save(os.path.join(PATH,f"{fname}_resized.jpg"))
                elif file.endswith(".jpeg"):
                    new_img.save(os.path.join(PATH,f"{fname}_resized.jpeg"))
                
            if (width > height):
                new_img_1 = Image.new("RGB",(width,width),dominant_color)
                new_img_1.paste(img,(0,(width - height)//2))
                if file.endswith(".jpg"):
                    new_img_1.save(os.path.join(PATH,f"{fname}_resized.jpg"))
                elif file.endswith(".jpeg"):
                    new_img_1.save(os.path.join(PATH,f"{fname}_resized.jpeg"))
                