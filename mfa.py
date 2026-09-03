import secrets
import string
import getpass

def generar_password(longitud: int = 16) -> str:
    if longitud < 12:
        raise ValueError("La contraseña 12 caracteres")

    alfabeto = string.ascii_letters + string.digits + string.punctuation
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    password += [secrets.choice(alfabeto) for _ in range(longitud - len(password))]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def generar_token(digitos: int = 6) -> str:
    token = "".join(secrets.choice(string.digits) for _ in range(digitos))
    return token


def verificar_password(password_generada: str, intentos: int = 3) -> bool:
  
    for intento in range(1, intentos + 1):
        ingresada = getpass.getpass(f"Intento {intento}/{intentos} - Ingresá la contraseña: ")
        if ingresada == password_generada:
            return True
        print("Contraseña incorrecta.\n")
    return False


def verificar_token(token_generado: str, intentos: int = 3) -> bool:
   
    for intento in range(1, intentos + 1):
        ingresado = input(f"Intento {intento}/{intentos} - Ingresá el token de 6 dígitos: ").strip()
        if ingresado == token_generado:
            return True
        print("Token incorrecto.\n")
    return False


def main():
    print("=" * 55)
    print("### SISTEMA DE AUTENTICACIÓN ### ")
    print("=" * 55)
    password = generar_password(16)
    print("\nSe generó una contraseña aleatoria.")
    print(f"   Contraseña: {password}\n")

    if not verificar_password(password):
        print("\nACCESO DENEGADO")
        return
    print("\nContraseña verificada correctamente.")
    token = generar_token(6)
    print("\nSe generó un token de acceso de 6 dígitos.")
    print(f"   Token: {token}\n")

    if verificar_token(token):
        print("\nACCESO AUTORIZADO")
    else:
        print("\nACCESO DENEGADO")


if __name__ == "__main__":
    main()