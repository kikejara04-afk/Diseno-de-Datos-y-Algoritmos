# Función para obtener y parsear los datos de entrada
def obtener_datos():
    # ENTRADA: Lee la cadena de entrada del usuario con cantidad de estudiantes y sus datos
    # Solicita al usuario que ingrese la cantidad de estudiantes seguida de pares nombre nota separados por espacios
    entrada = input("Ingrese la cantidad de estudiantes seguida de pares nombre nota (separados por espacios): ")
    # DIVIDIR: Convierte la cadena de entrada en una lista separada por espacios
    datos = entrada.split()
    # EXTRAER: Toma el primer elemento de la lista y lo convierte a entero para saber cuántos estudiantes hay
    n = int(datos[0])
    return datos, n

# Función para clasificar estudiantes en listas usando dividir y conquistar
def clasificar_estudiantes(datos, n):
    # PASO 1: DIVIDIR - Convertir datos crudos en lista de tuplas (nombre, nota)
    # Extrae pares nombre-nota de los datos de entrada y crea tuplas para cada estudiante
    lista_estudiantes = []
    for i in range(1, len(datos), 2):
        nombre = datos[i]
        nota = int(datos[i+1])
        estudiante = (nombre, nota)
        lista_estudiantes.append(estudiante)
    
    # PASO 2: CONQUISTAR - Aplicar algoritmo recursivo de dividir y conquistar
    # Función auxiliar recursiva que divide la lista, procesa cada parte y combina resultados
    def dividir_conquistar(lista):
        # CASO BASE: Si la lista tiene 0 o 1 elemento, procesarlo directamente sin más divisiones
        if len(lista) <= 1:
            # Clasificar el elemento base
            aprobados_base = [s for s in lista if s[1] >= 3]
            reprobados_base = [s for s in lista if s[1] < 3]
            return lista, aprobados_base, reprobados_base
        
        # CASO RECURSIVO: Dividir la lista en dos mitades aproximadamente iguales
        mitad = len(lista) // 2
        mitad_izquierda = lista[:mitad]
        mitad_derecha = lista[mitad:]
        
        # CONQUISTAR IZQUIERDA: Procesar recursivamente la mitad izquierda
        est_izq, aprob_izq, reprob_izq = dividir_conquistar(mitad_izquierda)
        
        # CONQUISTAR DERECHA: Procesar recursivamente la mitad derecha
        est_der, aprob_der, reprob_der = dividir_conquistar(mitad_derecha)
        
        # COMBINAR: Unir los resultados de ambas mitades
        estudiantes_combinados = est_izq + est_der
        aprobados_combinados = aprob_izq + aprob_der
        reprobados_combinados = reprob_izq + reprob_der
        
        return estudiantes_combinados, aprobados_combinados, reprobados_combinados
    
    # PASO 3: EJECUTAR - Ejecutar el algoritmo de dividir y conquistar en la lista completa
    estudiantes, aprobados, reprobados = dividir_conquistar(lista_estudiantes)
    return estudiantes, aprobados, reprobados

# Función para mostrar los resultados
def mostrar_resultados(estudiantes, aprobados, reprobados):
    # PASO 1: MOSTRAR LISTA COMPLETA - Imprime todos los estudiantes procesados
    # Encabezado de la sección de estudiantes
    print("Estudiantes:")
    # Iterar sobre cada estudiante y mostrar nombre y nota
    for nombre, nota in estudiantes:
        print(f"{nombre} {nota}")
    
    # PASO 2: MOSTRAR APROBADOS - Imprime solo los estudiantes con nota >= 3
    # Encabezado de la sección de aprobados
    print("Aprobados:")
    # Iterar sobre cada aprobado y mostrar nombre y nota
    for nombre, nota in aprobados:
        print(f"{nombre} {nota}")
    
    # PASO 3: MOSTRAR REPROBADOS - Imprime solo los estudiantes con nota < 3
    # Encabezado de la sección de reprobados
    print("Reprobados:")
    # Iterar sobre cada reprobado y mostrar nombre y nota
    for nombre, nota in reprobados:
        print(f"{nombre} {nota}")

# Función principal
def main():
    # PASO 1: OBTENER DATOS - Leer y parsear entrada del usuario
    # Obtiene la cantidad de estudiantes (n) y los datos crudos
    datos, n = obtener_datos()
    
    # PASO 2: CLASIFICAR USANDO DIVIDIR Y CONQUISTAR - Procesa datos con estrategia recursiva
    # Divide la lista de estudiantes en mitades, procesa recursivamente cada mitad,
    # y luego combina los resultados en listas de estudiantes, aprobados y reprobados
    estudiantes, aprobados, reprobados = clasificar_estudiantes(datos, n)
    
    # PASO 3: MOSTRAR RESULTADOS - Presentar los datos clasificados al usuario
    # Imprime las tres listas: todos los estudiantes, aprobados y reprobados
    mostrar_resultados(estudiantes, aprobados, reprobados)

# Ejecutar el programa - Inicia la ejecución del algoritmo de divide y conquista
main()
