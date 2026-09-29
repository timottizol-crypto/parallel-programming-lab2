import random
import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input("Размер: "))

matrix = []
for a in range(n):
    row = []
    for i in range(n):
        x = random.randint(0,100)
        row.append(x)
    matrix.append(row)
f = open("../data/A.txt" , "w")
f.write(str(n) + "\n")
for row in matrix:
    line = " ".join(str(x) for x in row)
    f.write(line + "\n")
f.close()

matrix_b = []
for i in range(n):
    row_b = []
    for a in range(n):
        b = random.randint(0,100)
        row_b.append(b)
    matrix_b.append(row_b)
h = open("../data/B.txt" ,"w")
h.write(str(n) + "\n")
for row_b in matrix_b:
    line = " ".join(str(b) for b in row_b)
    h.write(line + "\n")
h.close()
