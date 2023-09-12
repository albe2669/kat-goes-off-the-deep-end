MOD = 1_000_000_007


def multiply_matrices(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += (a[i][k] * b[k][j]) % MOD
                c[i][j] %= MOD
    return c


def matrix_power(matrix, n):
    if n <= 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return multiply_matrices(half_pow, half_pow)
    else:
        return multiply_matrices(matrix, matrix_power(matrix, n - 1))


def fibonacci(n):
    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n)
    return result[0][0]


print(fibonacci(int(input()) + 1) - 1)
