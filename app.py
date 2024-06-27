from flask import Flask, request, jsonify, send_from_directory, render_template
import os
from shorts import Shorts

app = Flask(__name__)
shorts_generator = Shorts()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_short', methods=['POST'])
def generate_short():
    data = request.json
    topic = data.get('topic')
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    try:
        script = shorts_generator.generate(topic)
        return jsonify({'message': 'Short generated successfully', 'script': script}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    print(filename)
    return send_from_directory(os.path.join(app.root_path, 'outputs/final_video'), filename)

if __name__ == '__main__':
    app.run(debug=True)
