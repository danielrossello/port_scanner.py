import socket

# Alvo do scan
host = "192.168.0.1"

# Lista de portas que serão testadas
ports = [21, 22, 23, 80, 443, 3306]

# Loop para verificar cada porta
for port in ports:
    s = socket.socket()           # Cria o socket
    s.settimeout(1)               # Define timeout para evitar travamentos

    try:
        s.connect((host, port))   # Tenta se conectar ao host e porta
        print(f"[+] Porta {port} aberta em {host}")
    except:
        print(f"[-] Porta {port} fechada")
    finally:
        s.close()                 # Fecha o socket