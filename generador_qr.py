import qrcode as qrlib

def qr_generator(url):
    print("Generando QR...")
    # Crea un objeto QRCode con las configuraciones deseadas
    try:
        qrcode = qrlib.QRCode(
            version=7,  # Versión del QR (1-40). Aumentar para admitir más datos.
            error_correction=qrlib.constants.ERROR_CORRECT_H,  # Nivel de corrección de errores (L, M, Q, H).
            box_size=10,  # Tamaño de cada caja en el QR.
            border=1,  # Tamaño del borde.
        )
        # Generamos la ruta a la que nuestro código QR va a redireccionar
        qrcode.add_data(url)

        # Genera el código QR con el ajuste fit=True para que se adapte automáticamente al tamaño de los datos
        qrcode.make(fit=True)

        # Pasamos los parámetros de color que tendrá nuestro QR
        qrcolor = 'Black'

        # Crea una imagen PIL (Pillow) del código QR con los colores especificados
        qrimg = qrcode.make_image(fill_color=qrcolor, back_color="green")

        # Guarda el código QR generado en un objeto BytesIO para su posterior uso
        qr_path = "./static/qr_xd.png"
        qrimg.save(qr_path)
        print("Codigo QR generado con exito")

        # Devolvemos los bytes de la imagen como respuesta
        return qr_path
    except Exception as e:
        print("Error al generar el código QR:", str(e))
        return None