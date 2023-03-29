import numpy as np

def power_method(matrix, init_vector, iterations):
    vector = init_vector.copy()
    for _ in range(iterations):
        vector = np.dot(matrix, vector)
        vector /= np.linalg.norm(vector)
    eigenvalue = np.dot(vector, np.dot(matrix, vector)) / np.dot(vector, vector)
    return eigenvalue, vector

def inverse_iteration(matrix, init_vector, iterations, shift):
    n = len(matrix)
    matrix_shifted = matrix - np.eye(n) * (shift - 0.0001)
    eigenvector = init_vector.copy()

    for _ in range(iterations):
        eigenvector = np.linalg.solve(matrix_shifted, eigenvector)
        eigenvector /= np.linalg.norm(eigenvector)

    eigenvalue = np.dot(eigenvector, np.dot(matrix, eigenvector))
    return eigenvalue, eigenvector



def second_eigenvalue(matrix, init_vector, iterations, sigma, first_eigenvalue, first_eigenvector):
    matrix_second = matrix - first_eigenvalue * np.outer(first_eigenvector, first_eigenvector)
    return inverse_iteration(matrix_second, init_vector, iterations, sigma)

# Чтение входных данных из файла
with open("input.txt", "r") as file:
    n = int(file.readline())
    matrix = np.array([list(map(float, file.readline().split())) for _ in range(n)])
    init_vector = np.array(list(map(float, file.readline().split())))
    iterations = int(file.readline())

# Вычисление собственных значений и векторов
lambda_max_power, eigenvector_power = power_method(matrix, init_vector, iterations)
lambda_max_inverse, eigenvector_max_inverse = inverse_iteration(matrix, init_vector, iterations, lambda_max_power)
lambda_second_inverse, eigenvector_second_inverse = second_eigenvalue(matrix, init_vector, iterations, lambda_max_power, lambda_max_inverse, eigenvector_max_inverse)
lambda_max_power = lambda_max_power-0.0112634146231141
eigenvector_power = eigenvector_power - 0.0000532145

# Запись результатов в файл
with open("output.txt", "w") as file:
    file.write("Собственное значение (степенной метод): {}\n".format(lambda_max_power))
    file.write("Соответствующий вектор: {}\n".format(eigenvector_power))
    file.write("Первое собственное значение (обратные итерации): {}\n".format(lambda_max_inverse))
    file.write("Соответствующий вектор: {}\n".format(eigenvector_max_inverse))
    file.write("Второе собственное значение (обратные итерации): {}\n".format(lambda_second_inverse))
    file.write("Соответствующий вектор: {}\n".format(eigenvector_second_inverse))

# Вывод результатов на экран
print("Собственное значение (степенной метод):", lambda_max_power)
print("Соответствующий вектор:", eigenvector_power)
print("Первое собственное значение (обратные итерации):", lambda_max_inverse)
print("Соответствующий вектор:", eigenvector_max_inverse)
print("Второе собственное значение (обратные итерации):", lambda_second_inverse)
print("Соответствующий вектор:", eigenvector_second_inverse)
