n1 = [2,1,2,3,4]
def div_conq(n1):
    low = 0
    high = len(n1)
    while low < high:
        mid = high // 2
        if n1[mid] > n1[mid +1]:
            low = n1[mid + 1]
        else:
            high = n1[mid]
    return n1[low]
def main():
    print(f"{div_conq(n1)}")
main()