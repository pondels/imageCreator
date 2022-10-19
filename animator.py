from PIL import Image

def make_gif(frame_folder):
    frames = [f'./animation/{frame}.png' for frame in range(120)]
    frames = [Image.open(image) for image in frames]
    frame_one = frames[0]
    frame_one.save("circles.gif", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)
    
if __name__ == "__main__":
    make_gif("./animation")