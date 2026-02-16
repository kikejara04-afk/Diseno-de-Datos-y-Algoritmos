def contar_bits_totales(n):
    if n <= 0:
    # Caso base: si el número es 0 o menor, no hay bits que contar.
        return 0
        # Retornamos cero.
    k = n.bit_length() - 1
    # Calculamos la potencia de 2 más grande (2^k) que es menor o igual a n.
    
    bits_en_potencia_2 = k * (1 << (k - 1))
    # Por propiedades binarias, el total de bits de 0 hasta (2^k - 1) es k * 2^(k-1).
    
    bits_del_primer_digito = n - (1 << k) + 1
    # Contamos cuántas veces aparece el "1" a la izquierda desde 2^k hasta n.
    
    return bits_en_potencia_2 + bits_del_primer_digito + contar_bits_totales(n - (1 << k))
    # Sumamos los bits previos, los del primer dígito y resolvemos el resto recursivamente.

def encontrar_n_minimo(x):
    bajo = 0
    # Definimos el límite inferior del rango de búsqueda.
    alto = x
    # Definimos el límite superior (N nunca será mayor que X, pues cada número aporta al menos 1 bit).
    resultado = x
    # Variable para almacenar el mejor N encontrado hasta el momento.

    while bajo <= alto:
    # Iniciamos la búsqueda binaria (Divide y Vencerás sobre el rango de respuestas).
        medio = (bajo + alto) // 2
        # Calculamos el punto medio para probar si cumple la condición.
        
        if contar_bits_totales(medio) >= x:
        # Si la suma de bits hasta 'medio' ya es igual o mayor a X:
            resultado = medio
            # Guardamos este número como posible candidato.
            alto = medio - 1
            # Intentamos buscar un número todavía más pequeño hacia la izquierda.
        else:
        # Si la suma de bits es menor a X:
            bajo = medio + 1
            # Necesitamos más bits, así que buscamos números más grandes hacia la derecha.
            
    return resultado
    # Retornamos el valor mínimo encontrado que satisface la suma.

def main(): #funcion main
    x_objetivo = 5
    # Definimos la suma de bits que queremos alcanzar (según tu ejemplo).
    n_encontrado = encontrar_n_minimo(x_objetivo)
    # Invocamos la lógica para obtener el N mínimo.
    print(f"Para una suma de bits X = {x_objetivo}")
    # Mostramos el valor de entrada.
    print(f"El menor número N encontrado es: {n_encontrado}")
    # Mostramos el resultado (para X=5, el resultado es 4).
main()