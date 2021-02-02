from flask import Flask, request, send_file
from pdf import addImages 
from util import getPath, storage
app = Flask(__name__,  static_url_path="/files")

@app.route('/pdf', methods=['POST'])
def imgInPdf():
    file = request.files['input']
    file_path = storage(file)
    vb_path = storage(request.files['vb'])
    sign_path = storage(request.files['sign'])
    output_file = addImages(file_path, vb_path, sign_path, file.filename)
    return { "file": output_file }


@app.route('/pdf', methods=['GET'])
def getPdf():
    data = request.args
    output_file = getPath(data.get('name'))
    return send_file(output_file)

if __name__ == '__main__':
    app.run()