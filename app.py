from flask import Flask, request, send_file
from pdf import addImages 
from util import getPath, storageFiles
app = Flask(__name__,  static_url_path="/files")

@app.route('/pdf', methods=['POST'])
def imgInPdf():
    file = request.files['input']
    vb = request.files['vb']
    sign = request.files['sign']
    f1, f2, f3 = storageFiles(file, vb, sign)
    output_file = addImages(f1, f2, f3, file.filename)
    return { "file": output_file }


@app.route('/pdf', methods=['GET'])
def getPdf():
    data = request.args
    output_file = getPath(data.get('name'))
    return send_file(output_file)

if __name__ == '__main__':
    app.run()