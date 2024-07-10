import streamlit as st
import qrcode

def generate_qr_code(data):
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Configurar la página web con Streamlit
st.title('Generador de Códigos QR')

# Campo para ingresar el número de código
codigo = st.text_input('Ingrese el número de código')

# Botón para generar el código QR
if st.button('Generar Código QR'):
    if codigo:
        # Generar el código QR
        qr_image = generate_qr_code(codigo)

        # Mostrar la imagen del código QR
        st.image(qr_image, caption=f'Código QR para el código: {codigo}', use_column_width=True)
    else:
        st.warning('Por favor ingrese un número de código')


