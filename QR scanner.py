import qrcode 
url=input()
gen_img=qrcode.make(url)
gen_img.save("qrcodee.png")