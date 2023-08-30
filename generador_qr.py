import qrcode as qrlib

def qr_generator(url):
    print("ejecutando generardor")
    try:
        qrcode = qrlib.QRCode(
            version = 7,
            error_correction = qrlib.constants.ERROR_CORRECT_H,
            box_size = 5,
            border = 1,
            
        )
        
        qrcode.add.data(url)
        
        qrcode.make(fit=True)
        
        
        qrcolor = 'Black'
        
        qrimg = qrcode.make_image(fill_color=qrcolor, back_color='white').convert('RGB')
        
        
        qr_path = "./static/qr_xd.png"
        qrimg.save(qr_path)
        
        
        return qr_path
    
    except Exception as e:
        print("Error al generar el codigo QR:", str(e))
        return None