#Text To Handwriting

import pywhatkit as pw
import os
from PIL import Image

txt = "This is a test of handwriting conversion."
pw.text_to_handwriting(txt, "demo_test.png", [0,0,138])
print("DONE")


img = Image.open("demo_test.png")
img.show()
