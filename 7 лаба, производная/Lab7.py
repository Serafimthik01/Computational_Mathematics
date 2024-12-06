import numpy as np
import matplotlib.pyplot as plt

# Определение функции и её производной
def f(x):
    return np.sin(x) + x**2 - x/20

def f_prime(x):
    return np.cos(x) + 2*x - 1/20

# Численное вычисление производной
def derivative_2nd_order(f, x0, h):
    return (f(x0 + h) - f(x0 - h)) / (2 * h)

def derivative_4th_order(f, x0, h):
    return (f(x0 - 2*h) - 8*f(x0 - h) + 8*f(x0 + h) - f(x0 + 2*h)) / (12 * h)

# Пример вычисления производной в точке x0
x0 = 1.0
h = 0.1

deriv_2nd = derivative_2nd_order(f, x0, h)
deriv_4th = derivative_4th_order(f, x0, h)
analytical_deriv = f_prime(x0)

print(f"Аналитическая производная в точке {x0}: {analytical_deriv}")
print(f"Численная производная 2-го порядка: {deriv_2nd}")
print(f"Численная производная 4-го порядка: {deriv_4th}")

# Оценка точности по формулам Рунге
h2 = h / 2
deriv_2nd_h2 = derivative_2nd_order(f, x0, h2)
deriv_4th_h2 = derivative_4th_order(f, x0, h2)

error_2nd = abs(deriv_2nd - analytical_deriv)
error_4th = abs(deriv_4th - analytical_deriv)

print(f"Погрешность 2-го порядка: {error_2nd}")
print(f"Погрешность 4-го порядка: {error_4th}")

# Уточнение точности по формулам Рунге
improved_deriv_2nd = (4 * deriv_2nd_h2 - deriv_2nd) / 3
improved_error_2nd = abs(improved_deriv_2nd - analytical_deriv)

print(f"Уточненная производная 2-го порядка: {improved_deriv_2nd}")
print(f"Уточненная погрешность 2-го порядка: {improved_error_2nd}")

# Построение графиков
x = np.linspace(-10, 10, 400)
y = f(x)
y_prime = f_prime(x)

plt.figure(figsize=(12, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, y_prime, label="f'(x)", linestyle='--')
plt.scatter([x0], [f(x0)], color='red', label=f'f({x0})')
plt.scatter([x0], [f_prime(x0)], color='orange', label=f"f'({x0})")
plt.legend()
plt.title('Графики функции f(x) и её производной f\'(x)')
plt.grid(True)
plt.show()
