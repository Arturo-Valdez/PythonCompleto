#USAR PROTOCOLO SMTP
#RECOMENDACION SENDGRID
#https://myaccount.google.com/u/2/lesssecureapps

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


plantilla = Path("11-paquetes-nativos/07-plantilla.html").read_text("utf-8")#DIRECCION DE PLANTILLA HTML
template = Template(plantilla)#CLASE DE PLANTILLAS
# cuerpo = template.substitute({"usuario": "Santiago Feliz"})
cuerpo = template.substitute(usuario = "Santiago triste")#SUSTITUTO DE USUARIO

path = Path("11-paquetes-nativos/descarga.jpeg")#DIRECCION DE IMAGEN
mime_image = MIMEImage(path.read_bytes())#DIRECCION TRADUCIDA EN LECTURA BYTES OBLIGATORIO
mensaje = MIMEMultipart()#CLASE DE CUERPO DEL CORREO EMAIL
mensaje["from"] = "Hola mundo"#NOMBRE DE PRESENTACION
mensaje["to"] = "enviar2@gmail.com"#CORREO AL QUE SE ENVIARA
mensaje["subject"] = "Esta es una prueba"#TITULO DE CORREO
cuerpo = MIMEText(cuerpo, "html")#CUERPO DE CORREO

mensaje.attach(cuerpo)#ANEXAR EN ATTACH TEXTO
mensaje.attach(mime_image)#ANEXAR EN ATTACH IMAGEN

#  La función smtplib.SMTP() se utiliza para crear una conexión con el servidor SMTP de Gmail.
#  host="smtp.gmail.com": Especifica el servidor SMTP de Gmail.
#  port=587: Especifica el puerto a usar para la conexión. El puerto 587 es comúnmente utilizado para conexiones seguras (con STARTTLS).

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # El método ehlo() se usa para identificar el cliente (el script Python) ante el servidor SMTP. Si la conexión se realiza correctamente, el servidor responderá con un saludo
    smtp.ehlo()
    # starttls() inicia una capa de seguridad (TLS) sobre la conexión SMTP, lo que cifra la comunicación entre el cliente y el servidor para proteger la información enviada (como las credenciales de login).
    smtp.starttls()

    smtp.login("enviar2@gmail.com", "password")
    smtp.send_message(mensaje)
    print("Mesaje enviado!")