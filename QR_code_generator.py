import pyqrcode
data = input()
img = pyqrcode.create(data)
img.png("Information.png", scale=10)
