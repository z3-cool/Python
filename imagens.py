
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps

ANCHO = 1280
ALTO = 720

def preparar_miniatura(ruta_imagen, carpeta_salida):

    try:
        imagen = Image.open(ruta_imagen).convert("RGB")
        miniatura = ImageOps.fit(
            imagen,
            (ANCHO, ALTO),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5)
        )

        nombre = os.path.splitext(
            os.path.basename(ruta_imagen)
        )[0]

        ruta_salida = os.path.join(
            carpeta_salida,
            nombre + "_youtube.jpg"
        )

        miniatura.save(
            ruta_salida,
            "JPEG",
            quality=95,
            optimize=True
        )

        return True

    except Exception as error:

        print("Error:", error)

        return False

def seleccionar_imagenes():

    archivos = filedialog.askopenfilenames(

        title="Selecciona las imágenes",

        filetypes=[
            (
                "Imágenes",
                "*.jpg *.jpeg *.png *.webp *.bmp"
            ),
            (
                "Todos los archivos",
                "*.*"
            )
        ]
    )

    if not archivos:
        return

    carpeta_salida = filedialog.askdirectory(
        title="Selecciona la carpeta de salida"
    )

    if not carpeta_salida:
        return

    cantidad = 0
    for archivo in archivos:
        resultado = preparar_miniatura(
            archivo,
            carpeta_salida
        )

        if resultado:
            cantidad += 1

    messagebox.showinfo(
        "Proceso terminado",
        f"Se procesaron {cantidad} imágenes.\n\n"
        f"Formato: {ANCHO} x {ALTO} píxeles\n"
        f"Relación: 16:9\n"
        f"Formato: JPG"
    )

ventana = tk.Tk()
ventana.title(
    "Generador de Miniaturas para YouTube"
)

ventana.geometry("600x400")
ventana.resizable(False, False)
ventana.configure(bg="red")

titulo = tk.Label(
    ventana,
    text="GENERADOR DE MINIATURAS",
    font=("Arial", 22, "bold"),
    bg="red",
    fg="white"
)

titulo.pack(pady=40)
descripcion = tk.Label(
    ventana,
    text=(
        "Selecciona varias imágenes y conviértelas\n"
        "automáticamente al formato de YouTube."
    ),
    font=("Arial", 13),
    justify="center",
    bg="red",
    fg="white"
)

descripcion.pack(pady=10)
boton = tk.Button(
    ventana,
    text="SELECCIONAR IMÁGENES",
    font=("Arial", 14, "bold"),
    padx=30,
    pady=15,
    command=seleccionar_imagenes,
    bg="blue",
    fg="white",
    activebackground="blue",
    activeforeground="white"
)

boton.pack(pady=35)
informacion = tk.Label(
    ventana,
    text="1280 × 720 px  |  16:9  |  JPG",
    font=("Arial", 11),
    bg="red",
    fg="white"
)

informacion.pack()
ventana.mainloop()

