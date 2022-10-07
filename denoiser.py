import cv2
from PIL import Image

def denoise_image(path, name):
    image = cv2.imread(path)
    dst = cv2.fastNlMeansDenoising(image)
    im = Image.fromarray(dst)
    im.save(f'images/denoised_{name}.png')

    # plt.subplot(121),plt.imshow(image)
    # plt.subplot(121),plt.imshow(dst)
    # plt.show()

denoise_image('images/hallway.png', 'canit')