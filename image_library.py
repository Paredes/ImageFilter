from PIL import Image
import numpy as np
from matplotlib import pyplot
import os

#Funciones para cargar, mostrar o guardar imagen
def load_image(namefile):
    with Image.open(namefile) as im:
        np_im = np.array(im)
    new_list = []
    for row in np_im:
        new_row = []
        for pixel in row:
            red, green, blue = pixel
            new_row.append([red, green, blue])
        new_list.append(new_row)
    return np_im

def show_image(data,title=None):
    if title is None:
        title=''
    im = Image.fromarray(data)
    pyplot.imshow(im)
    pyplot.title(title)
    pyplot.show()

def save_image(matrix, filename):
    path = os.path.join(os.getcwd(), 'output')
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)
    data = Image.fromarray(matrix)
    data.save(os.path.join(path,filename))