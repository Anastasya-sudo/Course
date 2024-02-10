t = {
    "key": 2,
    "left": {
        "key": 1
    },
    "right": {
        "key": 3
    }
}

"""find key in tree"""
def find(tree, key):
    if tree is None:
        return None

    if tree.get("key") == key:
        return tree

    if key < tree.get("key"):
        return find(tree.get("left"), key)
    else:
        return find(tree.get("right"), key)


"""left key right"""
def dfs(tree):
    if tree is None:
        return
    dfs(tree.get("left"))
    print(tree.get('key'))
    dfs(tree.get("right"))


"""bfs"""
def bfs(tree):
    if tree is None:
        return
    queue = [tree]  # Инициализируем очередь, начиная с корня
    while queue:
        node = queue.pop(0)  # Извлекаем узел из очереди
        print(node.get('key'))  # Печатаем значение текущего узла
        # Помещаем левый и правый узлы в очередь (если они существуют)
        if "left" in node:
            queue.append(node.get('left'))
        if "right" in node:
            queue.append(node.get('right'))


