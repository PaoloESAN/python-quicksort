"""
Implementación del algoritmo Quicksort utilizando sub-arrays.
"""


def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivote = array[len(array) // 2]
        menores = [x for x in array if x < pivote]
        iguales = [x for x in array if x == pivote]
        mayores = [x for x in array if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)


def casoPruebaSentencia():
    array1 = [7, 8, 1, 3, 4, 8, 9, 6, 2]
    print("Array1 prueba sentencia:", quicksort(array1))  # (8/9)*100 = 89%
    array2 = [1]
    print("Array2 prueba sentencia:", quicksort(array2))  # (3/9)*100 = 33%


def casoPruebaDecision():

    # CASO 1: Un array con un solo elemento.

    array_simple = [5]
    print(f"Array1 prueba decisión {array_simple}:", quicksort(array_simple))
    # Decisiones cubiertas: 1 de 8
    # (1/8)*100 = 12.5% de cobertura de decisión inicial.

    # CASO 2: Un array con todos los mismos números.

    array_iguales = [7, 7, 7]
    print(f"Array2 prueba decisión {array_iguales}:", quicksort(array_iguales))
    # Decisiones cubiertas: 5 de 8
    # (5/8)*100 = 62.5% de cobertura de decisión.

    # CASO 3: Un array estratégico (menores, iguales y mayores al pivote).

    array_optimo = [2, 1, 3]
    print(f"Array3 prueba decisión {array_optimo}:", quicksort(array_optimo))
    # Decisiones cubiertas: 8 de 8
    # (8/8)*100 = 100%


numeros = [34, 7, 23, 32, 5, 62, 32, 2, 78, 1]
print("Array original:", numeros)

numeros_ordenados = quicksort(numeros)
print("Array ordenado:", numeros_ordenados)

casoPruebaSentencia()
casoPruebaDecision()
