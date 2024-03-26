import numpy as np


class Matrix:
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
        if len(self.data[0]) != len(other.data):
            raise ValueError("Wrong matrix dimensions. Matrices must have the same shape")
        return Matrix([[sum(a * b for a, b in zip(row, col)) for col in zip(*other.data)] for row in self.data])

    def __str__(self):
        return '\n'.join(' '.join('{:4}'.format(item) for item in row) for row in self.data)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join('{:4}'.format(item) for item in row) + '\n')


np.random.seed(0)
matrix1 = np.random.randint(0, 10, (10, 10))
matrix2 = np.random.randint(0, 10, (10, 10))

obj1 = Matrix(matrix1)
obj2 = Matrix(matrix2)

result_add = obj1 + obj2
result_element_mul = obj1 * obj2
result_matrix_mul = obj1 @ obj2

obj1.save_to_file("../artifacts/3.1/matrix1.txt")
obj2.save_to_file("../artifacts/3.1/matrix2.txt")
result_add.save_to_file("../artifacts/3.1/matrix+.txt")
result_element_mul.save_to_file("../artifacts/3.1/matrix*.txt")
result_matrix_mul.save_to_file("../artifacts/3.1/matrix@.txt")
