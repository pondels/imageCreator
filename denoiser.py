import cv2
import numpy as np
from matplotlib import pyplot as plt


def denoise_image(path):
    image = cv2.imread(path)
    dst = cv2.fastNlMeansDenoisingColored(image)

    plt.subplot(121),plt.imshow(image)
    plt.subplot(121),plt.imshow(dst)
    plt.show()

denoise_image('generatedImage.png') 