from sklearn.datasets import load_iris
import pandas as pd
import random
import numpy as np

"""класс Series"""

my_series = pd.Series(
[random.randint(0, 10) for _ in range(5)],
index=['a', 'b', 'c', 'd', 'e'])
#print('--1--\n', my_series.head()) # вывод на экран первых 5 строк
#print('--2--\n', my_series[['a', 'c', 'e']]) # обращение по индексам
#print('--3--\n', my_series.max())
#print('--4--\n', my_series.min())
#print('--5--\n', my_series.mean())


"""класс DataaFrame"""

# вывод
def get_info_df(dataframe):
    print(dataframe.head())
    print(dataframe['target'].unique()) # уникальные значения из столбца target
    print(dataframe[['target', 'sepal width (cm)', 'petal width (cm)']]) # выводим столбцы
    print(dataframe.loc[[54, 55, 56], 'target']) # извлечение данных по метке
    print(dataframe.iloc[0:10])
    print(dataframe.loc[0:10])

# вывод с условтем
def get_info_ysl(dataframe):
    setosa = dataframe[dataframe['target'] == 0.0]
    versicolor = dataframe[dataframe['target'] == 1.0]
    verginica = dataframe[dataframe['target'] == 2.0]
    return setosa, versicolor, verginica

# группирует данные (группировка по столбцу target)
def group_by_df(dataframe):
    pass
    #print(dataframe.groupby('target').size())
    #print(dataframe.groupby('target')['sepal width (cm)'].mean())
    #print(dataframe.groupby('target')['sepal width (cm)'].min())

iris = load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names']+['target'])

get_info_df(df)
#print('\n')
#print(get_info_ysl(df))
group_by_df(df)

"""набор данных создается при помощи словарей"""

df = pd.DataFrame({'first': [1, 2, 3],
                   'second': [5, 6, 7],
                   'third': [7, 8, 9]})

df1 = pd.DataFrame({'f': [-1, -2, -3],
                   's': [5, 6, 7],
                   't': [7, 8, 9]})

#df_res = df.append(df1, ignore_index=True) # concot
#df_res.loc[len(df_res.index)] = [22, 33, 44] # add new

#print(df)
#'\n'
#print(df1)

