# Funciones para aplicar filtros a la imagen
def gris(data):
    matrix = data.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            acum = 0
            for elem in matrix[i][j]:
                acum += elem
            prom = acum / 3
            matrix[i][j][0] = prom
            matrix[i][j][1] = prom
            matrix[i][j][2] = prom
    return matrix
 
def negative(data):
    matrix = data.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            red, green, blue = matrix[i][j] 
            matrix[i][j] = [255 - red, 255 - green , 255 - blue]
    return matrix

def effect(data):
    matrix = data.copy()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i]-1)):
            red, green, blue = matrix[i][j]
            matrix[i][j] = [red, green, blue/4]
    return matrix