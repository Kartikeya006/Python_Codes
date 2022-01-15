import pyqrcode
data = 'Kartikeya Gupta\n190106021\n190106021@hbtu.ac.in\n2nd Electronics Engineering'
img = pyqrcode.create(data)
img.png("Information.png", scale=10)
