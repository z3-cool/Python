
# pip install qrcode[pil]
print("======================")
print("ENTORNO VIRTUALIZADO")
print("======================")
print("""
-------------------------------
Auditor de red + generador QR
-------------------------------

Detecta la IP local.
Detecta el nombre del equipo.
Obtiene la IP pública opcionalmente.
Permite introducir una IP o URL.
Comprueba conectividad mediante ping.
Genera un QR con el resultado.
Guarda el QR como imagen PNG.
Guarda el informe como .txt.
""")
import tkinter as tk
from tkinter import messagebox, filedialog
import socket
import platform
import subprocess
import qrcode


def obtener_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "No disponible"


def obtener_datos():
    equipo = socket.gethostname()
    ip = obtener_ip_local()
    sistema = platform.system()
    version = platform.version()

    datos = f"""
AUDITORÍA DE RED
========================

Equipo: {equipo}
IP local: {ip}
Sistema operativo: {sistema}
Versión: {version}
"""

    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, datos)


def comprobar_conexion():
    objetivo = entrada_ip.get().strip()

    if not objetivo:
        messagebox.showwarning("Aviso", "Introduce una IP o dominio")
        return

    try:
        comando = ["ping", "-n", "1", objetivo]

        proceso = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        if proceso.returncode == 0:
            estado = "ACTIVO / RESPONDE"
        else:
            estado = "SIN RESPUESTA"

        datos = f"""
AUDITORÍA DE RED
========================

Equipo: {socket.gethostname()}
IP local: {obtener_ip_local()}
Objetivo: {objetivo}
Estado: {estado}
"""

        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, datos)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def generar_qr():
    texto = resultado.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning(
            "Aviso",
            "Primero realiza una auditoría"
        )
        return

    archivo = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Imagen PNG", "*.png")]
    )

    if not archivo:
        return

    qr = qrcode.make(texto)
    qr.save(archivo)

    messagebox.showinfo(
        "QR generado",
        f"QR guardado correctamente:\n{archivo}"
    )


def guardar_reporte():
    texto = resultado.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning(
            "Aviso",
            "No existe ningún informe"
        )
        return

    archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivo de texto", "*.txt")]
    )

    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(texto)

        messagebox.showinfo(
            "Reporte",
            "Reporte guardado correctamente"
        )


ventana = tk.Tk()
ventana.title("Auditor de Red + QR")
ventana.geometry("700x550")
ventana.configure(bg="#252525")

titulo = tk.Label(
    ventana,
    text="AUDITOR DE RED + QR",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#252525"
)

titulo.pack(pady=20)

frame = tk.Frame(
    ventana,
    bg="#252525"
)

frame.pack()

entrada_ip = tk.Entry(
    frame,
    font=("Arial", 13),
    width=30
)

entrada_ip.grid(
    row=0,
    column=0,
    padx=5,
    pady=10
)

btn_ping = tk.Button(
    frame,
    text="Comprobar",
    command=comprobar_conexion,
    bg="#1976D2",
    fg="white",
    width=15
)

btn_ping.grid(
    row=0,
    column=1,
    padx=5
)

btn_datos = tk.Button(
    ventana,
    text="Obtener datos del equipo",
    command=obtener_datos,
    bg="#388E3C",
    fg="white",
    width=30
)

btn_datos.pack(pady=10)

resultado = tk.Text(
    ventana,
    height=15,
    width=70,
    font=("Consolas", 11)
)

resultado.pack(pady=10)

frame_botones = tk.Frame(
    ventana,
    bg="#252525"
)

frame_botones.pack(pady=10)

btn_qr = tk.Button(
    frame_botones,
    text="Generar QR",
    command=generar_qr,
    bg="#F57C00",
    fg="white",
    width=18
)

btn_qr.grid(
    row=0,
    column=0,
    padx=10
)

btn_guardar = tk.Button(
    frame_botones,
    text="Guardar reporte",
    command=guardar_reporte,
    bg="#616161",
    fg="white",
    width=18
)

btn_guardar.grid(
    row=0,
    column=1,
    padx=10
)

ventana.mainloop()

