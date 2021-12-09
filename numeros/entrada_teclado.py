def ingreso_entero():
    """Tarea: asegurarse que el usuario ingresa un número entero"""
    cn = input("Ingrese número entero: ")
    while float(cn) != int(float(cn)):
        cn = input("Ingrese número entero: ")
    return int(cn)
    

def ingreso_natural():
    """Tarea: asegurarse que el usuario ingresa un número par"""
    cn = input("Ingrese número natural: ")
    while float(cn) != int(float(cn)) or int(cn) <= 0:
        cn = input("Ingrese número natural: ")
    return int(cn)
    

    

