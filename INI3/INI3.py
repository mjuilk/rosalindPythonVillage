#Rosalind | Strings and Lists

def humpty(full, a, b, c, d):
    word1 = full[a:b + 1]
    word2 = full[c:d + 1]
    return word1 + ' ' + word2

with open('rosalind_ini3.txt', 'r') as f:
    file = f.readlines()
    bounds = [int(x) for x in file[1].split()]
    print(humpty(file[0], bounds[0], bounds[1], bounds[2], bounds[3]))