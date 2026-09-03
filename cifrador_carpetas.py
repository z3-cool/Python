
import os
import sys
import base64
import getpass
import shutil

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken

SALT_FILENAME = ".cifrado_salt"  
MARKER_SUFFIX = ".enc"           
ITERATIONS = 200_000


def derivar_clave(password: str, salt: bytes) -> bytes:
   
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    clave = kdf.derive(password.encode("utf-8"))
    return base64.urlsafe_b64encode(clave)


def listar_archivos(carpeta: str):
    
    rutas = []
    for raiz, _dirs, archivos in os.walk(carpeta):
        for nombre in archivos:
            ruta = os.path.join(raiz, nombre)
            if os.path.basename(ruta) == SALT_FILENAME:
                continue
            rutas.append(ruta)
    return rutas


def cifrar_carpeta(carpeta: str, password: str):
    if not os.path.isdir(carpeta):
        print(f"La carpeta no existe: {carpeta}")
        return

    salt_path = os.path.join(carpeta, SALT_FILENAME)
    if os.path.exists(salt_path):
        print("Esta carpeta ya parece estar cifrada")
        return

    salt = os.urandom(16)
    clave = derivar_clave(password, salt)
    fernet = Fernet(clave)

    archivos = listar_archivos(carpeta)
    if not archivos:
        print("La carpeta está vacía, no hay nada que cifrar.")
        return

    print(f"Cifrando {len(archivos)} archivos...")
    for ruta in archivos:
        with open(ruta, "rb") as f:
            datos = f.read()
        datos_cifrados = fernet.encrypt(datos)

        ruta_cifrada = ruta + MARKER_SUFFIX
        with open(ruta_cifrada, "wb") as f:
            f.write(datos_cifrados)

        os.remove(ruta)
        print(f"{os.path.relpath(ruta, carpeta)}")

    with open(salt_path, "wb") as f:
        f.write(salt)

    print(f"\nCarpeta cifrada correctamente: {carpeta}")
    print(" Guardá bien tu contraseña: sin ella los archivos NO se pueden recuperar.")


def descifrar_carpeta(carpeta: str, password: str):
    if not os.path.isdir(carpeta):
        print(f"La carpeta no existe: {carpeta}")
        return

    salt_path = os.path.join(carpeta, SALT_FILENAME)
    if not os.path.exists(salt_path):
        print("No se encontró el archivo de salt. ¿La carpeta está realmente cifrada?")
        return

    with open(salt_path, "rb") as f:
        salt = f.read()

    clave = derivar_clave(password, salt)
    fernet = Fernet(clave)

    archivos = [r for r in listar_archivos(carpeta) if r.endswith(MARKER_SUFFIX)]
    if not archivos:
        print("No se encontraron archivos cifrados (.enc) en la carpeta.")
        return

    print(f"Descifrando {len(archivos)} archivos...")
    errores = 0
    for ruta in archivos:
        with open(ruta, "rb") as f:
            datos_cifrados = f.read()
        try:
            datos = fernet.decrypt(datos_cifrados)
        except InvalidToken:
            print(f"Contraseña incorrecta o archivo dañado: {os.path.relpath(ruta, carpeta)}")
            errores += 1
            continue

        ruta_original = ruta[: -len(MARKER_SUFFIX)]
        with open(ruta_original, "wb") as f:
            f.write(datos)

        os.remove(ruta)
        print(f"{os.path.relpath(ruta_original, carpeta)}")

    if errores == 0:
        os.remove(salt_path)
        print(f"\nCarpeta descifrada correctamente: {carpeta}")
    else:
        print(f"\nSe completó con {errores} error. Revisá la contraseña.")


def pedir_password(confirmar: bool = False) -> str:
    password = getpass.getpass("Contraseña: ")
    if confirmar:
        password2 = getpass.getpass("Confirmá la contraseña: ")
        if password != password2:
            print("Las contraseñas no coinciden.")
            sys.exit(1)
    if not password:
        print("La contraseña no puede estar vacía.")
        sys.exit(1)
    return password


def main():
    if shutil.which is None:
        pass  

    if len(sys.argv) >= 3:
        accion = sys.argv[1].lower()
        carpeta = sys.argv[2]
    else:
        print("=== Cifrador de Carpetas ===")
        accion = input("¿Qué querés hacer? (cifrar/descifrar): ").strip().lower()
        carpeta = input("Ruta de la carpeta: ").strip().strip('"')

    if accion in ("cifrar", "encrypt"):
        password = pedir_password(confirmar=True)
        cifrar_carpeta(carpeta, password)
    elif accion in ("descifrar", "decrypt"):
        password = pedir_password(confirmar=False)
        descifrar_carpeta(carpeta, password)
    else:
        print(f"Acción no reconocida: {accion}. Usá 'cifrar' o 'descifrar'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
