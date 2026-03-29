'''
Descripcion del problema:
Una tienda de tecnología necesita organizar su inventario de computadores. 
Cada computador tiene un código único que permite identificarlo. Uso de Arboles Binarios de 
Búsqueda (BST) para almacenar y gestionar el inventario.

# Este programa usa funciones y diccionarios (sin clases) para:
# 1) Crear y mostrar un BST de productos.
# 2) Insertar nuevos productos al BST.
# 3) Mostrar recorridos (preorden, inorden, postorden).
# 4) Analizar la forma del BST.
# 5) Demostrar insercion AVL y rotaciones necesarias.
'''

def linea(titulo=""):
    ancho = 66
    if not titulo:
        print("=" * ancho)
        return
    txt = f" {titulo} "
    r = max(0, ancho - len(txt))
    print("=" * (r // 2) + txt + "=" * (r - r // 2))


def nodo(v):
    # Crea un nodo BST:
    # - v: valor guardado en el nodo
    # - i: referencia al hijo izquierdo
    # - d: referencia al hijo derecho
    return {"v": v, "i": None, "d": None}


def bst_insertar(raiz, v):
    # Inserta un valor en el BST respetando la regla:
    # - Menores a la izquierda
    # - Mayores a la derecha
    # Si el valor se repite, no lo inserta.
    if raiz is None:
        return nodo(v)
    if v < raiz["v"]:
        raiz["i"] = bst_insertar(raiz["i"], v)
    elif v > raiz["v"]:
        raiz["d"] = bst_insertar(raiz["d"], v)
    return raiz


def bst_buscar(raiz, v):
    # Busca un codigo en el BST.
    # Retorna True si existe y False si no existe.
    while raiz is not None:
        if v == raiz["v"]:
            return True
        if v < raiz["v"]:
            raiz = raiz["i"]
        else:
            raiz = raiz["d"]
    return False


def preorden(raiz):
    # Recorre el arbol en orden: raiz -> izquierda -> derecha.
    # Sirve para ver primero el nodo principal de cada subarbol.
    if raiz is None:
        return []
    return [raiz["v"]] + preorden(raiz["i"]) + preorden(raiz["d"])


def inorden(raiz):
    # Recorre el arbol en orden: izquierda -> raiz -> derecha.
    # En un BST entrega los valores ordenados de menor a mayor.
    if raiz is None:
        return []
    return inorden(raiz["i"]) + [raiz["v"]] + inorden(raiz["d"])


def postorden(raiz):
    # Recorre el arbol en orden: izquierda -> derecha -> raiz.
    # Es util cuando primero se procesan hijos y al final la raiz.
    if raiz is None:
        return []
    return postorden(raiz["i"]) + postorden(raiz["d"]) + [raiz["v"]]


def altura(raiz):
    # Calcula la altura de un arbol:
    # altura = 1 + max(altura izquierda, altura derecha)
    # Si no hay nodo, altura 0.
    if raiz is None:
        return 0
    return 1 + max(altura(raiz["i"]), altura(raiz["d"]))


def analizar_forma_bst(raiz):
    # Analiza la forma general del BST comparando alturas de ambos lados.
    # Reporta si esta vacio, equilibrado o inclinado.
    if raiz is None:
        return "BST vacio: no hay nodos para analizar."

    h_izq = altura(raiz["i"])
    h_der = altura(raiz["d"])
    diferencia = h_izq - h_der

    if diferencia == 0:
        estado = "equilibrado"
    elif diferencia > 0:
        estado = "inclinado a la izquierda"
    else:
        estado = "inclinado a la derecha"

    return (
        f"Altura izquierda: {h_izq}, altura derecha: {h_der}. "
        f"Forma general: {estado}."
    )


def imprimir_arbol(raiz):
    # Dibuja el arbol en formato jerarquico con ramas ASCII.
    # Ejemplo visual:
    # [50]
    # |-- L: [30]
    # |   `-- R: [40]
    # `-- R: [70]
    if raiz is None:
        print("(arbol vacio)")
        return

    def dibujar_hijos(nodo_actual, prefijo=""):
        hijos = []
        if nodo_actual["i"] is not None:
            hijos.append(("L", nodo_actual["i"]))
        if nodo_actual["d"] is not None:
            hijos.append(("R", nodo_actual["d"]))

        for indice, (lado, hijo) in enumerate(hijos):
            es_ultimo = indice == len(hijos) - 1
            conector = "`-- " if es_ultimo else "|-- "
            print(prefijo + conector + f"{lado}: [{hijo['v']}]")
            siguiente_prefijo = prefijo + ("    " if es_ultimo else "|   ")
            dibujar_hijos(hijo, siguiente_prefijo)

    print(f"[{raiz['v']}]")
    dibujar_hijos(raiz)


def h(n):
    # Devuelve la altura almacenada en nodo AVL.
    # Si no existe nodo, retorna 0.
    return n["h"] if n else 0


def nodo_avl(v):
    # Nodo AVL igual a BST, pero con campo adicional h (altura).
    return {"v": v, "i": None, "d": None, "h": 1}


def actualizar_h(n):
    # Recalcula la altura de un nodo AVL despues de insertar o rotar.
    n["h"] = 1 + max(h(n["i"]), h(n["d"]))


def balance(n):
    # Factor de balance AVL:
    # balance = altura izquierda - altura derecha
    # Valores fuera de [-1, 1] indican desbalance.
    return h(n["i"]) - h(n["d"]) if n else 0


def rot_derecha(y):
    # Rotacion simple a la derecha (caso LL).
    # Se usa cuando el arbol crece demasiado por la izquierda.
    x = y["i"]
    t2 = x["d"]
    x["d"] = y
    y["i"] = t2
    actualizar_h(y)
    actualizar_h(x)
    return x


def rot_izquierda(x):
    # Rotacion simple a la izquierda (caso RR).
    # Se usa cuando el arbol crece demasiado por la derecha.
    y = x["d"]
    t2 = y["i"]
    y["i"] = x
    x["d"] = t2
    actualizar_h(x)
    actualizar_h(y)
    return y


def avl_insertar(raiz, v):
    # Inserta un valor en AVL y corrige desbalances con rotaciones.
    # Retorna:
    # - nueva raiz del subarbol
    # - texto de la rotacion aplicada
    if raiz is None:
        return nodo_avl(v), "Sin rotacion"

    if v < raiz["v"]:
        raiz["i"], rot = avl_insertar(raiz["i"], v)
    elif v > raiz["v"]:
        raiz["d"], rot = avl_insertar(raiz["d"], v)
    else:
        return raiz, "Sin rotacion (valor repetido)"

    actualizar_h(raiz)
    b = balance(raiz)

    if b > 1 and v < raiz["i"]["v"]:
        return rot_derecha(raiz), "Rotacion derecha (LL)"
    if b < -1 and v > raiz["d"]["v"]:
        return rot_izquierda(raiz), "Rotacion izquierda (RR)"
    if b > 1 and v > raiz["i"]["v"]:
        raiz["i"] = rot_izquierda(raiz["i"])
        return rot_derecha(raiz), "Rotacion doble izquierda-derecha (LR)"
    if b < -1 and v < raiz["d"]["v"]:
        raiz["d"] = rot_derecha(raiz["d"])
        return rot_izquierda(raiz), "Rotacion doble derecha-izquierda (RL)"

    return raiz, rot


def leer_opcion_menu():
    # Pide opcion principal y valida que sea una opcion del menu.
    while True:
        op = input("Seleccione una opcion: ").strip()
        if op in {"1", "2", "3", "4", "0"}:
            return op
        print("Dato no valido. Use solo 1, 2, 3, 4 o 0.")


def leer_codigo_busqueda():
    # Pide un codigo entero para buscar en el BST.
    while True:
        entrada = input("Ingrese el codigo de computador a buscar: ").strip()
        try:
            return int(entrada)
        except ValueError:
            print("Dato no valido. Ingrese un numero entero.")


def leer_tipo_recorrido():
    # Permite elegir el tipo de recorrido para visualizar nodos BST.
    while True:
        print("Tipo de recorrido:")
        print("1. Preorden")
        print("2. Inorden")
        print("3. Postorden")
        op = input("Seleccione recorrido: ").strip()
        if op in {"1", "2", "3"}:
            return op
        print("Dato no valido. Use solo 1, 2 o 3.")


def leer_productos_nuevos():
    # Lee valores enteros separados por coma.
    # Si hay error de formato, vuelve a pedir datos sin cerrar el programa.
    while True:
        entrada = input("Ingrese nuevos productos (ejemplo: 25,65,90): ").strip()
        if not entrada:
            print("Debe ingresar al menos un numero.")
            continue

        partes = [p.strip() for p in entrada.split(",")]
        valores = []
        valido = True

        for parte in partes:
            if not parte:
                valido = False
                break
            try:
                valores.append(int(parte))
            except ValueError:
                valido = False
                break

        if valido:
            return valores
        print("Entrada invalida. Use solo numeros enteros separados por comas.")


def mostrar_recorrido(raiz):
    # Muestra los nodos segun el recorrido elegido por el usuario.
    if raiz is None:
        print("BST vacio: no hay recorridos disponibles.")
        return

    opcion = leer_tipo_recorrido()
    if opcion == "1":
        print("Preorden:", preorden(raiz))
    elif opcion == "2":
        print("Inorden:", inorden(raiz))
    else:
        print("Postorden:", postorden(raiz))


def buscar_codigo_bst(raiz):
    # Ejecuta una busqueda de codigo y muestra resultado claro al usuario.
    if raiz is None:
        print("BST vacio: no hay codigos para buscar.")
        return

    codigo = leer_codigo_busqueda()
    if bst_buscar(raiz, codigo):
        print(f"Codigo {codigo}: ENCONTRADO en el inventario.")
    else:
        print(f"Codigo {codigo}: NO ENCONTRADO en el inventario.")


def demo_avl_con_rotaciones():
    # Demostracion guiada de AVL:
    # Inserta una secuencia fija y muestra si hubo rotacion en cada paso.
    linea("AVL: Insercion con Rotaciones")
    # Secuencia fija para el analisis solicitado.
    valores = [10, 20, 30, 40, 50]
    print("Valores a insertar en AVL:", valores)
    raiz_avl = None
    for valor in valores:
        raiz_avl, rotacion = avl_insertar(raiz_avl, valor)
        print(f"Insertado {valor}: {rotacion}")

    print("Arbol AVL final:")
    imprimir_arbol(raiz_avl)


def actividad_unica():
    # Proceso principal:
    # 1) Construye un arbol base de productos.
    # 2) Permite ver el BST y sus recorridos.
    # 3) Permite buscar codigos de computadores.
    # 4) Permite insertar productos y comparar antes/despues.
    # 5) Permite analizar BST vacio/actual y ejecutar demo AVL.
    raiz = None
    productos_base = [50, 30, 70, 20, 40, 60, 80]
    for valor in productos_base:
        raiz = bst_insertar(raiz, valor)

    while True:
        # Menu principal con tres acciones de estudio del tema.
        linea("Arbol de Productos")
        print("1. Ver BST y elegir recorrido (pre/in/postorden)")
        print("2. Buscar codigo de computador en el BST")
        print("3. Agregar productos al BST y ver antes/despues")
        print("4. Analizar BST vacio, forma del BST actual y demo AVL")
        print("0. Salir")

        opcion = leer_opcion_menu()

        if opcion == "1":
            # Visualizacion del BST actual y del recorrido seleccionado.
            linea("Arbol Actual")
            imprimir_arbol(raiz)
            mostrar_recorrido(raiz)
            print(analizar_forma_bst(raiz))
        elif opcion == "2":
            # Busca un codigo y confirma si existe o no en el inventario.
            linea("Busqueda de Codigo")
            buscar_codigo_bst(raiz)
        elif opcion == "3":
            # Muestra estado anterior, inserta y luego muestra estado final.
            linea("Antes de Agregar")
            imprimir_arbol(raiz)

            nuevos = leer_productos_nuevos()
            for valor in nuevos:
                raiz = bst_insertar(raiz, valor)

            linea("Despues de Agregar")
            imprimir_arbol(raiz)
            print(analizar_forma_bst(raiz))
        elif opcion == "4":
            # Analisis conceptual + aplicacion con AVL y rotaciones.
            linea("Analisis de BST Vacio")
            print(analizar_forma_bst(None))

            linea("Forma del BST Actual")
            imprimir_arbol(raiz)
            print(analizar_forma_bst(raiz))

            demo_avl_con_rotaciones()
        else:
            linea("Salida")
            print("Fin del programa.")
            break

print("Puede ver el arbol antes y despues de agregar productos.")
actividad_unica()