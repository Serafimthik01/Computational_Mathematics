import numpy as np

def f(x):
    return np.sin(x) + x**2 - x/20

def simpson_rule(a, b, n):
    if n % 2:
        raise ValueError("n должно быть чётным.")
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        weight = 4 if i % 2 else 2
        integral += weight * f(x)

    integral *= h / 3
    return integral

def integrate_with_tolerance(a, b, tol):
    n = 6
    integral_old = simpson_rule(a, b, n)
    n *= 2
    integral_new = simpson_rule(a, b, n)

    while abs(integral_new - integral_old) > tol:
        integral_old = integral_new
        n *= 2
        integral_new = simpson_rule(a, b, n)

    return integral_new, n

a = 0
b = 4
tolerance = 1e-4

result, n = integrate_with_tolerance(a, b, tolerance)
print(f"Интеграл: {result}, кол-во интервалов: {n}")
