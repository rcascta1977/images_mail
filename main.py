import sys
import threading
from src.images import showImageFromURL, downloadImageFromUrl, grayScaleImage
from src.mymail import sendQuickMail,sendAttachEmail
from src.mensajes import Saludo,Menu,Despedida,Mensaje_descarga
from src.funcionesutiles import borrar_pantalla

def main(args):
    if "--i" in args:
        borrar_pantalla()
        print(Saludo)
        input("Presione la tecla Enter para continuar")
    
    print(Menu)

    ciclos=False
    while ciclos==False:
       print(Menu)
       opcion=input("Escriba el número de la tarea que quiere realizar: ")

       if opcion not in ["1","2","3","4","5","6"]:
          print("Seleccionó la opción equivocada")
          print("Debe escribir un número entre 1 y 6")
          break
    
    #Código para descargar y ver la imagen de una URL determinada
       if opcion=="1":
          url=input("Ingrese la URL de la imagen que desea ver: ")
          print(Mensaje_descarga)
          showImageFromURL(url)
          borrar_pantalla()
    
    #Código para descargar y ver la imagen de una URL determinada y guardarla en una ruta escogida por el usuario
       if opcion=="2":
          url=input("Ingrese la URL de la imagen que desea ver: ")
          ruta=input("Ingrese la ruta donde desea guardar la imagen: ")
          nombre=input("Indique el nombre con que desea guardar el archivo: ")
          path=ruta+"\\"+nombre+".png"
          print(Mensaje_descarga)
          downloadImageFromUrl(url,path)
          borrar_pantalla()
   
   #Código para convertir una imagen a blanco y negro
       if opcion=="3":
         url=input("Ingrese la URL de la imagen que desea ver: ")
         ruta=input("Ingrese la ruta donde desea guardar la imagen: ")
         nombre=input("Indique el nombre con que desea guardar el archivo: ")
         path=ruta+"\\"+nombre+".png"
         print(Mensaje_descarga)
         grayScaleImage(url,path)
         borrar_pantalla()
       
    #Código para enviar un mensaje corto por correo electrónico
       if opcion=="4":
          subject=input("Indique el tema del mensaje: ")
          message=input("Escriba el mensaje del correo: ")
          destination=input("Indique el correo de destino: ")
          print("Ahora comenzará el envío del correo")
         
          hilo1=threading.Thread(target=sendQuickMail, args=(subject,message,destination))
          hilo1.start()
          hilo1.join()

    #Código para enviar un mensaje por correo electrónico con un archivo adjunto
       if opcion=="5":
          subject=input("Indique el tema del mensaje: ")
          message=input("Escriba el mensaje del correo: ")
          destination=input("Indique el correo de destino: ")
          url=input("Indique la ruta del archivo que quiere adjuntar: ")
          print("Ahora comenzará el envío del correo")

          hilo2=threading.Thread(target=sendAttachEmail, args=(subject,message,destination,url))
          hilo2.start()
          hilo2.join()

       if opcion=="6":
          print(Despedida)
          ciclos=True

if __name__=="__main__":
    main(sys.argv)

