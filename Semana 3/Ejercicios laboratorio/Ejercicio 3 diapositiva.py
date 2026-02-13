def exponenciacion_modular(base, exponente, modulo): # Definimos la función con sus tres parámetros
    if exponente == 0:                               # Si el exponente llega a cero (caso base)
        return 1                                     # Retornamos 1 porque cualquier número a la 0 es 1
    
    # Dividir: Llamada recursiva con la mitad del exponente (división entera //)
    mitad = exponenciacion_modular(base, exponente // 2, modulo) # Guardamos el resultado de la mitad
    
    # Vencer: Elevamos al cuadrado el resultado obtenido y aplicamos el módulo
    resultado = (mitad * mitad) % modulo             # Esto reduce drásticamente el número de operaciones
    
    if exponente % 2 == 0:                           # Si el exponente original era par
        return resultado                             # El resultado actual es correcto y lo devolvemos
    else:                                            # Si el exponente era impar (sobra uno al dividir)
        return (resultado * base) % modulo           # Multiplicamos por la base una vez más y aplicamos módulo

def main():                                          # Función principal para organizar la ejecución
    base_num = 5                                     # Definimos la base (a)
    exp_num = 3                                      # Definimos el exponente (n)
    mod_num = 13                                     # Definimos el módulo (m)
    
    # Invocamos la función y guardamos lo que nos devuelva
    final = exponenciacion_modular(base_num, exp_num, mod_num) # Llamada al algoritmo de divide y vencerás
    
    print(f"Resultado: {final}")                     # Mostramos el resultado final en la consola
    main()                                           # Si es así, arrancamos el programa llamando a main