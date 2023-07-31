import subprocess

#Integrantes:
#Jose Torres
#Yhoselyn Meza
#Carolina Lopes
#David Peralta

# Obtener versión del sistema operativo Windows
os_version = subprocess.check_output(["winver"]).decode("utf-8").strip()
print(f'Tu sistema operativo es: {os_version}')
#Imprimir versión del sistema operativo Windows