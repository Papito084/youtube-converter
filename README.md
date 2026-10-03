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

1. Clona el repositorio.
2. Instala las dependencias necesarias abriendo una terminal en la carpeta:
   ```bash
   pip install flask yt-dlp imageio-ffmpeg
   ```
3. Ejecuta la aplicacin haciendo doble clic en el archivo proporcionado `Launch YouTube Converter.bat` o desde la terminal ejecutando `python app.py`.
4. La aplicacin web se abrir automticamente (por defecto en `http://localhost:5000`).
5. Pega la URL del video y descarga.
