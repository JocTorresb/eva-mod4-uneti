Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 

import socket

# Definir el host y el rango de puertos
host = 'localhost'
puertos = range(1, 1025)

# Iterar a través de los puertos y escanearlos
for puerto in puertos:
    try:
        # Crear un objeto de socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establecer un tiempo de espera de conexión de 1 segundo
        sock.settimeout(1)
        # Conectar el socket al host y al puerto
        resultado = sock.connect_ex((host, puerto))
        # Comprobar si el puerto está abierto
        if resultado == 0:
            print(f"El puerto {puerto} está abierto")
        # Cerrar el socket
        sock.close()
    # Manejar excepciones de conexión
    except socket.error as error:
        print(f"Error de conexión: {error}")
