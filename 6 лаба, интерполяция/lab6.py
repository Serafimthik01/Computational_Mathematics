import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def f(x):
  return np.sin(x) + x**2 - x / 20


x_points = np.array([0, np.pi/2, np.pi])
y_points = f(x_points)

cs = CubicSpline(x_points, y_points)


x_fine = np.linspace(x_points[0], x_points[-1], 1000)
y_cs = cs(x_fine)

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points, 'o', label='Точки данных')
plt.plot(x_fine, y_cs, label='Кубический сплайн')
plt.plot(x_fine, f(x_fine), label='Исходная функция')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кубический сплайн')
plt.legend()
plt.grid(True)
plt.show()