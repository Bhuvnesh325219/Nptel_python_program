import numpy

from PIL import Image

im = Image.open('corr.jpg')

pixelMap = im.load()

print(pixelMap)

I = numpy.asanyarray(Image.open('corr.jpg'))

# compress the image


img = Image.new(im.mode, im.size)

pixelNew = img.load()

'''

0-31    =0 
32-63   =1
64-95   =2
96-127  =3
128-159 =4
160-191 =5
192-223 =6
224-255 =7

'''

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if 0 <= pixelMap[i, j] <= 31:
            pixelNew[i, j] = 0
        if 32 <= pixelMap[i, j] <= 63:
            pixelNew[i, j] = 1
        if 64 <= pixelMap[i, j] <= 95:
            pixelNew[i, j] = 2
        if 96 <= pixelMap[i, j] <= 127:
            pixelNew[i, j] = 3
        if 128 <= pixelMap[i, j] <= 159:
            pixelNew[i, j] = 4
        if 160 <= pixelMap[i, j] <= 191:
            pixelNew[i, j] = 5
        if 192 <= pixelMap[i, j] <= 223:
            pixelNew[i, j] = 6
        if 224 <= pixelMap[i, j] <= 255:
            pixelNew[i, j] = 7

img.save('corr2.jpg')

J = numpy.asanyarray(Image.open('corr2.jpg'))

print(J)
