#qrcode enhanced

import qrcode
import os
from PIL import Image

#Here qr as variable/function
qr = qrcode.QRCode( version=1 ,
                    error_correction = qrcode.constants.ERROR_CORRECT_H ,
                    box_size = 10 , border = 10  )
qr.add_data("https://github.com/RamParmar1/python/mini-project/qrcode_generator")
qr.make(fit = True)
img = qr.make_Image(fill_color = "red" , back_color = "white")
img.save("Mine_GitHub.png")

print("Image Created Successfully")
img = Image.open("Mine_GitHub.png")
img.show()
