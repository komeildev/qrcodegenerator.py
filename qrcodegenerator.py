import pyqrcode
from pyqrcode import QRCode
s="www.gopythontutorial.wordpress.com"
url=pyqrcode.create(s)
url.svg("MyFirstQRCode.svg",scale=10)