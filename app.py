import qrcode
from io import BytesIO
from PIL import Image
from flask import Response, Flask, render_template, request, url_for, redirect
from conexiones import app, db
from modelo import Personas

@app.route("/vista6")
def comprobante():
    return render_template("vista6.html")

def qr_generator(data):
    # Generar un código QR en la memoria
    qr = qrcode.QRCode(version=7, error_correction= qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="darkgreen", back_color="lightgreen").convert("RGB")
    img_bytes_io = BytesIO()
    img.save(img_bytes_io, format="PNG")
    return img_bytes_io.getvalue()

    # # Leer la imagen desde BytesIO y mostrar
    # img_bytes_io.seek(0)
    # image = Image.open(img_bytes_io)
    # image.show()


@app.route("/generar_QR")
def generar_html_conqr(data):
    imagen_qr = qr_generator(data)
    ip = "192.168.1.34"
    data = "www.youtube.com"
    return Response(imagen_qr, content_type="imagen/png")


#creacion de ruta principal

# CRUD - create, read, update, delete. Hay que podes lograr todo eso con nuestra base de datos. 

@app.route("/cargar_datos", methods = ["GET", "POST"])
def cargar_datos():
    # Si el metodo es POST obtenemos los datos "nombre", etc etc...
    if request.method == "POST":
        cedula = request.form["cedula"]
        punto = request.form["punto"]

        datos_personas = Personas(cedula, punto)

        #POST envia los datos 

        db.session.add(datos_personas)
        db.session.commit()

        return render_template("cargar_datos.html")
    return render_template("cargar_datos.html")
