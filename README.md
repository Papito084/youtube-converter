# YouTube to MP3/MP4 Converter

Servicio backend RESTful desarrollado en Python (Flask) para la extracción, procesamiento y conversión de streams de video utilizando herramientas de línea de comandos del ecosistema FFmpeg.

## 🏗️ Arquitectura y Funcionamiento Interno
- **Arquitectura Cliente-Servidor:** 
  - El frontend se comunica con el framework Flask mediante peticiones HTTP POST asíncronas (`Fetch API`), enviando payloads en formato JSON.
  - El backend procesa las solicitudes, orquestando la descarga y emitiendo una respuesta con las rutas absolutas para el acceso al archivo resultante.
- **Motor de Extracción y Conversión:**
  - Se integra `yt-dlp` como módulo de resolución de URLs para desencriptar firmas de video y descargar flujos de máxima calidad.
  - Implementa un pipeline de transcodificación mediante `ffmpeg` (gestionado por `imageio-ffmpeg`) que permite extraer pistas de audio o remultiplexar contenedores (MP4) sobre la marcha.
- **Gestión del Almacenamiento y Temporales:** Los archivos procesados se almacenan temporalmente en el volumen de sistema `/downloads/`. Se sanitizan los nombres de archivo mediante expresiones regulares para evitar vulnerabilidades de Path Traversal.

## 📂 Estructura del Proyecto

```text
youtube-converter/
├── app.py                  # Router principal y Endpoints Flask
├── requirements.txt        # Manejo de dependencias de entorno
├── templates/
│   └── index.html          # Vistas HTML (Frontend)
├── static/                 # Archivos estáticos (CSS, JS modular, assets)
├── downloads/              # Directorio de procesamiento (ignorado en Git)
├── Launch YouTube Converter.bat  # Entry-point automatizado para Windows
└── README.md
```

## 🚀 Instalación y Puesta en Marcha

**Requisitos Previos:**
- Python 3.10+ instalado en el sistema.
- FFmpeg configurado en el PATH del sistema (o instalado mediante módulo).

**Pasos:**

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Papito084/youtube-converter.git
   cd youtube-converter
   ```
2. **Crear y activar un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/macOS:
   source venv/bin/activate
   ```
3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```
5. Accede a la interfaz web en: `http://localhost:5000`

## 🛠️ Endpoints Principales

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| **GET** | `/` | Carga de la interfaz web principal. |
| **POST** | `/convert` | Recibe la URL y formato (`mp3` / `mp4`), inicia la extracción y retorna el archivo procesado. |
| **GET** | `/download/<file>` | Sirve el archivo estático procesado al cliente como descarga. |
