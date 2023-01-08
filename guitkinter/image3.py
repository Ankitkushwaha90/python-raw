from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob("1.jpg"):
file,ext = os.path.splitext(image)
image = Image.open(image)
image.thumbnail(size, Image.ANTIALIAS)
image.save(file + ".thumbnail", "JPEG")