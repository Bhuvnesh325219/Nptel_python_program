
from PIL import Image

import cv2

# img=Image.open('img.jpg')
# transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
# transposed_img.save('corr.jpg')
# print("Done")





img =cv2.imread('img.jpg')

clahe =cv2.createCLAHE()

gray_img =cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

enh_img =clahe.apply(gray_img)

s="Bhuvnesh"

print(sorted(s))

