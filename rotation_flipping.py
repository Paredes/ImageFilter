#Funciones para espejar una imagen
def mirroring_hori(data):
    matrix = data.copy()
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix

def mirroring_vert(data):
    matrix = data.copy()
    return matrix[::-1]

# Funciones para rotar imagen 

def rotate_90(data):
    matrix = data.copy()
    new_matrix = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)-1,-1,-1):
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix

def rotate_180(data):
    matrix = data.copy()
    return mirroring_hori(mirroring_vert(matrix))