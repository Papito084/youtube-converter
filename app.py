from flask import Flask, render_template, request, send_file, jsonify
import yt_dlp
import os
import re
import imageio_ffmpeg

# Base directory is wherever this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

# Ensure download directory exists
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'downloads')
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    url = data.get('url')
    fmt = data.get('format', 'mp3')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Use video ID for the initial filename to avoid OS filesystem issues with special characters
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(id)s.%(ext)s'),
            'noplaylist': True,
            'restrictfilenames': True,
            'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe(),
        }

        if fmt == 'mp4':
            ydl_opts.update({
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'merge_output_format': 'mp4',
            })
        else:  # mp3
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            temp_filename = ydl.prepare_filename(info)

            # Handle extension changes due to post-processing or merging
            base, ext = os.path.splitext(temp_filename)
            if fmt == 'mp3':
                temp_filename = base + '.mp3'
                ext = '.mp3'
            elif fmt == 'mp4':
                temp_filename = base + '.mp4'
                ext = '.mp4'

            # Rename to the human-readable title
            video_title = info.get('title', 'Video')
            safe_title = sanitize_filename(video_title)
            final_filename = os.path.join(DOWNLOAD_FOLDER, f"{safe_title}{ext}")

            if os.path.exists(temp_filename):
                if os.path.exists(final_filename) and os.path.abspath(temp_filename) != os.path.abspath(final_filename):
                    try:
                        os.remove(final_filename)
                    except Exception:
                        pass

                try:
                    os.rename(temp_filename, final_filename)
                except Exception as e:
                    print(f"Rename failed: {e}")
                    final_filename = temp_filename

            return jsonify({
                'message': 'Conversion successful',
                'filename': os.path.basename(final_filename),
                'title': video_title
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
