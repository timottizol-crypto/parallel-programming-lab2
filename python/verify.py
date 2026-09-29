import numpy as np
import sys

path_a = "A.txt"
path_b = "B.txt"
path_c = "C.txt"
with open(path_a, "r") as f:
    n_a = int(f.readline().strip())

with open(path_b, "r") as f:
    n_b = int(f.readline().strip())

with open(path_c, "r") as f:
    n_c = int(f.readline().strip())
A = np.loadtxt(path_a, skiprows=1)
B = np.loadtxt(path_b, skiprows=1)
C_cpp = np.loadtxt(path_c, skiprows=1)
C_correct = A @ B
if np.allclose(C_correct, C_cpp):
    print("OK")
else:
    print("FAIL")
print("Размер матрицы (A):", n_a)
print("Размер матрицы (B):", n_b)
print("Размер матрицы (C):", n_c)
print("Максимальное расхождение:", np.max(np.abs(C_correct - C_cpp)))