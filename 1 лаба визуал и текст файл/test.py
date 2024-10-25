import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x) + x ** 2 - x / 20


x = np.arange(-1000, 1000, 0.0001)

y = f(x)

plt.plot(x, y)

plt.grid(True)

plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Laba 1, 2 part

# import matplotlib.pyplot as plt
# import numpy as np
#
# def create():
#     with open("data.txt", "w") as file:
#         for i in range(5):
#             x = i
#             y = i**2
#             file.write(x, y, "\n")
#
# def read_data(filename):
#     x_data = []
#     y_data = []
#     with open(filename, 'r') as file:
#         for line in file:
#             x, y = map(float, line.split())
#             x_data.append(x)
#             y_data.append(y)
#         return np.array(x_data), np.array(y_data)
# #
# filename = input("Введите имя файла: ")
#
# try:
#     x, y = read_data(filename)
# except FileNotFoundError:
#     print("Файл не найден")
#
# # def f(x):
# #     return np.sin(x) + x ** 2 - x/20
#
#
# # y = f(x)
#
# plt.plot(x,y)
#
# plt.grid(True)
#
# # plt.xlim(-2, 2)
# # plt.ylim(-2, 10)
#
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("График функции")
#
# plt.show()
