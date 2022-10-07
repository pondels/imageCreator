import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def denoise_image(path, name):
    image = cv2.imread(path)
    dst = cv2.fastNlMeansDenoisingColored(image)
    im = Image.fromarray(dst)
    im.save(f'denoised_{name}.png')

    plt.subplot(121),plt.imshow(image)
    plt.subplot(121),plt.imshow(dst)
    plt.show()

denoise_image('mandelbrot.png', 'mandelbrot') 