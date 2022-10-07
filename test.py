from PIL import Image
from itertools import permutations

class GenerateImage:

    def __init__(self, color_mode='RGB', width=7680, height=4320, filename='generatedImage', format='png'):
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
            # x = i
            for j in range(self.height):
                y = j - self.height // 2
                # y = j

                pallen = len(self.palette)
                # randomNumber = 14 * (1920/1080) * (self.height/self.width)
                randomNumber = 15500/(min(self.width, self.height) ** 2)
                index = int(round(i*i*randomNumber, 0)) + int(round(j*j*randomNumber, 0))
                # index = int(round(x*x*x*randomNumber, 0)) + int(round(y*y*y*randomNumber, 0))
                if index >= pallen: index = pallen - 1
                elif index < 0: index = 0
                grabber = pallen - 1 - index
                color = self.palette[grabber]
                # color = (n << 21) + (n << 10) + n*8
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

        modifier = .1/(2*(self.height/800))
        iterations = 255

        for i in range(self.height):
            x = i - self.height // 2
            for j in range(self.width):
                y = j - self.width // 2
                a = -.05 + x*modifier
                b = -.05 + y*modifier
                # c = -.5 + (x+y)*modifier

                ca = a
                cb = b
                # cc = c

                n = iterations

                while n > 1:
                    aa = a*a + b*b
                    bb = 2 * a * b
                    # ccc = a * b * c

                    a = aa + ca
                    b = bb + cb
                    # c = ccc + cc

                    # if (abs(a + b + c) > 25): break
                    if (abs(a + b) > 25): break
                    n -= 1

                color = (n << 21) + (n << 10) + n*8
                image.putpixel((j, i), color)
            if (self.height - i) % (self.height * .1) == 0: image.save(self.image_name)
        image.save(self.image_name)

    def formula4(self):
        # Julia Set
        image = Image.open(self.image_name)

        zoom = 1
        cX, cY = -0.7, 0.27015
        moveX, moveY = 0.0, 0.0
        maxIter = 255
    
        for i in range(self.width):
            for j in range(self.height):

                zx = 1.5*(i - self.width/2)/(0.5*zoom*self.width) + moveX
                zy = 1.0*(j - self.height/2)/(0.5*zoom*self.height) + moveY
                n = maxIter
                while zx*zx + zy*zy < 4 and n > 1:
                    tmp = zx*zx - zy*zy + cX
                    zy,zx = 2.0*zx*zy - cY, tmp
                    n -= 1
    
                # convert byte to RGB (3 bytes), kinda 
                # magic to get nice colors
                color = (n << 21) + (n << 10) + n*8
                image.putpixel((i, j), color)
            if (self.height - i) % (self.height * .1) == 0: image.save(self.image_name)
        image.save(self.image_name)

    def formula5(self):
        pass
    
GI = GenerateImage(filename='julia')
# GI.formula1()
# GI.formula2() # My Own
# GI.formula3() # Backrooms???
GI.formula4() # Manipulated Julia Set