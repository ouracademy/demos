from werkzeug.utils import secure_filename
import os
def getPath(name, folder = 'files'):
    return os.path.join(folder, secure_filename(name))

def storage(file):
    path = getPath( name = file.filename)
    file.save(path)
    return path
