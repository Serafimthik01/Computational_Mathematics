import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) + x ** 2 - x / 20


def df(x):
    return np.cos(x) + 2 * x - 1 / 20


def ddf(x):
    return -np.sin(x) + 2


def newton(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_prev = x
        x = x - df(x) / ddf(x)
        if abs(x - x_prev) < tol:
            break
    return x


x0 = 0.5

min_x = newton(x0)

print("Минимум функции:", min_x)

x = np.linspace(-100, 100, 2000)
plt.plot(x, f(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции sin(x) + x^2 - x/20")
plt.scatter(min_x, f(min_x), color="red", label="Минимум функции")
plt.legend()
plt.grid(True)
plt.show()
