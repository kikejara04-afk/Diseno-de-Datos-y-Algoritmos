#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def andXorOr(a):
    max_value = 0
    stack = []

    # En una pila creciente, el mejor candidato para cada elemento
    # aparece comparandolo con vecinos relevantes (tope de la pila).
    for value in a:
        while stack:
            max_value = max(max_value, value ^ stack[-1])

            if value < stack[-1]:
                stack.pop()
            else:
                break

        stack.append(value)

    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
