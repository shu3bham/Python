import qrcode as qc 

img = qc.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
img.save(r"C:\\Users\shubham.deshmukh\\OneDrive - Perficient, Inc\Desktop\\github_repo\Python\\Python Projects\\QR_code\\export\QR_Code.png")