def cant_digitos(n):
    """Tarea: Calcula cantidad de digitos de un número"""
    cant = 0
    while n > 0:
        cant += 1
        n = n // 10
    return cant
    

def suma_digitos(n):
    """Tarea: calcula la suma de los digitos de un número"""
    suma = 0
    while n > 0:
        suma = suma + n % 10
        n = n // 10
    return suma

