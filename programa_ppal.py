from verificaciones_numericas import *
from numeros.entrada_teclado import *
from numeros.digitos_numero.aritmetica import *


"""

Tarea: Permite ingresar números enteros hasta que se ingrese el valor 0.
Además, informa cantidad de números pares y números de dos digitos
ingresados.

"""

cant_pares = 0
cant_nros_dos_dig = 0

n = ingreso_entero()

while n != 0:
    if es_par(n):
        cant_pares += 1
    if cant_digitos(n) == 2:
        cant_nros_dos_dig += 1
    n = ingreso_entero()

print("Cantidad de números pares ingresados: {}\n".format(cant_pares))
print("Cantidad de números de dos digitos ingresados: {}\n".format(cant_nros_dos_dig))

