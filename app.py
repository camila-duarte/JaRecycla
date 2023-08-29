from flask import render_template, request, url_for, redirect
from conexiones import app, db
from modelo import Personas
from generador_qr import qr_generator



#creacion de ruta principal

# CRUD - create, read, update, delete. Hay que podes lograr todo eso con nuestra base de datos. 

@app.route("/cargar_datos", methods = ["GET", "POST"])
def cargar_datos():
    # Si el metodo es POST obtenemos los datos "nombre", etc etc...
    if request.method == "POST":
        cedula = request.form["cedula"]

        datos_personas = Personas(cedula)

        #POST envia los datos 

        db.session.add(datos_personas)
        db.session.commit()

        return render_template("vista2.html")
    return render_template("cargar_datos.html")

@app.route("/vista2")
def vista2():
    return render_template("vista2.html")

@app.route("/sumar_puntos/", methods=["GET", "POST"])
def sumar_puntos():
    cantidad = int(request.form["cantidad"])
    
    punto = cantidad
    
    cedula = int(request.form["cedula"])
    usuario = Personas.query.filter_by(cedula=cedula).first()
    if usuario:
        usuario.sumar_pts(punto)
        db.session.commit()
        
        return redirect(url_for("vista4"))
    else:
        return "Usuario no encontrado"


@app.route("/generar_qr/<int:usuario_id>", methods=["GET"])
def generar_qr(usuario_id):
    usuario = Personas.query.get(usuario_id)
    
    if usuario:
        punto = usuario.punto
        url = f"/visualizar_qr/{usuario_id}/punto/{punto}"
        qr_image = qr_generator(url)
        
        
        return render_template("vista5.html", qr_image_url = url_for("static", filename="qr_xd.png"))
    else:
        return "Usuario no encontrado"
