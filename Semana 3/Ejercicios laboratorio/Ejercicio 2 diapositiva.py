def busqueda_binaria(arr):
	# lo y hi definen los índices entre los que buscamos.
	lo = 0
	hi = len(arr) - 1
	# Invariante: el entero faltante está en la posición (lo..hi+1) respecto a índices+1
	while lo <= hi:
		# Calcula el punto medio.
		mid = (lo + hi) // 2
		# Si el valor en mid coincide con el valor esperado mid+1,
		# entonces todos los elementos desde 0..mid están alineados correctamente,
		# así que el faltante (si existe) está en la mitad derecha.
		if arr[mid] == mid + 1:
			lo = mid + 1
		else:
			# Si arr[mid] != mid+1, el faltante está en la mitad izquierda (incluyendo mid).
			hi = mid - 1
	# Cuando el bucle termina, lo apunta a la primera posición donde
	# el valor esperado index+1 no se cumple, por lo que el entero faltante es lo+1.
	return lo + 1


def encontrar_faltante(arr):
	"""
	Parámetros
	- arr: lista ordenada de enteros de longitud N-1 con valores en 1..N

	Retorna
	- El entero faltante en 1..N.
	"""
	# Delegamos la lógica de divide y vencerás a la función privada en español.
	return busqueda_binaria(arr)


def main():
	ejem = [
		# arreglo con faltante en medio -> 5
		[1, 2, 3, 4, 6, 7, 8],
		# arreglo con faltante en medio -> 7
		[1, 2, 3, 4, 5, 6, 8, 9]
	]
	for arr in ejem:
		print(f"{arr} -> faltante {encontrar_faltante(arr)}")

main()