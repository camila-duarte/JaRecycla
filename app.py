from flask import render_template, request, url_for, redirect
from conexiones import app, db
from modelo import Personas
from generador_qr import qr_generator



#creacion de ruta principal

# CRUD - create, read, update, delete. Hay que podes lograr todo eso con nuestra base de datos. 

@app.route("/vista1", methods = ["GET", "POST"])
def vista1():
    if request.method == "POST":
        cedula = request.form["cedula"]

        datos_personas = Personas(cedula)

        #POST envia los datos 

        db.session.add(datos_personas)
        db.session.commit()
        print("Ingreso kp", datos_personas.cedula)
        print(" usuario creado")
        return render_template("vista2.html",cedula=cedula)
    
    return render_template("vista1.html")

@app.route("/vista2/<int:cedula>")
def vista2(cedula):
        return render_template("vista2.html", cedula=cedula)


@app.route("/vista3/<int:cedula>")
def vista3(cedula):
    return render_template("vista3.html", cedula = cedula)

@app.route("/vista4/<int:cedula>")
def vista4(cedula):
    return render_template("vista4.html",cedula=cedula)

@app.route("/vista5")
def vista5():
    return render_template("vista5.html")

@app.route("/banner/<int:id>")
def banner (id):
    usuario = Personas.query.get(id)
    return (f"Total de puntos {usuario.punto}")

@app.route("/sumar_puntos/", methods=["GET", "POST"])
def sumar_puntos():
    cantidad = int(request.form["cantidad"])
    
    punto = cantidad
    
    cedula = int(request.form["cedula"])
    usuario = Personas.query.filter_by(cedula=cedula).first()
    if usuario:
        usuario.sumar_pts(punto)
        db.session.commit()
        
        return redirect(url_for("vista4", cedula=cedula))
    else:
        return "Usuario no encontrado"


@app.route("/generar_qr/<int:cedula>", methods=["GET"])
def generar_qr(cedula):
    usuario = Personas.query.filter_by(cedula=cedula).first()
    
    if usuario:
        ip = "192.168.1.159"
        port = 8000
        url= f"http://{ip}:{port}/banner/{usuario.id}"
        qr_image =qr_generator(url)
        print(qr_image)
        
        return render_template("vista5.html", qr_image_url = url_for("static", filename="qr_xd.png"))
    else:
        return "Usuario no encontrado"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=8000)