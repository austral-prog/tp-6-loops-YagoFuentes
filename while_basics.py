# Replace the "ANSWER HERE" for your answer

def countdown(n):
    """
    Retorna una lista con la cuenta regresiva desde n hasta 0.
    Si n < 0, retorna una lista vacia.

    Ejemplo: countdown(5) -> [5, 4, 3, 2, 1, 0]
    Ejemplo: countdown(0) -> [0]
    Ejemplo: countdown(-1) -> []
    """
    sting = []
    if n == 0:
        return [0]
    while n > 0:
        for x in range(n + 1):
            sting.insert(0, x)
            n -= 1

    return sting



def double_until(limit):
    """
    Comenzando desde 1, va duplicando el valor y agrega cada uno
    a una lista mientras sea menor o igual a limit.
    Si limit < 1, retorna una lista vacia.

    Ejemplo: double_until(10) -> [1, 2, 4, 8]
    Ejemplo: double_until(1) -> [1]
    Ejemplo: double_until(0) -> []
    """
    sucesion = [1]
    adicion = 1
    if limit == 0:
        del sucesion[0]
        return sucesion
    while (adicion * 2) <= limit:
        adicion = adicion * 2
        sucesion.append(adicion)
    return sucesion
