import numpy as np

# 1. Inner Product: <a|b>
def inner_product(a, b):
    return np.vdot(a, b)

# 2. Outer Product: |a><b|
def outer_product(a, b):
    return np.outer(
        np.asarray(a).reshape(-1), np.asarray(b).reshape(-1).conj()
    )

# 3. Matrix Multiply: Zigma Aik.Bkj
def matrix_product(a, b):
    return np.matmul(a, b)

# 4. Tensor Product: |a> ⊗ |b>
def tensor_product(a, b):
    return np.kron(a, b)

'''
Use Examples
'''

A = np.array([
    [-9, 3j],
    [-1j, 7]
], dtype=complex)

B = np.array([
    [5j, 6j],
    [20, 8]
], dtype=complex)

print("Inner Product:")
print(inner_product(A[0], B[0]))

print("\nOuter Product:")
print(outer_product(A[:, 0], B[:, 0]))

print("\nMatrix Multiplication:")
print(matrix_product(A, B))

print("\nTensor Product:")
print(tensor_product(A, B))