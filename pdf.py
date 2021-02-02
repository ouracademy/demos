import fitz
from util import getPath

def shape_sign(x,y):
    w, h = (160,90) 
    return x,y, x+w,y+h


def addImages(origin, vb, sign, output):
    image_rectangle = fitz.Rect(500,40,550,100)
    file_handle = fitz.open(origin)
    num_pages = file_handle.pageCount
    for page_number in range(0,num_pages):
        page = file_handle[page_number]
        page.insertImage(image_rectangle, filename=vb)
        if page_number == num_pages - 1:
            x,y,x1,y1 = page.searchFor("Lima, 04 de enero de 2021")[0]
            rectangule = fitz.Rect(shape_sign(x+30,y+30))
            page.insertImage(rectangule, filename=sign)
    output_file = 'output-'+output
    file_handle.save(getPath(output_file))
    return output_file