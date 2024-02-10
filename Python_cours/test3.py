import numpy as np
from sklearn.datasets import load_iris # набор данных
from sklearn.preprocessing import StandardScaler # для нормализации данных

from sklearn import preprocessing
import pandas as pd


"""z - нормализация"""

dataset = load_iris()

scaler = StandardScaler() # объект класса
i_data = dataset.data # извлекаем данные из датасета

# выполняем стандартизацию

scale = scaler.fit_transform(i_data)
#print(scale)


"""минимаксная нормализация"""
data = pd.read_csv("fail")
scaler_1 = preprocessing.MinMaxScaler() # объект нормализатора

names = data.columns # извлекаем из датасета название столбцов
scaled_data = scaler_1.fit_transform(data) # вызываем нормализацию у объекта

scaled_df = pd.DataFrame(scaled_data, columns=names) # создаем DataFrame на основе нормализованых данных
#print(scaled_df.head()) # выводи голову DataFrame (1e 5 строк)


"""tasks"""

l = [[ 9, -4], [10, 6], [-9, 3]]

#1
def create_matrix(l):
    return np.array(l)
#print(create_matrix(l))

#2
def get_info(l):
    return l.shape
#print(get_info(create_matrix(l)))

#3
def solve_system(m, v):
    return np.linalg.solve(m, v)

#4
def line_sum(l):
    return np.sum(l, axis=1)
#print(type(line_sum(l)))

#5
def vsum_array(l):
    return np.sum(l, axis=0)

#6
def max_array(l):
    return np.max(l)

#7
def mean_array(l):
    return round(np.mean(l), 2)

#8
def cos_array(matrix):
    rows, cols = matrix.shape
    result = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            angle_deg = matrix[i, j]
            cos_value = np.cos(angle_deg)
            result[i, j] = round(cos_value, 2)

    return result
#print(cos_array(create_matrix(l)))

#9
def cov_array(vector):
    cov_matrix = np.cov(vector, )
    rows, cols = cov_matrix.shape
    result = np.zeros((rows, cols), dtype=float)

    for i in range(rows):
        for j in range(cols):
            cov_value = cov_matrix[i, j]
            result[i, j] = round(cov_value, 2)

    return result
#print(cov_array(create_matrix(l)))