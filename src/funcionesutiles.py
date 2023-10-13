import sys

#Función para borrar la pantalla 
import os

def borrar_pantalla():
#Con os.name preguntamos que tipo de sistema tiene la computadora, Windows o Mac/Linux
#Dependiendo de la respuesta, usamos cls o clear para limpiar la pantalla
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")