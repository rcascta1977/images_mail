from PIL import Image,ImageOps
import requests

def showImageFromURL(url:str)-> None:
    """
    Descarga una imagen desde una URL y la muestra

    Arguments
    url(str): Es la dirección de la imagen que se desea descargar y visualizar.
    
    Returns: 
    None
    """
    archivo_imagen=requests.get(url,stream=True)
    with Image.open(archivo_imagen.raw) as imagen:
        imagen.show()

def downloadImageFromUrl(url:str, path:str)-> None:
    """
    Descarga una imagen y la guarda en la ruta indicada

    Arguments:

    url(str): Es la dirección de la imagen que se desea descargar y visualizar.
    path(str): Indica la ruta donde se va a descargar la imagen.
    
    return
    None
    """
    archivo_imagen=requests.get(url,stream=True)
    with Image.open(archivo_imagen.raw) as imagen:
        imagen.show()

    imagen.save(path)
    imagen.show(path)

def grayScaleImage(url:str,path:str):
    """
    Convierte una imagen a blanco y negro

    Arguments:

    url(str): Es la dirección de la imagen que se desea descargar y visualizar.
    path(str): Indica la ruta donde se va a descargar la imagen.
    
    Returns
    None
    """
    archivo_imagen=requests.get(url,stream=True)
    with Image.open(archivo_imagen.raw) as imagen:
        imagen_grises=ImageOps.grayscale(imagen)
        imagen_grises.show(path)
        imagen_grises.save(path)
