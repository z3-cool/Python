import qrcode

numero = "549XXXXXXXXXX"
mensaje = "Hola, quiero comunicarme contigo."
url = f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)
imagen = qr.make_image(fill_color="black", back_color="white")
imagen.save("codigo_qr_whatsapp.png")
print("Código QR creado correctamente.")