def quicksort(array):
    """
    Implementación del algoritmo Quicksort utilizando sub-arrays.
    """
    if len(array) <= 1:
        return array
    else:
        pivote = array[len(array) // 2]

        menores = [x for x in array if x < pivote]
        iguales = [x for x in array if x == pivote]
        mayores = [x for x in array if x > pivote]
        
        return quicksort(menores) + iguales + quicksort(mayores)

numeros = [34, 7, 23, 32, 5, 62, 32, 2, 78, 1]
print("Array original:", numeros)

numeros_ordenados = quicksort(numeros)
print("Array ordenado:", numeros_ordenados)