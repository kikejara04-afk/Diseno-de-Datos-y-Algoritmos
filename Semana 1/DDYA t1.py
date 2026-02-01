print(f"Vamos a verificar un número que decidas y se va a procesar.\n")
n = float(input("Ingresa un número para verificar si es positivo, negativo o 0: "))

def verificacion_num(n):
    if n < 0:
        print(f"{n} Es un número negativo.")
    if n > 0:
        print(f"El valor {n}, si es positivo.")
    elif n == 0:
        print(f"El valor del número es 0")
        
def serie_fibonacci(numero):
    numeros = [ ]
    a, b = 0, 1
    for i in numero:
        numeros.append(a)
        a, b = b, a + b
    print(f"{numeros}")
    if numero == i:
        print(f"{numero} si se encuentra en la serie fibonacci.")
    
#def si_es_primo(num):

def main():
    verificacion_num(n)
    print(f"\nAhora vamos a ver si un número entra en la serie Fibonacci.")
    fib = int(input("Ingresa un valor entero, ya sea negativo o positivo: "))
    serie_fibonacci(fib)
    print(f"Ahora vamos a ver si un numero es primo.\n")
   # primo = float(input("Ingresa un valor entero positivo: "))
    #si_es_primo(primo)
main()