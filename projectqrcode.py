import qrcode

def generate_qr_code( text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

#Input text to genertate QR Code for 
text = "https://github.com/Gale748?tab=repositories"
#File name to save the QR Code
file_name = "qr_code.png"
#Generate QR Code
generate_qr_code(text, file_name)
print(f"QR Code saved as {file_name}")