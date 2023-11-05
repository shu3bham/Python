import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

qr.add_data("https://www.w3schools.com/python/default.asp")
qr.make(fit = True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.save(r"C:\\Users\shubham.deshmukh\\OneDrive - Perficient, Inc\Desktop\\github_repo\Python\\Python Projects\\QR_code\\export\QR_Code_custom.png")