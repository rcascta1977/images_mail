
#Estas bibliotecas permiten hacer la conexión al servidor y el correo usado para el envío
import ssl
import smtplib
#Estas bibliotecas permiten construir el mensaje del correo por partes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mimetypes import MimeTypes

def sendQuickMail(subject:str, message:str, destination:str) -> None:
    """
    Envía un correo electrónico rápido al destino indicado.
    @param subject: El tema del mensaje.
    @param message: El mensaje que será enviado en el correo.
    @param destination: El correo electrónico de destino del mensaje.
    returns: None
    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com
    """
    correo_envio=input("Indique el correo que usará para el envío del mensaje: ")
    password=input("Indique la clave de acceso a la app de su correo: ")

    mensaje = MIMEMultipart("mixed")
    mensaje["Subject"] = subject
    mensaje["From"] = correo_envio
    mensaje["To"] = destination
    mensaje["Cc"] = "jazminmonge@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
       conexion.ehlo()
       conexion.starttls(context=context)
       conexion.ehlo()
       conexion.login(correo_envio, password)
       respuesta=conexion.sendmail(correo_envio, destination, message)
   
    print(respuesta)

def sendAttachEmail(subject:str, message:str, destination:str, path:str)-> None:
    """
    Envía un correo electrónico con un archivo adjunto a la dirección indicada
    @param subject: El tema del mensaje.
    @param message: El mensaje que será enviado en el correo.
    @param destination: El correo electrónico de destino del mensaje.
    @param path: La ruta del archivo que se va a adjuntar.
    returns: None

    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com
    """
    correo_envio=input("Indique el correo que usará para el envío del mensaje: ")
    password=input("Indique la clave de acceso a la app de su correo: ")

    mensaje = MIMEMultipart()
    mensaje["Subject"] = subject
    mensaje["From"] = correo_envio
    mensaje["To"] = destination
    mensaje["Cc"] = "rcanessaccr@yahoo.com"

    contenido_mensaje=MIMEText(message,"html")
    
    mime=MimeTypes()
    tipo_archivo=mime.guess_type(path)
    if tipo_archivo[0]!=None:
        tipos=tipo_archivo[0].split("/") 
        tipo=tipos[0]
        subtipo=tipos[1]
    else:
        tipo, subtipo="application", "octet-stream"
        
    adjunto=MIMEBase(tipo, subtipo)
    with open(path,mode="rb") as attachment:
        adjunto.set_payload(attachment.read())
    
    encoders.encode_base64(adjunto)
    adjunto.add_header("Content-Disposition",
                       f"attachment; filename={path}")
    
    mensaje.attach(contenido_mensaje)
    mensaje.attach(adjunto)

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
       conexion.ehlo()
       conexion.starttls(context=context)
       conexion.ehlo()
       conexion.login(correo_envio, password)
       respuesta=conexion.sendmail(correo_envio, destination, mensaje.as_string())
    print(respuesta)

