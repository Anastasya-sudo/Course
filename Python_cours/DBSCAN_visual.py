from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN # импорт алгоритма кластеризации DBSCAN
from sklearn.decomposition import PCA # метод анализа пространства признаков
import matplotlib.pyplot as plt


if __name__ == "__main__":
    iris = load_iris()
    dbscan = DBSCAN(eps=0.5, min_samples=5) # создаем объект

    dbscan.fit(iris.data) # выполняем кластеризацию

    """кол-во осей = 2, алгоритм связанный с снижением размерности пространства признаков(метод главных компонент - pca) нужен для "привычной" визуализации"""
    pca_obj = PCA(n_components=2)
    pca_fitted = pca_obj.fit(iris.data) # производим снижение размерности пространства до 2х
    pca_2d = pca_fitted.transform(iris.data) # рез-т преобразования -> двумерный массив

    # разметка данных для последующей визуализации

    for i in range(0, pca_2d.shape[0]): # pca_2d.shape[0] - кол-во наблюдений
        if dbscan.labels_[i] == 0:
            c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+') # отрисовка точки
        elif dbscan.labels_[i] == 1:
            c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
        elif dbscan.labels_[i] == -1:
            c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

    plt.legend([c1, c2, c3], ['Cluster_1', 'Cluster_2', 'Noise'])


    plt.title('DBSCAN finds 2 clusters and noise')
    plt.savefig("plot.png")