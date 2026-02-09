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

'''
ANÁLISIS
DESCRIPCIÓN DEL PROBLEMA:
Desarrollar un sistema de clasificación de estudiantes que reciba como entrada una
cantidad de estudiantes seguidos de pares nombre-nota, y que procese estos datos 
utilizando el enfoque algorítmico de "Dividir y Conquistar" para clasificarlos 
en dos categorías: aprobados (nota >= 3) y reprobados (nota < 3).
El programa debe mantener la estructura modular con funciones especializadas y 
presentar los resultados de manera clara y organizada.


REQUERIMIENTOS (HISTORIAS DE USUARIO):

1. HISTORIA DE USUARIO: Ingreso de datos
   Como usuario, quiero ingresar la cantidad de estudiantes y sus calificaciones
   en una sola línea de entrada para ahorrar tiempo.
   Criterios de aceptación:
   - El programa debe recibir un número N seguido de N pares nombre-nota
   - Los datos deben estar separados por espacios
   - El programa debe validar que la cantidad de datos sea correcta

2. HISTORIA DE USUARIO: Clasificación de estudiantes
   Como sistema, necesito clasificar estudiantes en aprobados y reprobados
   utilizando un algoritmo eficiente de divide y conquista.
   Criterios de aceptación:
   - Un estudiante es aprobado si su nota es >= 3
   - Un estudiante es reprobado si su nota es < 3
   - El proceso debe usar recursión y división en mitades

3. HISTORIA DE USUARIO: Presentación de resultados
   Como usuario, quiero ver claramente los tres grupos de estudiantes
   (total, aprobados, reprobados) de forma organizada.
   Criterios de aceptación:
   - Mostrar encabezados descriptivos
   - Listar los estudiantes con su nombre y nota
   - Cada grupo debe estar claramente separado


ANÁLISIS DE COMPLEJIDAD:

Complejidad de tiempo:
- Función obtener_datos(): O(n) donde n es la cantidad total de elementos en la entrada
  Razón: split() recorre toda la cadena, int() es O(1)

- Función clasificar_estudiantes():
  * Construcción de lista_estudiantes: O(n) donde n es la cantidad de estudiantes
  * Función dividir_conquistar (algoritmo recursivo):
    - En cada nivel de recursión: Se divide el problema en 2 mitades
    - Niveles de recursión: log₂(n)
    - Trabajo en cada nivel: O(n) (por las operaciones de slicing y concatenación)
    - Complejidad total: O(n log n)
    - En el caso base: O(1) para listas vacías/unitarias

- Función mostrar_resultados(): O(n) donde n es la cantidad total de estudiantes
  Razón: Itera sobre todas los estudiantes para imprimirlos

- Complejidad temporal TOTAL del programa: O(n log n)
  Justificación: La operación dominante es el algoritmo de divide y conquista
  que se ejecuta en O(n log n)


ANÁLISIS PROPIO:

Ventajas del enfoque Divide y Conquista:
El enfoque de divide y conquista ofrece ventajas clave en este proyecto: escalabilidad 
superior con complejidad O(n log n), que supera a O(n²) en grandes volúmenes de datos; 
modularidad impecable al encapsular la lógica en la función recursiva dividir_conquistar(), 
separándola de entradas y salidas; claridad conceptual absoluta, ya que este patrón 
algorítmico es estándar y comprensible para cualquier programador; y recursión eficiente con 
profundidad O(log n), que evita desbordamientos en listas extensas. Aunque didácticamente 
poderoso para ilustrar la estrategia en Python con funciones anidadas, no es la opción óptima aquí, 
pues una iteración lineal simple alcanza O(n) sin la carga recursiva; sin embargo, 
este ejercicio impone su valor educativo al demostrar con autoridad cómo aplicar divide y conquista de manera efectiva.
'''
