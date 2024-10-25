import numpy as np


def zeidel(A, b, x0, eps=1e-6, max_iter=1000):  # Увеличили max_iter до 1000
    """
    Решает систему линейных уравнений Ax = b методом Зейделя.

    Args:
        A: Матрица коэффициентов.
        b: Вектор правой части.
        x0: Начальное приближение решения.
        eps: Точность решения.
        max_iter: Максимальное количество итераций.

    Returns:
        Вектор решения x или None, если не достигнута сходимость.
    """

    n = A.shape[0]
    x = x0.copy()

    for k in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            s = 0
            for j in range(i):
                s += A[i, j] * x[j]
            for j in range(i + 1, n):
                s += A[i, j] * x_prev[j]
            x[i] = (b[i] - s) / A[i, i]

        if np.linalg.norm(x - x_prev) < eps:
            return x

    print("Превышено максимальное число итераций.")
    return None


# Пример использования

A = np.array([[2.57, -2.57, 3.29, 0.14],
              [0, -1, 4, 0],
              [-1, -4, 8, 1],
              [-0.29, -7.71, 4.86, 6.43]])

b = np.array([4.87, 9, 12, -2.41])

# Используем решение LU-разложения как начальное приближение
L, U = lu_decomposition(A)
x0 = solve_lu(L, U, b)

x = zeidel(A, b, x0)

if x is not None:
    print("Решение системы методом Зейделя:")
    print(x)

