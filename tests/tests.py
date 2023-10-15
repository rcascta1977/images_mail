import unittest
import os

from src.ImagenesMail_rcanessa.images import showImageFromURL, downloadImageFromUrl, grayScaleImage
from src.ImagenesMail_rcanessa.mymail import sendQuickMail,sendAttachEmail

#Pruebas unitarias para las funciones de manejo de imágenes
class Testimages(unittest.TestCase):
       
    def test_verificar_imagen(self):

        url="https://www.tecnicasdetrading.com/wp-content/uploads/2023/10/tipos-triangulos-expansivos.png"

        resultado=showImageFromURL(url)
        self.assertTrue(resultado==None)

    def test_descargar_imagen(self):

        url="https://www.tecnicasdetrading.com/wp-content/uploads/2023/10/tipos-triangulos-expansivos.png"
        path="prueba.jpg"

        downloadImageFromUrl(url,path)
        self.assertTrue(os.path.exists(path))
    
    def test_escala_grises(self):
        url="https://www.tecnicasdetrading.com/wp-content/uploads/2023/10/tipos-triangulos-expansivos.png"
        path="prueba.jpg"

        grayScaleImage(url,path)
        self.assertTrue(os.path.exists(path))
    
    def teerDown(self):
        path="prueba.jpg"
        if os.path.exists(path):
            os.remove(path)

#Pruebas unitarias para las funciones de envío de correos
class TestMails(unittest.TestCase):

    def test_envio_correo(self):
        subject="Correo de prueba"
        message="Este es un correo para una prueba unitaria de funcion"
        destination="rcanessa@gmail.com"

        resultado=sendQuickMail(subject,message,destination)
        self.assertTrue(resultado==None)

    def test_envio_correo_adjunto(self):
        subject="Correo de prueba"
        message="Este es un correo para una prueba unitaria de funcion"
        destination="rcanessa@gmail.com"
        path="adjunto.png"

        resultado=sendAttachEmail(subject,message,destination,path)
        self.assertTrue(resultado==None)
       

if __name__ == "__main__":
    unittest.main()
