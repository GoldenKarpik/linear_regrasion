'''
У алгоритма градиентного спуска есть один важный недостаток, он застрявает в локальных минимумах
наприер если звять функцию sin(x)+0.5*x, то в зависимости от начальной точки, алгоритм сойдется к 1 из точек минимума
'''
import time
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)+0.5*x

def df(x):
    return np.cos(x) + 0.5

N = 20     # число итераций
xx = 0     # начальное значение или 2.5 (вообще любое, просто для 2 примера поближе ко 2 локальному минимуму)
lmd = 0.9  # шаг сходимости

x_plt = np.arange(-5.0, 5.0, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()   # включение интерактивного режима отображения графиков
fig, ax = plt.subplots()    # Создание окна и осей для графика
ax.grid(True)   # отображение сетки на графике

ax.plot(x_plt, f_plt)                   # отображение параболы
point = ax.scatter(xx, f(xx), c='red')  # отображение точки красным цветом

mn = 100
for i in range(N):
    lmd = 1/min(i+1, mn)
    xx = xx - lmd*np.sign(df(xx))    # изменение аргумента на текущей итерации

    point.set_offsets([xx, f(xx)])  # отображение нового положения точки

    # перерисовка графика и задержка на 20 мс
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()   # выключение интерактивного режима отображения графиков

print(xx)
ax.scatter(xx, f(xx), c='blue')
plt.show()