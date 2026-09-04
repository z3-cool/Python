# programa que escanea los puertos abiertos 
# escanea si el sistema operativo esta actualizado
# realizado en un entorno virtualizado 

import socket
import subprocess
import platform

HOST="127.0.0.1"
PUERTOS = {
    21:"FTP",22:"SSH",23:"TELNET",25:"SMTP",
    53:"DNS",80:"HTTP",135:"RPC",139:"NetBIOS",
    443:"HTTPS",445:"SMB",3306:"MySQL",
    3389:"RDP",5432:"PostgreSQL",5900:"VNC",
    8080:"HTTP-ALT"
}

def firewall():
    cmd=[
        "powershell","-Command",
        "Get-NetFirewallProfile | Select Name,Enabled"
    ]
    r = subprocess.run(cmd,capture_output=True, text=True)
    print("\n---FIREWALL---")
    print(r.stdout)
    return "False" not in r.stdout

def escanear():
    print("\n---PUERTOS ABIERTOS---")
    abiertos = []
    for puerto, servicio in PUERTOS.items():
        s = socket.socket()
        s.settimeout(0.3)

        if s.connect_ex((HOST, puerto))== 0:
            abiertos.append(puerto)
            print(f'[ABIERTO] {puerto}-{servicio}')
        s.close()
    if not abiertos:
        print("no se encontraron puertos abiertos")
    return abiertos

def main():
    print("=" * 50)
    print("--- AUDITORIA DE SEGURIDAD ---")
    print("=" * 50)
    print(f'\nSistema: {platform.system()}')
    print(f'\nVersion: {platform.release()}')
    print(f'\nEquipo: {socket.gethostname()}')
    fw = firewall()
    puertos = escanear()

    print('\n---RESULTADO ---')
    if fw:
        print("Firewall: ACTIVO")
    else:
        print("Firewall: Inactivo")

    if puertos:
        print(f'puertos abiertos encontrados: {len(puertos)}')
    else:
        print(f'no se encontraron puertos abiertos ')
    if not fw:
        print('\nRECOMENDACION:')
        print("actualiza windows defender")
    if 445 in puertos:
        print("SMB(445) Revisa que no este expuesto")
    if 3389 in puertos:
        print("RDP (3389) rESTRINGE EL ACCESO")
    print('\nAUDITORIA FINALIZADA...')

if __name__ == "__main__":
    main()
    


