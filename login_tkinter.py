import tkinter as tk
from tkinter import messagebox

def validar_login():
    usuario = entry_usuario.get()
    password = entry_password.get()

    if usuario == "root" and password == "admin":
        messagebox.showinfo("Resultado", "Valores correctos")
    else:
        messagebox.showerror("Resultado", "Valores incorrectos")

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("550x380")      # Ventana más grande
ventana.configure(bg="#3b3b3b")
ventana.resizable(False, False)

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

frame = tk.Frame(
    ventana,
    bg="#4a4a4a",
    padx=50,
    pady=40,
    relief="ridge",
    bd=4
)

frame.grid(row=0, column=0)

titulo = tk.Label(
    frame,
    text="LOGIN",
    font=("Arial", 20, "bold"),
    bg="#4a4a4a",
    fg="white"
)

titulo.grid(row=0, column=0, columnspan=2, pady=(0, 30))
lbl_usuario = tk.Label(
    frame,
    text="Usuario:",
    font=("Arial", 12),
    bg="#4a4a4a",
    fg="white"
)

lbl_usuario.grid(row=1, column=0, sticky="e", padx=10, pady=10)

entry_usuario = tk.Entry(
    frame,
    width=20,            
    font=("Arial", 12)
)

entry_usuario.grid(row=1, column=1, padx=10, pady=10)

lbl_password = tk.Label(
    frame,
    text="Password:",
    font=("Arial", 12),
    bg="#4a4a4a",
    fg="white"
)

lbl_password.grid(row=2, column=0, sticky="e", padx=10, pady=10)

entry_password = tk.Entry(
    frame,
    width=20,            
    font=("Arial", 12),
    show="*"
)

entry_password.grid(row=2, column=1, padx=10, pady=10)
frame_botones = tk.Frame(frame, bg="#4a4a4a")
frame_botones.grid(row=3, column=0, columnspan=2, pady=30)

btn_enviar = tk.Button(
    frame_botones,
    text="Enviar",
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12,
    command=validar_login
)

btn_enviar.grid(row=0, column=0, padx=10)

btn_salir = tk.Button(
    frame_botones,
    text="Salir",
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12,
    command=ventana.destroy
)

btn_salir.grid(row=0, column=1, padx=10)


ventana.bind("<Return>", lambda event: validar_login())

ventana.mainloop()