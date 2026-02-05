numeros = [64, 34, 25, 12, 22, 11, 90]
'''

Define una lista de números enteros que se utilizará como ejemplo para el ordenamiento.

'''
def insertion_sort_descendente(arr):
    """
    
    Implementa el algoritmo de Insertion Sort para ordenar en orden descendente.
    donde arr esta definido como parámetro y la ordena en orden descendente.
    
    """
    n = len(arr)
    
    # Recorremos desde el segundo elemento
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Movemos elementos mayores que key una posición a la derecha
        # Cambiamos la condición a > para orden descendente
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j] #Mueve el elemento en arr[j] una posición a la derecha.
            j -= 1 # Decrementa j para seguir comparando con los elementos anteriores.
        
        # Insertamos key en su posición correcta
        arr[j + 1] = key
    
    return arr # Devuelve la lista ordenada en orden descendente.

def main(): #Llama a la función principal
    print(f"Lista original: {numeros}")
    
    resultado = insertion_sort_descendente(numeros) #Llama a la función de ordenamiento con la lista numeros y asigna el resultado a resultado
    print(f"Lista ordenada (descendente): {resultado}")
main() # para ejecutar el ejemplo.
