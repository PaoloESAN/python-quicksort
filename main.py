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
    array1 = [7,8,1,3,4,8,9,6,2]
    print("Array1 prueba sentencia:", quicksort(array1))  # (8/9)*100 = 89%
    array2 = [1]
    print("Array2 prueba sentencia:", quicksort(array2)) # (3/9)*100 = 33%

numeros = [34, 7, 23, 32, 5, 62, 32, 2, 78, 1]
print("Array original:", numeros)

numeros_ordenados = quicksort(numeros)
print("Array ordenado:", numeros_ordenados)

casoPruebaSentencia()