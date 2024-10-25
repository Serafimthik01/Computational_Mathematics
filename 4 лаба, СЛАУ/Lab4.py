import numpy as np


def lu_decomposition(A):
    n = A.shape[0]
    L = np.identity(n)
    U = A.copy()

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, :] -= factor * U[i, :]

    return L, U


def solve_lu(L, U, b):
    n = L.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)

    # Решение системы Ly = b
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

    # Решение системы Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x



def zeidel(A, b, x0, eps=1e-6, max_iter=100):
    n = A.shape[0]
    x = x0.copy()
    x1 = 0

    for k in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            s = 0
            for j in range(i):
                s += A[i, j] * x[j]
            for j in range(i + 1, n):
                s += A[i, j] * x_prev[j]
            x[i] = (b[i] - s) / A[i, i]
            x1 = x1 + 1


        if np.linalg.norm(x - x_prev) < eps:
            print(x1)
            return x



    print("Превышено максимальное число итераций.")
    return None

A = np.array([[2.57, -2.57, 3.29, 0.14],
              [0, -1, 4, 0],
              [-1, -4, 8, 1],
              [-0.29, -7.71, 4.86, 6.43]])

b = np.array([4.87, 9, 12, -2.41])

L, U = lu_decomposition(A)

x = solve_lu(L, U, b)

x2 = zeidel(A, b, x)

print("L:")
print(L)
print("\nU:")
print(U)
print("\nРешение системы:")
print(x)

if x2 is not None:
    print("Решение системы методом Зейделя:")
    print(x2)
