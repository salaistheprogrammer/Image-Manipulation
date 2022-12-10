from PIL import Image
import numpy as np
from numpy import asarray

def MSE(image1, image2):
    img1, img2 = asarray(image1), asarray(image2)
    mean = ((np.sum(img1, dtype="float") - np.sum(img2, dtype = "float"))**2)

    if mean == 0.0:
        print("The Images are same.")
    else:
        print("The Images are different.")
    return mean
    

def compare_image(path1, path2):
    with Image.open(path1) as image1:
        with Image.open(path2) as image2:
            MSE(image1, image2)

    

