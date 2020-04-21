import glob
from PIL import Image
import numpy as np
#https://stackoverflow.com/questions/51178166/iterate-through-folder-with-pillow-image-open

images = glob.glob("output/*.jpg")
for image in images:
    with open(image, 'rb') as file:
        img = Image.open(file)
        img=np.array(img)
        a=img.shape
        print(a,image)