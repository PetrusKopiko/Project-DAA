from PIL import Image
import numpy as np

col = Image.open("image.png")
gray = col.convert('L')

# Let numpy do the heavy lifting for converting pixels to pure black or white
bw = np.asarray(gray).copy()

# Pixel range is 0...255, 256/2 = 128
bw[bw < 100] = 0    # Black
bw[bw >= 100] = 255 # White

# Now we put it back in Pillow/PIL land
imfile = Image.fromarray(bw)
imfile.save("result_bw.png")