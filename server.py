from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess


app = Flask(__name__)
CORS(app)  #모든 출처 허용 (개발용)
#CORS(app, resources={r"/run-python": {"origins": "http://127.0.0.1:5500"}}) 실 배포시

@app.route('/run-python', methods=['POST'])
def run_python():
    result = subprocess.run(['python', 'test1/googlecrawling.py'], capture_output=True, text=True)
    return jsonify({
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
