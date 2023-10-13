from PIL import Image,ImageOps
import requests

def showImageFromURL(url:str)-> None:
    """
    Descarga una imagen desde una URL y la muestra
    @param url: Es la dirección de la imagen que se desea descargar y visualizar.
    return: None
    """
    archivo_imagen=requests.get(url,stream=True)
    with Image.open(archivo_imagen.raw) as imagen:
        imagen.show()
        return(imagen)

def downloadImageFromUrl(url:str, path:str)-> None:
    """
    Descarga una imagen y la guarda en la ruta indicada
    @param url: Es la dirección de la imagen que se desea descargar y visualizar.
    @param path: Indica la ruta donde se va a descargar la imagen.
    return: None
    """
    archivo_imagen=requests.get(url,stream=True)
    with Image.open(archivo_imagen.raw) as imagen:
        imagen.show()

    imagen.save(path)
    imagen.show(path)

def grayScaleImage(url:str,path:str):
    """
    Convierte una imagen a blanco y negro
    @param url: Es la dirección de la imagen que se desea descargar y visualizar.
    @param path: Indica la ruta donde se va a descargar la imagen.
    return: None
    """
    archivo_imagen=requests.get(url,stream=True)
    with Image.open(archivo_imagen.raw) as imagen:
        imagen_grises=ImageOps.grayscale(imagen)
        imagen_grises.show(path)
        imagen_grises.save(path)
