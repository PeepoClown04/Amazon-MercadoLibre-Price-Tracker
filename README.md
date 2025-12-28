# Amazon/MercadoLibre Price Tracker
![Status](https://img.shields.io/badge/Status-Completed-green)

Herramienta de automatización diseñada para monitorear fluctuaciones de precios en plataformas de comercio electrónico. Rastrea URLs específicas, extrae datos de precios en tiempo real y notifica al usuario cuando se detecta un descuento objetivo.

## Funcionalidades
- **Scraping Dinámico:** Extracción robusta de Título, Precio y Disponibilidad usando `Selenium` (con manejo de pop-ups y anti-bloqueo).
- **Sistema de Alertas:** Notificación automática vía correo electrónico (SMTP) cuando el precio cae por debajo del umbral definido.
- **Histórico de Datos:** Registro de precios en CSV para análisis de tendencias.
- **Modo Headless:** Ejecución en segundo plano sin interfaz gráfica.

## Stack Tecnológico
- Python 3.x
- Selenium WebDriver
- Pandas (Data Management)
- SMTP Library (Notificaciones)

## Instalación y Uso
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Crear archivo `config.py` (ver abajo).
4. Ejecutar: `python main.py`

### ⚙️ Configuración Segura
Este proyecto requiere un archivo `config.py` en la raíz (no incluido por seguridad).
Crea un archivo llamado `config.py` y agrega tus credenciales:

```python
EMAIL_SENDER = "tucorreo@gmail.com"
EMAIL_PASSWORD = "tu-contraseña-de-aplicacion"
EMAIL_RECEIVER = "destino@gmail.com"
