from PIL import Image,ImageChops
import numpy as np

col = Image.open("Gambar 2.png")
gray = col.convert('L')

bw = np.asarray(gray).copy()

bw[bw < 128] = 0    # Black
bw[bw >= 128] = 255 # White

imfile = Image.fromarray(bw)

inv_img = ImageChops.invert(imfile)
inv_img.save("inverted.png")