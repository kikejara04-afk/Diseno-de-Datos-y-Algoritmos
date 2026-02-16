def merge_sort(lista):
# Definimos la función principal que recibe la lista de letras a ordenar.
    if len(lista) <= 1:
    # Caso base: si la lista tiene 1 elemento o está vacía, ya está ordenada.
        return lista
        # Devolvemos la lista tal cual para empezar a combinarla.
    medio = len(lista) // 2
    # Calculamos el índice central para dividir la lista en dos partes iguales.
    izquierda = merge_sort(lista[:medio])
    # Aplicamos recursión para dividir y ordenar la mitad izquierda.
    derecha = merge_sort(lista[medio:])
    # Aplicamos recursión para dividir y ordenar la mitad derecha.
    
    return mezclar(izquierda, derecha)
    # Llamamos a la función auxiliar para unir ambas mitades en orden.

def mezclar(izq, der):
# Esta función toma dos listas ordenadas y las fusiona en una sola.
    resultado = []
    # Creamos una lista vacía donde guardaremos los elementos ya ordenados.
    i = j = 0
    # Inicializamos dos punteros (i para la izquierda, j para la derecha).
    
    while i < len(izq) and j < len(der):
    # Mientras queden letras por comparar en ambas listas.
        if izq[i] < der[j]:
        # Si la letra de la izquierda es alfabéticamente menor.
            resultado.append(izq[i])
            # La añadimos a nuestra lista de resultado.
            i += 1
            # Avanzamos el puntero de la lista izquierda.
        else:
        # Si la letra de la derecha es menor o igual.
            resultado.append(der[j])
            # La añadimos a nuestra lista de resultado.
            j += 1
            # Avanzamos el puntero de la lista derecha.       
    resultado.extend(izq[i:])
    # Si sobraron letras en la lista izquierda, las pegamos al final.
    resultado.extend(der[j:])
    # Si sobraron letras en la lista derecha, las pegamos al final.
    return resultado
    # Devolvemos la lista combinada y perfectamente ordenada.

def main():
# Función principal para ejecutar nuestro experimento.
    palabra = "ALGORITMO"
    # Definimos la cadena de texto que queremos organizar.
    letras = list(palabra)
    # Convertimos el texto en una lista de caracteres individuales.
    print(f"Original: {palabra}")
    # Imprimimos la palabra antes del proceso.
    ordenadas = merge_sort(letras)
    # Ejecutamos el algoritmo de Divide y Vencerás.
    final = "".join(ordenadas)
    # Unimos las letras ordenadas para volver a formar una palabra.
    print(f"Ordenado: {final}")
    # Mostramos el resultado alfabético: AGILMOORT.
main()