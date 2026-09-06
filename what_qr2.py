import qrcode
from PIL import Image, ImageDraw
print("=== lo hacemos con un toque especial ===")
numero = "549xxxxxx"
mensaje = "hola puedo comunicarme contigo gracias"
archivo_salida = "QR_WhatsApp.png"
import urllib.parse
mensaje_codificado = urllib.parse.quote(mensaje)
url_whatsapp = (
    f"https://wa.me/{numero}?text={mensaje_codificado}" 
)

qr = qrcode.QRCode(
    version =5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4
)
qr.add_data(url_whatsapp)
qr.make(fit=True)
imagen_qr = qr.make_image(
    fill_color = "black",
    back_color = "white"
).convert("RGB")

logo_size = 180
logo = Image.new(
    "RGB",
    (logo_size, logo_size),
    "white"
)

draw = ImageDraw.Draw(logo)
draw.ellipse(
    (10,10, logo_size -10, logo_size -10),
    fill = "#25D366"
)

draw.ellipse(
    (48,48, logo_size -48, logo_size -48),
    fill = "white"
)

draw.arc(
    (65,58,125,125),
    start=130,
    end=330,
    fill ="#25D366",
    width=12
)
draw.line(
    (62,125,88,112),
    fill ="#25D366",
    width=10
)
draw.line(
    (62,125,88,117),
    fill ="#25D366",
    width=10
)

posicion_x = (imagen_qr.width - logo.width)//2
posicion_y = (imagen_qr.height - logo.height)//2

imagen_qr.paste(
    logo,
    (posicion_x, posicion_y)
)

imagen_qr.save(
    archivo_salida,
    quality=100
)
print("=======================")
print("QR DE WHATSAPP CREADO")
print("=======================")
print(f'Archivo: {archivo_salida}')
print(f'Numero: {numero}')
print("=======================")