#qr code generator

import qrcode as qr
import os
from PIL import Image

img = qr.make("https://github.com/RamParmar1/python/mini-project/qrcode_generator")
img.save('Mine_GitHub.png')
print("Image Done")
img = Image.open("Mine_GitHub.png")
img.show()

