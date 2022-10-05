from PIL import Image
from itertools import permutations
import random
# import cv2

class GenerateImage:

    def __init__(self, color_mode='RGB', width=1920, height=1080, filename='generatedImage', format='png'):
        '''
            color_mode = 'RGB' by default
            width = 1280 by default
            height = 720 by default
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

    def formula(self):

        image = Image.open(self.image_name)

        for i in range(self.width):
            for j in range(self.height):
                
                pallen = len(self.palette)
                randomNumber = 12
                index = int(round(i*i*randomNumber, 0)) + int(round(j*j*randomNumber, 0))
                if index >= pallen: index = pallen - 1
                elif index < 0: index = 0
                grabber = pallen - 1 - index
                color = self.palette[grabber]
                image.putpixel((i, j), color)
        image.save(self.image_name)

    def formula2(self):

        image = Image.open(self.image_name)

        iterations = 1000
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
                color = self.palette[amount]
                image.putpixel((i, j), color)
        image.save(self.image_name)

    def mandelbrot(self):

        image = Image.open(self.image_name)

        modifier = .01/(2*(self.height/800))
        iterations = 50

        for i in range(self.width):
            for j in range(self.height):
                a = -2 + i*modifier
                b = -2 + j*modifier

                ca = a
                cb = b

                n = 0

                while n < iterations:
                    aa = a*a + b*b
                    bb = 2 * a * b

                    a = aa + ca
                    b = bb + cb

                    if (abs(a + b) > 16): break
                    n += 1

                color = self.palette[int(round(n * n * 16.581119, 0))]
                image.putpixel((i, j), color)
        image.save(self.image_name)

GI = GenerateImage()
GI.mandelbrot()