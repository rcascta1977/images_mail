# ImagenesMail

Hola a todos, bienvenidos a mi biblioteca de Python.

Esta biblioteca permite descargar y visualizar imágenes de una url. Las imágenes pueden ser guardadas o convertidas a escala de grises.

También permite enviar mensajes por correo electrónico con o sin archivos adjuntos.

<b>Lenguaje:</b> Python 100%

## Instalación
Esta sección muestra como instalar el paquete ImagenesMail.

Para instalar el paquete el usuario necesita crear un entorno virtual:

```terminal
python -m venv env
ImagenesMail\Scripts\activate
pip install -r python venv venv
```

Para usarlo solo debe importar las funciones al inicio del módulo:

```python
from src.ImagenesMail_rcanessa.images import showImageFromURL, downloadImageFromUrl, grayScaleImage
from src.ImagenesMail_rcanessa.mymail import sendQuickMail,sendAttachEmail
```
## Usos del paquete
La descarga y visualización de imágenes y envío de correos electrónicos
con este paquete se explica a continuación.

### Funciones de manejo de imágenes
Para descargar y visualizar una imagen de una url se debería llamar a 
las funciones de la siguiente forma:

#### Para descargar y ver una imagen
```python
from src.ImagenesMail_rcanessa.images import showImageFromURL

url_imagen="https://www.tecnicasdetrading.com/wp-content/uploads/2023/10/tipos-triangulos-expansivos.png"

showImageFromURL(url_imagen)
```
#### Para descargar imagen y guardarla en ruta indicada

```python
from src.ImagenesMail_rcanessa.images import downloadImageFromURL

url_imagen="https://www.tecnicasdetrading.com/wp-content/uploads/2023/10/tipos-triangulos-expansivos.png"

path="C:\Users\Desktop\Desktop\imagen.jpg"

downloadImageFromUrl(url_imagen, path)

```
#### Para convertir una imagen a escala de grises

```python

from src.ImagenesMail_rcanessa.images import grayScaleImage

url_imagen="https://www.tecnicasdetrading.com/wp-content/uploads/2023/10/tipos-triangulos-expansivos.png"

path="C:\Users\Desktop\Desktop\imagen.jpg"

grayScaleImage(url_imagen, path)

```
### Funciones de envío de correos

Para enviar un correo electrónico con o sin archivo adjunto las funciones se usan como se muestra a continuación.

#### Envío de mensajes sin archivos adjuntos
```python
from src.ImagenesMail_rcanessa.images import sendQuickMail

subject="Correo de prueba"

message="Saludos desde Python"

destination="correodestino@correo.com"

sendQuickMail(subject, message, destination)

```
#### Envío de mensajes con archivos adjuntos
```python
from src.ImagenesMail_rcanessa.images import sendAttachEmail

subject="Correo de prueba"

message="Saludos desde Python"

destination="correodestino@correo.com"

path="Ruta del archivo a cargar"

sendAttachEmail(subject, message, destination, path)

```

## Referencias
Para ver el código fuente diríjase al repositorio en: [Github](https://github.com/rcascta1977/images_mail.git)

## Imagen de prueba
![Imagen de prueba](https://www.tecnicasdetrading.com/wp-content/uploads/2023/05/patron-rectangulo-alcista.png)







