#Rosalind | Working with Files

with open('rosalind_ini5.txt', 'r') as f:
    with open('INI5_RESULT.txt', 'w') as w:
        file = [x.strip() for x in f.readlines()]
        for x in file:
            if file.index(x) % 2 != 0:
                w.write(x + '\n')