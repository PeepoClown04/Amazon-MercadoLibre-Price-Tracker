import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os

# Agregamos la ruta raíz para poder importar config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    import config
except ImportError:
    print("⚠️ ADVERTENCIA: No se encontró config.py. Las alertas por correo no funcionarán.")
    config = None

def send_email_alert(product_name, price, url):
    if not config:
        return

    print(f"📧 Enviando alerta por correo para: {product_name}...")

    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_SENDER
    msg['To'] = config.EMAIL_RECEIVER
    msg['Subject'] = f"🚨 BAJADA DE PRECIO: ${price:,.0f} - {product_name[:30]}..."

    body = f"""
    ¡BUENAS NOTICIAS!
    
    El producto que rastreas ha bajado de precio.
    
    📦 Producto: {product_name}
    💰 Precio Actual: ${price:,.0f}
    🔗 Link: {url}
    
    Corre a comprarlo antes de que se agote.
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(config.EMAIL_SENDER, config.EMAIL_RECEIVER, text)
        server.quit()
        print("✅ ¡Correo enviado con éxito!")
    except Exception as e:
        print(f"❌ Error enviando correo: {e}")