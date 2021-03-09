# Funciones para aplicar filtros a la imagen
def grayscale(data, basic=False):
    def grayscale_1(data):
        matrix = data.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                red, green, blue = matrix[i][j]
                prom = (red + green + blue)/3
                matrix[i][j] = [prom, prom, prom]
        return matrix

    # Usando la recomendacion BT.601-7
    def grayscale_2(data):
        matrix = data.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                red, green, blue = matrix[i][j]
                gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
                matrix[i][j] = [int(gray), int(gray), int(gray)]
        return matrix
    if basic:
        return grayscale_1(data)
    else:
        return grayscale_2(data)
        
def negative(data):
    matrix = data.copy()
    neg = lambda color: 255 - color
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            red, green, blue = matrix[i][j] 
            matrix[i][j] = [neg(red), neg(green), neg(blue)]
    return matrix

def effect(data):
    matrix = data.copy()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i]-1)):
            red, green, blue = matrix[i][j]
            matrix[i][j] = [red, green, blue/4]
    return matrix