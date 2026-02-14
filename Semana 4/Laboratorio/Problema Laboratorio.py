def contar_formas_dominos_3xn(n):
    """
    Cuenta cuántas formas hay de cubrir un tablero 3×n con dominós 2×1.
    (int) -> int
    """

    # n debe siempre ser par asi que verificamos
    if n % 2 == 1:
        return 0

    # tablas
    formas_completas = [0] * (n + 1) # formas de cubrir 3×n completo
    formas_con_hueco = [0] * (n + 1) 

    # casos base
    formas_completas[0] = 1
    formas_con_hueco[0] = 0

    if n >= 2:
        formas_completas[2] = 3
        formas_con_hueco[2] = 1 

    for n in range(4, n + 1, 2):
        formas_con_hueco[n] = formas_completas[n - 2] + formas_con_hueco[n - 2]
        formas_completas[n] = formas_completas[n - 2] + 2 * formas_con_hueco[n - 2]

    return formas_completas[n] 

def main():
    n = int(input())

    print(contar_formas_dominos_3xn(n))
main()
