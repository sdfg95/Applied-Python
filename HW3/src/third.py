import numpy as np


class HashCacheMixin:
    def __hash__(self):
        hash_value = sum((i + 1) * (j + 1) * val for i, row in enumerate(self.data) for j, val in enumerate(row))
        return int(hash_value)


class Matrix(HashCacheMixin):
    _cache = {}

    def __init__(self, data):
        self.data = tuple(map(tuple, data))

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Wrong matrix dimensions. Matrices must have the same shape")

        return Matrix([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])

    def __mul__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Wrong matrix dimensions. Matrices must have the same shape")

        return Matrix([[a * b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])

    def __matmul__(self, other):
        hash_val = hash(self) + hash(other)
        if hash_val in Matrix._cache:
            return Matrix._cache[hash_val]

        if len(self.data[0]) != len(other.data):
            raise ValueError("Wrong matrix dimensions. Matrices must have the same shape")

        result = Matrix([[sum(a * b for a, b in zip(row, col)) for col in zip(*other.data)] for row in self.data])

        Matrix._cache[hash_val] = result
        return result

    def __str__(self):
        return '\n'.join(' '.join('{:4}'.format(item) for item in row) for row in self.data)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join('{:4}'.format(item) for item in row) + '\n')


def find_matrices_with_same_hash(matrix_size):
    hash_to_matrices = {}

    while True:
        matrix1 = np.random.randint(1, 100, size=(matrix_size, matrix_size))
        matrix2 = np.random.randint(1, 100, size=(matrix_size, matrix_size))

        matrix1_obj = Matrix(matrix1)
        matrix2_obj = Matrix(matrix2)

        hash1 = hash(matrix1_obj)
        hash2 = hash(matrix2_obj)

        if hash1 == hash2 and matrix1_obj.data != matrix2_obj.data:
            return matrix1_obj, matrix2_obj


matrix_size = 3
matrix1, matrix2 = find_matrices_with_same_hash(matrix_size)
print("Первая матрица и хеш:")
print(matrix1.data)
print(hash(matrix1))
print("Вторая матрица и хеш:")
print(matrix2.data)
print(hash(matrix2))

A_obj = matrix1
C_obj = matrix2

b = np.random.randint(1, 100, size=(matrix_size, matrix_size))
B_obj = Matrix(b)
D_obj = Matrix(b.copy())

AB = A_obj @ B_obj
CD = C_obj @ D_obj

A_obj.save_to_file("../artifacts/3.3/A.txt")
B_obj.save_to_file("../artifacts/3.3/B.txt")
C_obj.save_to_file("../artifacts/3.3/C.txt")
D_obj.save_to_file("../artifacts/3.3/D.txt")
AB.save_to_file("../artifacts/3.3/AB.txt")
CD.save_to_file("../artifacts/3.3/CD.txt")

with open("../artifacts/3.3/hash.txt", "w") as f:
    f.write(f"hash(AB): {hash(AB)}\n")
    f.write(f"hash(CD): {hash(CD)}\n")
    f.write(f"hash(A): {hash(A_obj)}\n")
    f.write(f"hash(C): {hash(C_obj)}\n")
    f.write(f"hash(B): {hash(B_obj)}\n")
    f.write(f"hash(D): {hash(D_obj)}\n")
