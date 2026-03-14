#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Cada elemento en la pila guarda: (nivel_pesticida, dias_hasta_morir)
    stack = []
    max_days = 0

    for pesticide in p:
        days = 0

        # Si encontramos plantas a la izquierda con pesticida mayor o igual,
        # la planta actual sobrevive esos dias y seguimos retrocediendo.
        while stack and pesticide <= stack[-1][0]:
            days = max(days, stack[-1][1])
            stack.pop()

        if not stack:
            # No hay una planta menor a la izquierda: no muere.
            days = 0
        else:
            # Existe una planta menor a la izquierda: muere un dia despues
            # del maximo dia heredado del bloque que absorbio.
            days += 1

        max_days = max(max_days, days)
        stack.append((pesticide, days))

    return max_days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()