import qrcode
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    )

qr.add_data('https://jabaripowery.github.io/Resume/')

qr.make(fit=True)

img = qr.make_image(fill_color=(217,217,217), back_color=(64,64,64))

img.save("resume-qr.png")