import matplotlib.pyplot as plt
import numpy as np

def lin_plot():
    x = [1, 5, 10, 15, 20]
    y1 = [1, 5, 3, 7, 9]
    y2 = [4, 1, 3, 9, 9]
    plt.figure(figsize=(12, 7))
    plt.plot(x, y1) # отображаем 2е прямых
    plt.plot(x, y2)
    plt.legend()
    plt.grid() #отображение сетки
    plt.savefig('lin.png')

# площадь под кривой
def area_plot():
    plt.fill_between([-1, 4, 2], [2.4, 8.9, 7.5])
    plt.savefig('area.png')

# гистограмма
def hist_plot():
    data = np.random.randint(0, 100, 100)
    plt.hist(data, bins=20) # гистограмма из 20 столбцов
    plt.savefig('hist.png')

# столбчатая диаграмма
def bar_plot():
    index = np.arange(5)
    values = [3, 8, 5, 1, 0]
    plt.bar(index, values)
    plt.xticks(index +0.4, ['A', 'B', 'C', 'D', 'E'])
    plt.savefig('bar.png')

# круговая диаграмма
def pie_plot():
    values = [24, 7, 13, 40, 33]
    labels = ['a', 'b', 'f', 'r', 'e']
    plt.pie(values, labels=labels)
    plt.savefig('pie.png')

def box_plot():
    data = [24, 53, 44, 17, 20]
    plt.boxplot(data)
    plt.savefig('box.png')

pie_plot()