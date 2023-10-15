import sys
from src.ImagenesMail_rcanessa.images import showImageFromURL, downloadImageFromUrl, grayScaleImage
from src.ImagenesMail_rcanessa.mymail import sendQuickMail,sendAttachEmail

def main(args):
    if "--i" in args:
        input("Presione la tecla Enter para continuar")
    #Esta función es para hacer pruebas de la biblioteca images.py.
    
    url="https://www.tecnicasdetrading.com/wp-content/uploads/2023/10/tipos-triangulos-expansivos.png"
    path="prueba.jpg"

    showImageFromURL(url)
    downloadImageFromUrl(url,path)
    grayScaleImage(url,path)

    #Esta función es para hacer pruebas de la biblioteca mymail.py
    subject="Correo de prueba"
    message="Este es un correo para una prueba de la funcion"
    destination="rcanessa@gmail.com"
    path="adjunto.png"

    sendQuickMail(subject,message,destination)
    sendAttachEmail(subject,message,destination,path)


if __name__=="__main__":
    main(sys.argv)
