#qr code generator

#create qr
import qrcode as qr
img = qr.make("https://github.com/RamParmar1/python/mini-project/qrcode_generator")
img.save('Mine_GitHub.png') #give name that you want

#create and enhance qr
#qr as variable/function
'''import qrcode
from PIL import Image
qr = qrcode.QRCode( version=1 ,
                    error_correction = qrcode.constants.ERROR_CORRECT_H ,
                    box_size = 10 , border = 10  )
qr.add_data("https://github.com/RamParmar1/python/mini-project/qrcode_generator")
qr.make(fit = True)
img = qr.make_Image(fill_color = "red" , back_color = "white")
img.save("Mine_GitHub.png")
'''
