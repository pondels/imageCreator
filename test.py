from PIL import Image
from itertools import permutations
import random
# import cv2

class GenerateImage:

    def __init__(self, color_mode='RGB', width=3380, height=2160, filename='generatedImage', format='png'):
        '''
            color_mode = 'RGB' by default
            width = 1920 by default
            height = 1080 by default
            filename = generatedImage by default
            format = png by default
        '''
        self.color_mode = color_mode
        self.width = width
        self.height = height
        self.image_name = f'{filename}.{format}'

        self.im = Image.new(self.color_mode, (self.width, self.height), (0, 0, 0))
        self.im.save(self.image_name)

        self.palette = list(permutations([i for i in range(256)], 3))

    def formula1(self):

        image = Image.open(self.image_name)

        for i in range(self.width):
            x = i - self.width // 2
            for j in range(self.height):
                y = j - self.height // 2

                pallen = len(self.palette)
                # randomNumber = 14 * (1920/1080) * (self.height/self.width)
                randomNumber = 15500/(min(self.width, self.height) ** 2)
                # index = int(round(i*i*randomNumber, 0)) + int(round(j*j*randomNumber, 0))
                index = int(round(x*x*x*randomNumber, 0)) + int(round(y*y*y*randomNumber, 0))
                if index >= pallen: index = pallen - 1
                elif index < 0: index = 0
                grabber = pallen - 1 - index
                color = self.palette[grabber]
                image.putpixel((i, j), color)

        image.save(self.image_name)

    def formula2(self):

        image = Image.open(self.image_name)

        iterations = 255
        for i in range(self.width):
            for j in range(self.height):
                a = -i
                b = j
                z = a + b
                n = 0
                while n < iterations:
                    a += a
                    b += b
                    z = abs(a + b)

                    if (z > iterations ** 5): break
                    n += 1
                amount = i*j*n
                if amount >= len(self.palette): amount = len(self.palette) - 1
                elif amount == 0: amount = 1
                # color = self.palette[16581119 % amount]
                color = (n << 21) + (n << 10) + n*8
                image.putpixel((i, j), color)
        image.save(self.image_name)

    def formula3(self):

        image = Image.open(self.image_name)

        modifier = .01/(2*(self.height/800))
        iterations = 255

        for i in range(self.width):
            x = i - self.width // 2
            for j in range(self.height):
                y = j - self.height // 2
                a = -.5 + x*modifier
                b = -.5 + y*modifier

                ca = a
                cb = b

                n = 0

                while n < iterations:
                    aa = a*a - b*b
                    bb = 2 * a * b

                    a = aa + ca
                    b = bb + cb

                    if (abs(a + b) > 16): break
                    n += 1

                if n == 0: n = 1
                # color = self.palette[16581119 % int(round(n * n * 16.581119, 0))]
                color = (n << 21) + (n << 10) + n*8
                image.putpixel((i, j), color)
        image.save(self.image_name)

    def formula4(self):
        # Julia Set
        image = Image.open(self.image_name)

        zoom = 1
        cX, cY = -0.7, 0.27015
        moveX, moveY = 0.0, 0.0
        maxIter = 255
    
        for x in range(self.width):
            for y in range(self.height):
                zx = 1.5*(x - self.width/2)/(0.5*zoom*self.width) + moveX
                zy = 1.0*(y - self.height/2)/(0.5*zoom*self.height) + moveY
                i = maxIter
                while zx*zx + zy*zy < 4 and i > 1:
                    tmp = zx*zx - zy*zy + cX
                    zy,zx = 2.0*zx*zy + cY, tmp
                    i -= 1
    
                # convert byte to RGB (3 bytes), kinda 
                # magic to get nice colors
                color = (i << 21) + (i << 10) + i*8
                image.putpixel((x, y), color)
        image.save(self.image_name)

GI = GenerateImage()
GI.formula4()