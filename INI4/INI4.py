#Rosalind | Conditions and Loops

def oddSum(a, b):
    sum = 0
    for x in range(a, b):
        if x % 2 != 0:
            sum += x
    if b % 2 != 0:
        sum += b
    return sum

with open('rosalind_ini4.txt', 'r') as file:
    f = [int(x) for x in file.read().split()]
    print (oddSum(f[0], f[1]))    