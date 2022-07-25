from PIL import Image
import os

PATH = "E:\Images\\"
files = os.listdir(PATH)

for file in files:
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        file_path = os.path.join(PATH,file)
        with Image.open(file_path) as img:
            height = img.height
            width = img.width
            ratio = height/width
            if (ratio == 0.625):
                new_img = Image.new("RGB",(2560,2560),(255,255,255))
                new_img.paste(img,(0,480))
                new_img.save(f"{file}_resized.jpg")
            if (ratio == 0.5625):
                new_img_1 = Image.new("RGB",(3840,3840),(255,255,255))
                new_img_1.paste(img,(0,840))
                new_img_1.save(f"{file}_resized.jpg")
            if (width/height == 0.75):
                new_img_2 = Image.new("RGB",(1280,1280),(255,255,255))
                new_img_2.paste(img,(160,0))
                new_img_2.save(f"{file}_resized.jpeg")

            
