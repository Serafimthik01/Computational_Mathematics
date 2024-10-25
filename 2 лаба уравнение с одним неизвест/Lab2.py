import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) + x ** 2 - x / 20


def dichotomy_method(a, b, eps):
    while (b - a) > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


a = -1
b = 0.5
eps = 0.0001
root1 = dichotomy_method(a, b, eps)
print(f"Первый корень функции f(x) = sin(x) + x^2 - x/20 в интервале [{a}, {b}] с точностью {eps}: {root1}")

a = -0.5
b = 1
eps = 0.0001
root2 = dichotomy_method(a, b, eps)
print(f"Второй корень функции f(x) = sin(x) + x^2 - x/20 в интервале [{a}, {b}] с точностью {eps}: {root2}")

x = np.linspace(-3, 3, 2000)
y = f(x)
plt.plot(x, y, label='f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Функция f(x) и ее корни')
if root1 is not None:
    plt.scatter(root1, f(root1), color='green', label='Первый корень')
if root2 is not None:
    plt.scatter(root2, f(root2), color='red', label='Второй корень')
plt.legend()
plt.grid(True)
plt.show()
