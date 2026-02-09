# Función para obtener y parsear los datos de entrada
def obtener_datos():
    # Solicitar entrada al usuario: Pide al usuario que ingrese la cantidad de estudiantes y sus datos en una sola línea.
    entrada = input("Ingrese la cantidad de estudiantes seguida de pares nombre nota (separados por espacios): ")
    # Dividir la entrada en una lista: Convierte la cadena de entrada en una lista separada por espacios.
    datos = entrada.split()
    # Extraer la cantidad de estudiantes: Toma el primer elemento de la lista y lo convierte a entero para saber cuántos estudiantes hay.
    n = int(datos[0])
    return datos, n

# Función para clasificar estudiantes en listas
def clasificar_estudiantes(datos, n):
    # Inicializar listas: Crea listas vacías para almacenar todos los estudiantes, aprobados y reprobados.
    estudiantes = []
    aprobados = []
    reprobados = []
    # Procesar los datos: desde el índice 1, tomar pares nombre-nota: Itera sobre la lista de datos, empezando desde el índice 1, tomando pares de nombre y nota.
    for i in range(1, len(datos), 2):
        # Extraer nombre y nota: Obtiene el nombre y la nota del estudiante actual.
        nombre = datos[i]
        nota = int(datos[i+1])
        # Crear tupla del estudiante: Forma una tupla con el nombre y la nota.
        estudiante = (nombre, nota)
        # Agregar a la lista de estudiantes: Añade la tupla a la lista de todos los estudiantes.
        estudiantes.append(estudiante)
        
        # Verificar aprobación: Si la nota es mayor o igual a 3, se considera aprobado; de lo contrario, reprobado.
        if nota >= 3:
            # Agregar a aprobados: Añade el estudiante a la lista de aprobados.
            aprobados.append(estudiante)
        else:
            # Agregar a reprobados: Añade el estudiante a la lista de reprobados.
            reprobados.append(estudiante)
    return estudiantes, aprobados, reprobados

# Función para mostrar los resultados
def mostrar_resultados(estudiantes, aprobados, reprobados):
    # Mostrar resultados sin brackets ni paréntesis: Imprime el encabezado para la lista de estudiantes.
    print("Estudiantes:")
    # Iterar sobre estudiantes: Para cada estudiante, imprime el nombre y la nota sin formato de lista.
    for nombre, nota in estudiantes:
        print(f"{nombre} {nota}", end=', '"\n")
    
    # Imprimir encabezado para aprobados: Muestra el título para la lista de aprobados.
    print("Aprobados:")
    # Iterar sobre aprobados: Para cada aprobado, imprime el nombre y la nota.
    for nombre, nota in aprobados:
        print(f"{nombre} {nota}")
    
    # Imprimir encabezado para reprobados: Muestra el título para la lista de reprobados.
    print("Reprobados:")
    # Iterar sobre reprobados: Para cada reprobado, imprime el nombre y la nota.
    for nombre, nota in reprobados:
        print(f"{nombre} {nota}")

# Función principal
def main():
    datos, n = obtener_datos() # Llama a la función para obtener los datos de entrada
    estudiantes, aprobados, reprobados = clasificar_estudiantes(datos, n) # Clasifica a los estudiantes en listas
    mostrar_resultados(estudiantes, aprobados, reprobados) # Muestra los resultados

# Ejecutar el programa
main()

'''

Análisis de Complejidad de Tiempo
El código procesa datos de estudiantes en una sola entrada, clasificándolos y mostrándolos. La complejidad se mide en términos de n (número de estudiantes), asumiendo que la entrada es válida y que el tamaño de la cadena de entrada es proporcional a n (aprox. 2n elementos después del split).
Complejidad general: O(n), ya que las operaciones principales (parsing, clasificación y impresión) son lineales en n.

obtener_datos(): El split de la cadena es O(m), donde m ≈ 2n (elementos en la lista), y extracción de n es O(1). Total: O(n).
clasificar_estudiantes(): Bucle que itera n veces (una por estudiante), con operaciones O(1) por iteración. Total: O(n).
mostrar_resultados(): Tres bucles que iteran sobre listas de tamaño total O(n), con impresiones O(1) por elemento. Total: O(n).
main(): Llamadas secuenciales, no añade complejidad adicional.

Mejor caso: Cuando n = 0 (sin estudiantes), todas las operaciones son O(1), ya que no hay bucles o procesamiento de listas.
Peor caso: Cuando n es grande (ej. miles de estudiantes), la complejidad es O(n), dominada por los bucles de clasificación e impresión. No hay dependencias cuadráticas o peores; el código es eficiente para entradas típicas.

Analisis propio: puedo confirmar que el código maneja eficientemente los datos de n estudiantes en O(n), con el parsing inicial dominando a través del split en O(m) ≈ O(n), 
seguido de bucles simples para clasificar e imprimir sin complicaciones extras; en el mejor caso, con n=0, todo se resuelve en O(1), y en el peor, con miles de entradas, 
se mantiene escalable y robusto, lo que me convence de que no requiere mejoras adicionales para usos prácticos

PD: Grafica de mejor/peor caso en un documento aparte llamado "Grafica_Analisis_Complejidad"

'''

