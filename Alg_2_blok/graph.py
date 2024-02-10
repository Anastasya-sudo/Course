x = [('A', 'C', 3), ('B', 'C', 2), ('A', 'B', 1)]
ufs = {
    1: 2,
    2: 4,
    3: 4,
    10: 9,
    11: 9,
}

"""сортировка вершин графа по весу"""
# 1й  вар-т
def sort_(x):
    sort_ves = []
    res = []
    for i in range(0, len(x)):
        sort_ves.append([x[i][2], i])
    sort_ves.sort()
    for i in range(0, len(x)):
        res.append(x[sort_ves[i][1]])
    return res
# 2й вар-т
def sort(x):
    sorted_edges = sorted(x, key=lambda edge: edge[2])
    return sorted_edges


"""возвращает идотнефикатор множества для заданого элемента"""
def find(ufs, key):
    if ufs.get(key) is None:
        return key
    ufs[key] = find(ufs, ufs.get(key))
    return ufs.get(key)


"""минимальное остовное дерево"""
def find(ufs, key):
    if ufs.get(key) is None:
        return key
    ufs[key] = find(ufs, ufs.get(key))
    return ufs.get(key)

def union(ufs, x, y): # объединение множеств
    root_x = find(ufs, x)
    root_y = find(ufs, y)
    ufs[root_x] = root_y

def mst(edges):
    sorted_edges = sorted(edges, key=lambda x: x[2])  # Сортировка ребер по весу
    ufs = {}  # Инициализация системы непересекающихся множеств
    mst_edges = []  # Инициализация списка ребер минимального остовного дерева

    for edge in sorted_edges:
        vertex1, vertex2, weight = edge
        if find(ufs, vertex1) != find(ufs, vertex2):
            mst_edges.append(edge)
            union(ufs, vertex1, vertex2)

    return mst_edges

# Пример использования
print(mst(x))  # Вывод: [('A', 'B', 1), ('B', 'C', 2)]




