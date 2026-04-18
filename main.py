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
