
import os

from rotation_flipping import mirroring_hori,mirroring_vert,rotate_180
from transform_image import effect,negative,gris
from image_library import load_image,save_image,show_image

namefile = 'Lenna.png'
data = load_image(namefile)

escala_grises = gris(data)
espejado_horizontal = mirroring_hori(data)
espejado_vertical = mirroring_vert(data)
rotado_180 = rotate_180(data) 
negativo = negative(data)
efecto = effect(data)


show_image(escala_grises,'Escala de grises')

# save_image(escala_grises, 'Lenna_escala_gris.png')
# save_image(espejado_horizontal, 'Lenna_espejo_hor.png')
# save_image(espejado_vertical, 'Lenna_espejo_vert.png')
# save_image(rotado_180, 'Lenna_rotate_180.png')