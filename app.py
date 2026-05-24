from flask import Flask, render_template, jsonify, send_file, request
from dotenv import load_dotenv
import os, pathlib, json, uuid

load_dotenv()
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB upload limit

# Uploaded sounds stored in data/sounds/
SOUNDS_DIR = pathlib.Path(__file__).parent / 'data' / 'sounds'
SOUNDS_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_EXTENSIONS = {'.wav', '.mp3', '.aif', '.aiff', '.flac', '.ogg', '.m4a'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sounds')
def list_sounds():
    sounds = []
    if SOUNDS_DIR.exists():
        for f in sorted(SOUNDS_DIR.iterdir()):
            if f.suffix.lower() in AUDIO_EXTENSIONS:
                sounds.append({'name': f.stem, 'filename': f.name})
    return jsonify(sounds)

@app.route('/api/sounds/upload', methods=['POST'])
def upload_sound():
    if 'file' not in request.files:
        return jsonify({'error': 'no file'}), 400
    f = request.files['file']
    if not f.filename:
        return jsonify({'error': 'no filename'}), 400
    ext = pathlib.Path(f.filename).suffix.lower()
    if ext not in AUDIO_EXTENSIONS:
        return jsonify({'error': 'unsupported format'}), 400
    safe_name = pathlib.Path(f.filename).stem[:60].replace(' ', '_') + ext
    dest = SOUNDS_DIR / safe_name
    f.save(dest)
    return jsonify({'name': pathlib.Path(safe_name).stem, 'filename': safe_name})

@app.route('/api/sounds/<path:filename>', methods=['DELETE'])
def delete_sound(filename):
    filepath = SOUNDS_DIR / filename
    if filepath.exists() and filepath.suffix.lower() in AUDIO_EXTENSIONS:
        filepath.unlink()
        return jsonify({'ok': True})
    return jsonify({'error': 'not found'}), 404

@app.route('/sounds/<path:filename>')
def serve_sound(filename):
    filepath = SOUNDS_DIR / filename
    if filepath.exists() and filepath.suffix.lower() in AUDIO_EXTENSIONS:
        return send_file(filepath)
    return jsonify({'error': 'not found'}), 404

@app.route('/api/status')
def status():
    return jsonify({'status': 'ok', 'project': 'time'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5568))
    host = '0.0.0.0' if os.environ.get('RAILWAY_ENVIRONMENT') else '127.0.0.1'
    app.run(host=host, port=port, debug=False)
