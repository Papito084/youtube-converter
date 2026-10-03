# YouTube to MP3/MP4 Converter

Servicio backend RESTful desarrollado en Python (Flask) para la extracción, procesamiento y conversión de streams de video utilizando herramientas de línea de comandos del ecosistema FFmpeg.

## 🏗️ Arquitectura y Funcionamiento Interno
- **Arquitectura Cliente-Servidor:** 
  - El frontend se comunica con el framework Flask mediante peticiones HTTP POST asíncronas (Fetch API), enviando payloads en formato JSON.
  - El backend procesa las solicitudes, orquestando la descarga y emitiendo una respuesta con las rutas absolutas para el acceso al archivo resultante.
- **Motor de Extracción y Conversión:**
  - Se integra yt-dlp como módulo de resolución de URLs para desencriptar firmas de video y descargar flujos de máxima calidad.
  - Implementa un pipeline de transcodificación mediante fmpeg (gestionado por imageio-ffmpeg) que permite extraer pistas de audio o remultiplexar contenedores (MP4) sobre la marcha.
- **Gestión del Almacenamiento y Temporales:** Los archivos procesados se almacenan temporalmente en el volumen de sistema /downloads/. Se sanitizan los nombres de archivo mediante expresiones regulares para evitar vulnerabilidades de Path Traversal.

## 📂 Estructura del Proyecto
`plaintext
youtube-converter/
├── app.py                      # Router principal y Endpoints Flask
├── requirements.txt            # Manejo de dependencias de entorno
├── templates/
│   └── index.html              # Vistas HTML (Frontend)
├── static/                     # Archivos estáticos (CSS, JS modular, assets)
├── downloads/                  # Directorio de procesamiento (ignorado en Git)
├── Launch YouTube Converter.bat # Entry-point automatizado para Windows
└── README.md
`

## 🔌 Endpoints de la API

### POST /convert
Inicia el flujo de trabajo de resolución y conversión.
- **Request:** {"url": "https://youtube.com/watch?v=...", "format": "mp3"} (o mp4)
- **Response (200 OK):** {"message": "Conversion successful", "filename": "uuid-video.mp3", "title": "Video Title"}
- **Response (400/500):** Excepciones capturadas y propagadas con detalle del error.

### GET /download/<filename>
Expone el archivo estático procesado al cliente.
- **Response:** Binario del archivo transcodificado con cabeceras HTTP Content-Disposition: attachment.

## ⚙️ Configuración del Entorno
`ash
# 1. Crear entorno virtual aislado
python -m venv venv
venv\Scripts\activate  # o 'source venv/bin/activate' en sistemas UNIX

# 2. Instalar dependencias mediante PIP
pip install -r requirements.txt

# 3. Inicializar el servidor WSGI de desarrollo
python app.py
`
"@

 = @"
# HTML to PDF Converter

Herramienta profesional de renderizado en el navegador que convierte documentos web (HTML/CSS) en archivos PDF rasterizados, manteniendo la fidelidad visual, la inyección de estilos y el layout en formato estandarizado.

## 🏗️ Arquitectura y Funcionamiento Interno
- **Renderizado del DOM Virtual:** 
  - La aplicación hace uso de html2canvas para analizar recursivamente el árbol DOM (Document Object Model) y aplicar algoritmos de renderizado de CSS que clonan la estructura visual sobre un lienzo (<canvas>).
- **Codificación a Formato Documento (PDF):** 
  - A través de jsPDF, se instancia un motor de generación de documentos portátiles que captura la data-URI generada en el Canvas, escalando y paginando el contenido para adaptarlo automáticamente a la resolución de una página A4.
- **Aislamiento y Seguridad (Zero-Trust):** 
  - Al utilizar la FileReader API y buffers en memoria del navegador, todo el ciclo de vida de la conversión ocurre en un hilo local del cliente. El código fuente nunca pasa por un backend centralizado, eliminando riesgos de intercepción de datos confidenciales (Man-in-the-Middle).

## 📂 Estructura del Proyecto
`plaintext
html-to-pdf/
├── index.html          # Interfaz de usuario e importación de librerías CDN
├── app.js              # Manejador de eventos y lógica de parseo PDF
├── styles.css          # Variables CSS (Custom Properties) y Responsive Grid
├── icon.png            # Iconografía nativa HQ (Transparencia Alpha)
├── icon.ico            # Formato de binario de icono multipropósito
├── make_shortcut.ps1   # Script PowerShell de instalación de escritorio
└── README.md
`

## ⚙️ Uso y Despliegue
- Clonar el repositorio localmente.
- Arquitectura descentralizada: no necesita Node.js ni Webpack. Solo se requiere iniciar index.html en un navegador.
- Los módulos están desacoplados, permitiendo que la lógica de conversión en pp.js sea escalable a otros pipelines (React/Vue/Angular) si el proyecto crece.
