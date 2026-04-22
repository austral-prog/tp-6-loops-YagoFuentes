# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    string = []
    longitud = len(matrix)
    for x in range(longitud):
        string += matrix[x]
    return string


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    string = []
    longitud = len(matrix)
    for x in range(longitud):
        suma = sum(matrix[x])
        string.append(suma)
    return string


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    string = []
    longitudFilas = len(matrix)
    longitudColumnas = len(matrix[0])
    for x in range(longitudColumnas):  # 3
        suma = 0
        for c in range(longitudFilas):  # 2
            suma += (matrix[c][x])
        string.append(suma)
    return string
