#Rosalind | Dictionaries

with open('rosalind_ini6.txt', 'r') as f:
    file = f.read().split()
    unifile = set(file)
    words = dict()
    for x in unifile:
        words[x] = file.count(x)
    for i in words:
        print (i, str(words[i]))