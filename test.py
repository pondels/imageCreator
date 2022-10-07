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

        self.palette = list(permutations([i for i in range(256)], 3))
        self.image_directory = './images/'
        self.im.save(self.image_directory + self.image_name)

    def circles(self):

        image = Image.open(self.image_directory + self.image_name)

        for i in range(self.height):
            for j in range(self.width):

                pallen = len(self.palette)
                randomNumber = 15500/(min(self.width, self.height) ** 2)
                index = int(round(i*i*randomNumber, 0)) + int(round(j*j*randomNumber, 0))
                if index >= pallen: index = pallen - 1
                elif index < 0: index = 0
                grabber = pallen - 1 - index
                color = self.palette[grabber]
                image.putpixel((j, i), color)
            if (self.width - i) % (self.width * .1) == 0: image.save(self.image_directory + self.image_name)
        image.save(self.image_directory + self.image_name)

    def lazer(self):

        image = Image.open(self.image_directory + self.image_name)

        iterations = 255
        for i in range(self.width):
            for j in range(self.height):
                a = -i//2
                b = j
                z = a + b
                n = 0
                while n < iterations:
                    a += a
                    b += b
                    z = abs(a + b)

                    if (z > iterations*2): break
                    n += 1
                amount = n
                if amount >= len(self.palette): amount = len(self.palette) - 1
                elif amount == 0: amount = 1
                color = (amount << 21) + (amount << 10) + amount*8
                image.putpixel((i, j), color)
            if (self.height - i) % (self.height * .1) == 0: image.save(self.image_directory + self.image_name)
        image.save(self.image_directory + self.image_name)

    def backrooms(self):

        image = Image.open(self.image_directory + self.image_name)

        modifier = .01/(2*(self.height/800))
        iterations = 255

        for i in range(self.height):
            x = i - self.height // 2
            for j in range(self.width):
                y = j - self.width // 2
                a = -.05 + x*modifier # - self.height // (i*i + 1)
                b = -.05 + y*modifier # - self.width // (j*j + 1)
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
            if (self.height - i) % (self.height * .1) == 0: image.save(self.image_directory + self.image_name)
        image.save(self.image_directory + self.image_name)

    def album(self):
        # Julia Set
        image = Image.open(self.image_directory + self.image_name)

        zoom = 1
        cX, cY = -0.7, 0.27015
        moveX, moveY = 0.0, 0.0
        maxIter = 255
    
        for i in range(self.width):
            for j in range(self.height):

                zx = 1.5*(i - self.width/2)/(0.5*zoom*self.width) + moveX
                zy = 1.0*(j - self.height/2)/(0.5*zoom*self.height) + moveY
                n = maxIter
                while zx-zx * zy-zy < 10 and n > 1:
                    # tmp = zx*zx - zy*zy + cX
                    tmp = zx+zx * zy-zy / cX
                    # zy,zx = 2.0*zx*zy - cY, tmp
                    zy,zx = 2.0*zx*zy // cY, tmp
                    n -= 1
    
                # convert byte to RGB (3 bytes), kinda 
                # magic to get nice colors
                color = (-n << 21) + (-n << 10) + n*8
                image.putpixel((i, j), color)
            if (self.height - i) % (self.height * .1) == 0: image.save(self.image_directory + self.image_name)
        image.save(self.image_directory + self.image_name)

    def formula5(self):
        image = Image.open(self.image_directory + self.image_name)

        zoom = 1
        cX, cY = -0.369, -0.17015
        moveX, moveY = 0.0, 0.0
        maxIter = 255
    
        for i in range(self.width):
            for j in range(self.height):

                zx = 1.5*(i - self.width/2)/(0.5*zoom*self.width) + moveX
                zy = 1.0*(j - self.height/2)/(0.5*zoom*self.height) + moveY
                n = maxIter
                while zx-zy * zx-zy < 10 and n > 1:
                    tmp = zy-zx * zx-zy / cY
                    zy,zx = 2.0*zx-zy / cX, tmp
                    n -= 1

                color = (-n << 21) + (-n << 10) + -n*8
                image.putpixel((i, j), color)
            if (self.height - i) % (self.height * .1) == 0: image.save(self.image_directory + self.image_name)
        image.save(self.image_directory + self.image_name)
    
    def jumpin(self):
        image = Image.open(self.image_directory + self.image_name)

        zoom = 1
        cX, cY = -0.369, -0.17015
        moveX, moveY = 0.075, -0.08

        modifier = .00001/(2*(self.height/800))
        iterations = 255

        for i in range(self.height):
            x = i - self.height // 2
            for j in range(self.width):
                y = j - self.width // 2
                a = -1 + x*modifier
                b = -.05 + y*modifier
                
                ca = a
                cb = b

                zx = 1.5*(i - self.width/2)/(5*zoom*self.width) + moveX
                zy = 1.0*(j - self.height/2)/(5*zoom*self.height) + moveY
                
                n = iterations

                while zx-zy * zx-zy < 10 and n > 1:
                    aa = a*a + b*b
                    bb = 2 * a * b


                    tmp = zx*zx + zy*zy / cX
                    zy,zx = 2.0*zx-zx / cY, tmp

                    a = aa + ca - zy
                    b = bb + cb - zx

                    if (abs(-a - b - zx - zy) > 25): break
                    n -= 1

                color = (n << 21) + (n << 10) + n*8
                image.putpixel((j, i), color)
            if (self.height - i) % (self.height * .1) == 0: image.save(self.image_directory + self.image_name)
        image.save(self.image_directory + self.image_name)

GI = GenerateImage(width = 1280, height = 720, filename='test')
# GI.cricles()
# GI.lazer() # My Own
# GI.backrooms() # Backrooms???
# GI.album() # Manipulated Julia Set
GI.formula5() # Manipulated Julia Set 2
# GI.jumpin()