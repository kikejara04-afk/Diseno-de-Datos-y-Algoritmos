# Función para obtener y parsear los datos de entrada
def obtener_datos():
    # Solicita al usuario la entrada de texto por consola
    entrada = input("Ingrese la cantidad de estudiantes seguida de pares nombre nota (separados por espacios): ")
    # # Convierte el texto ingresado en una lista de palabras/números usando los espacios como separador
    datos = entrada.split()
    # # Verifica si la lista está vacía para evitar errores de ejecución
    if not datos: return [], 0
    # # Extrae el primer elemento y lo convierte a entero para definir el número de registros
    n = int(datos[0])
    # # Retorna la lista completa de datos y el número total de estudiantes
    return datos, n

# Función para clasificar estudiantes usando Programación Dinámica
def clasificar_estudiantes(datos, n):
    # Inicializa una lista vacía para almacenar los datos limpios (tuplas de nombre y nota)
    lista_estudiantes = []
    # # Recorre los datos crudos saltando de 2 en 2 para emparejar nombres con sus notas
    for i in range(1, len(datos), 2):
        # # Asigna el elemento actual de la lista como el nombre del estudiante
        nombre = datos[i]
        # # Asigna el siguiente elemento como la nota, convirtiéndolo de texto a entero
        nota = int(datos[i+1])
        # # Agrega una tupla con el par (nombre, nota) a la lista de estudiantes
        lista_estudiantes.append((nombre, nota))
    
    # Crea un diccionario para almacenar los resultados de estudiantes ya evaluados (Memoización)
    memoria_clasificacion = {}
    # # # 
    # # Inicializa la lista que contendrá a todos los estudiantes procesados
    estudiantes_procesados = []
    # # Inicializa la lista para los estudiantes que pasaron la materia (nota >= 3)
    aprobados = []
    # # Inicializa la lista para los estudiantes que perdieron la materia (nota < 3)
    reprobados = []

    # Inicia el ciclo para procesar cada estudiante de la lista original
    for est in lista_estudiantes:
        # # Desempaqueta la tupla del estudiante en variables individuales de nombre y nota
        nombre, nota = est
        # # Añade el estudiante actual a la lista general de salida
        estudiantes_procesados.append(est)

        # Revisa si el nombre del estudiante ya existe en la memoria para no repetir el cálculo
        if nombre in memoria_clasificacion:
            # # Si ya existe, recupera el resultado guardado (Aprobado o Reprobado)
            resultado = memoria_clasificacion[nombre]
        else:
            # # Si no está en memoria, evalúa si la nota es mayor o igual a 3
            if nota >= 3:
                # # Define el resultado como "Aprobado"
                resultado = "Aprobado"
            else:
                # # Define el resultado como "Reprobado"
                resultado = "Reprobado"
            # # Guarda el nuevo resultado en el diccionario de memoria para futuras consultas
            memoria_clasificacion[nombre] = resultado

        # Clasifica al estudiante en su lista correspondiente basándose en el resultado obtenido
        if resultado == "Aprobado":
            # # Agrega al estudiante a la lista final de aprobados
            aprobados.append(est)
        else:
            # # Agrega al estudiante a la lista final de reprobados
            reprobados.append(est)
                
    # Retorna las tres listas generadas: total, aprobados y reprobados
    return estudiantes_procesados, aprobados, reprobados

# Función para mostrar los resultados en pantalla
def mostrar_resultados(estudiantes, aprobados, reprobados):
    # Imprime un encabezado para la sección de todos los estudiantes
    print("\nEstudiantes:")
    # # Recorre la lista de todos los estudiantes procesados
    for nombre, nota in estudiantes:
        # # Muestra el nombre y la nota de cada uno
        print(f"{nombre} {nota}")
    
    # Imprime un encabezado para la sección de aprobados
    print("Aprobados:")
    # # Recorre únicamente la lista de los que ganaron la materia
    for nombre, nota in aprobados:
        # # Muestra el nombre y la nota del estudiante aprobado
        print(f"{nombre} {nota}")
    
    # Imprime un encabezado para la sección de reprobados
    print("Reprobados:")
    # # Recorre únicamente la lista de los que perdieron la materia
    for nombre, nota in reprobados:
        # # Muestra el nombre y la nota del estudiante reprobado
        print(f"{nombre} {nota}")

# Función principal que coordina la ejecución
def main():
    # Llama a la función de entrada y guarda los valores obtenidos
    datos, n = obtener_datos()
    # # Verifica que la cantidad de estudiantes sea mayor a cero para proceder
    if n > 0:
        # # Llama a la lógica de programación dinámica para clasificar los datos
        est_totales, est_aprobados, est_reprobados = clasificar_estudiantes(datos, n)
        # # Envía las listas resultantes a la función encargada de imprimirlas
        mostrar_resultados(est_totales, est_aprobados, est_reprobados)
main()