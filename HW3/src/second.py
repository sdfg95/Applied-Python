import numpy as np


class NumpyMixin(np.lib.mixins.NDArrayOperatorsMixin):
    def __add__(self, other):
        return MatrixOperations(self.value + other.value)

    def __mul__(self, other):
        return MatrixOperations(self.value * other.value)

    def __matmul__(self, other):
        return MatrixOperations(self.value @ other.value)

    def __str__(self):
        return '\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in self.value])

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.value:
                file.write(' '.join(['{:6}'.format(item) for item in row]) + '\n')


class MatrixOperations(NumpyMixin):
    def __init__(self, data):
        self.value = data

    def get_matrix(self):
        return self.value

    def set_matrix(self, new_matrix):
        self.value = new_matrix


np.random.seed(0)
matrix1 = np.random.randint(0, 10, (10, 10))
matrix2 = np.random.randint(0, 10, (10, 10))

matrix_obj1 = MatrixOperations(matrix1)
matrix_obj2 = MatrixOperations(matrix2)

result_add = matrix_obj1 + matrix_obj2
result_mul = matrix_obj1 * matrix_obj2
result_elementwise = matrix_obj1 @ matrix_obj2

result_add.save_to_file("../artifacts/3.2/matrix+.txt")
result_mul.save_to_file("../artifacts/3.2/matrix_multiply*.txt")
result_elementwise.save_to_file("../artifacts/3.2/matrix_elementwise@.txt")
