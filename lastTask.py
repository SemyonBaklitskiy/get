import numpy as np
import matplotlib.pyplot as plot

with open("settings.txt", "r") as settings: 
    tmp = [float(i) for i in settings.read().split("\n")]

set_array = np.loadtxt("settings.txt", dtype = float)
data_array = np.loadtxt("data.txt", dtype = int)

fig, ax = plot.subplots(figsize = (16, 11), dpi = 200)


data_array = data_array * set_array[0]
y = data_array
x = [0] * 898

for i in range(898):
    x[i] = i * set_array[1]

t_charge = np.argmax(data_array)
t_charge = t_charge * set_array[1]
t_down = (898 - np.argmax(data_array)) * set_array[1]
plot.title("Процесс заряда и разряда конденсатора в RC - цепочке", color = 'green') # заголовок
ax.grid(color = "blue",    #  цвет линий
        linewidth = 0.45,    #  толщина
        linestyle = 'dashed')
ax.minorticks_on()
ax.grid(which='minor',
        color = 'orange',
        linewidth = 0.25,
        linestyle = 'dashed')
plot.plot(x, y, '-b', label='Зависимость', markevery=50, marker = "s")
plot.legend()
ax.set_xlabel('Время t (с)')
ax.set_ylabel('Напряжение U (В)')
plot.text(6, 1.5, 'время зарядки %f' % t_charge, fontsize=10)
plot.text(6, 2, 'время разрядки %f' % t_down, fontsize=10)
print(t_charge)
print(t_down)

plot.xlim (0, 10)
plot.ylim (0, 3.5)

plot.text(0, 8, 'время зарядки %f' % t_charge, fontsize=500)

fig.savefig("png.svg")
plot.show()