from PIL import Image

image = Image.open('1.jpg')
image.rotate(45).show()