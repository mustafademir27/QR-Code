import qrcode
import image

qr = qrcode.QRCode(
    version = 15,   #15 means version of the qr code 
    box_size = 10,  #size of the box where qr code will be displayed
    border = 4  #is it white part   of image
 )

data = ('https://github.com/mustafademir27?tab=repositories')  
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color = "white")
img.save("github.png")


# basic form for qr code
'''
code = qrcode.make('https://app.patika.dev/paths')
code.save('qrcode1.png')
'''