from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN # импорт класса DBSCAN

iris = load_iris()
dbscan = DBSCAN(eps=0.5, min_samples=5) # создаем объект

dbscan.fit(iris.data) # вызываем у объекта метод

print(dbscan.labels_) # выводим полученные метки