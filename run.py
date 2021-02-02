from flask import Flask, request, send_file
from flask_cors import CORS
from pdf import addImages 
from util import getPath, storage
app = Flask(__name__,  static_url_path="/files")
CORS(app)

@app.route('/pdf', methods=['POST'])
def imgInPdf():
    file = request.files['input']
    file_path = storage(file)
    vb_path = storage(request.files['vb'])
    sign_path = storage(request.files['sign'])
    output_file = addImages(file_path, vb_path, sign_path, file.filename)

    url_file = f'{request.base_url}?name={output_file}'
    return { "file": url_file }


@app.route('/pdf', methods=['GET'])
def getPdf():
    data = request.args
    output_file = getPath(data.get('name'))
    return send_file(output_file)


@app.route('/')
def hello():
    return 'Ouracademy demos'

if __name__ == '__main__':
    app.run()