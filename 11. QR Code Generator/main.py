import pyqrcode
from pyqrcode import QRCode
import png

s = "www.google.com"

url = pyqrcode.create(s)

url.png("myqr.svg", scale=8)
url.png("myqr.png", scale=8)