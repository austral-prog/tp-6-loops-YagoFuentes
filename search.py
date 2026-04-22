# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    longitud = len(lst)
    if not target in lst:
        return -1
    for x in range(longitud):
        if lst[x] == target:
            return x


def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """
    longitud = len(lst)
    if not target in lst:
        return -1
    elif start == 0:
        for x in range(start, longitud):
            if lst[x] == target:
                return x
    elif not target in lst[start + 1:longitud]:
        return -1
    for x in range(start + 1, longitud):
        if lst[x] == target:
            return x


def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    longitud = len(lst)
    if not "" in lst:
        return -1
    for x in range(longitud):
        if lst[x] == "":
            return x
