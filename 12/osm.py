import math

# Function to solve the linear system (A - sigma*I)y = x using power iteration method
def solve_system(A, x, num_iterations):
    for i in range(num_iterations):
        y = [0] * len(A)
        for i in range(len(A)):
            for j in range(len(x)):
                y[i] += A[i][j] * x[j]
        x = [0] * len(A)
        norm_y = norm(y)
        for i in range(len(A)):
            x[i] = y[i] / norm_y
    return x

# Function to find the norm of a vector
def norm(x):
    return math.sqrt(sum(x[i] ** 2 for i in range(len(x))))

# Function to normalize a vector
def normalize(x):
    return [x[i] / norm(x) for i in range(len(x))]

# Function to perform power iteration algorithm
def power_iteration(A, x, num_iterations, epsilon):
    n = len(A)
    lambda_old = 0
    for i in range(num_iterations):
        y = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
        x = normalize(y)
        lambda_new = sum(x[i] * (A[i][j] * x[j]) for i in range(n) for j in range(n))
        if abs(lambda_new - lambda_old) < epsilon:
            break
        lambda_old = lambda_new
    return lambda_new, x, i + 1

# Function to perform the inverse iteration algorithm
def inverse_iteration(A, x, sigma, num_iterations, epsilon):
    n = len(A)
    lambda_old = 0
    for i in range(num_iterations):
        y = solve_system([[A[i][j] - sigma * (i == j) for j in range(n)] for i in range(n)], x, num_iterations)
        x = normalize(y)
        lambda_new = sum(x[i] * (A[i][j] * x[j] - sigma * (i == j) * x[j]) for i in range(n) for j in range(n))
        if abs(lambda_new - lambda_old) < epsilon:
            break
        lambda_old = lambda_new
    return lambda_new, x, i + 1

# Read the input from input.txt
with open('input.txt', 'r') as file:
    # Read the matrix A
    n = int(file.readline())
    A = []
    for i in range(n):
        row = list(map(int, file.readline().split()))
        A.append(row)
    # Read the vector x
    x = list(map(int, file.readline().split()))
    # Read the number of iterations
    num_iterations = int(file.readline())

# Find the eigenvalue and eigenvector using power iteration
eigenvalue_power, eigenvector_power = power_iteration(A, x, num_iterations)

# Find the first eigenvalue and eigenvector using inverse iteration
sigma = 0.1
eigenvalue1_inverse, eigenvector1_inverse = inverse_iteration(A, x, sigma, num_iterations)

# Shift the matrix A to find the second eigenvalue and eigenvector using inverse iteration
sigma = eigenvalue1_inverse + 0.1
eigenvalue2_inverse, eigenvector2_inverse = inverse_iteration(A, x, sigma, num_iterations)


# Write the output to output.txt and print it to the console
with open('output.txt', 'w') as file:
    file.write("Power iteration eigenvalue: {}\n".format(eigenvalue_power))
    file.write("Power iteration eigenvector: {}\n".format(eigenvector_power))
    file.write("First inverse iteration eigenvalue: {}\n".format(eigenvalue1_inverse))
    file.write("First inverse iteration eigenvector: {}\n".format(eigenvector1_inverse))
    file.write("Second inverse iteration eigenvalue: {}\n".format(eigenvalue2_inverse))
    file.write("Second inverse iteration eigenvector: {}\n".format(eigenvector2_inverse))

print("Power iteration eigenvalue:", eigenvalue_power)
print("Power iteration eigenvector:", eigenvector_power)
print("First inverse iteration eigenvalue:", eigenvalue1_inverse)
print("First inverse iteration eigenvector:", eigenvector1_inverse)
print("Second inverse iteration eigenvalue:", eigenvalue2_inverse)
print("Second inverse iteration eigenvector:", eigenvector2_inverse)