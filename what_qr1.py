import qrcode

numero = "549xxxxxxxx"
mensaje = "hola, quiero comunicarme contigo gracias"
url = f'https://wa.me/{numero}?text-{mensaje.replace(' ','%20')}'

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)
imagen = qr.make_image(fil_color ="black",back_color="white")
imagen.save("codigo qr de whatsapp.png")
print("codigo generado exitosamente")