# Using py2
# pip install qrcode[pil]

import qrcode

data = "https://github.com/gabrielSSimoura?tab=repositories"

filename = "web.png"

img = qrcode.make(data)

img.save(filename)

