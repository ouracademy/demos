from werkzeug.utils import secure_filename
import os
def getPath(name, folder = 'files'):
    return os.path.join(folder, secure_filename(name))

def storageFiles(origin, vb, sign):
    file_path_origin = getPath( name = origin.filename)
    origin.save(file_path_origin)

    file_path_vb = getPath( name = vb.filename)
    vb.save(file_path_vb)

    file_path_sign = getPath( name = sign.filename)
    sign.save(file_path_sign)

    return file_path_origin,file_path_vb,file_path_sign
