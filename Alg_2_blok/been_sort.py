"""
arr = [1, 3, 5]
print(binary_search(arr, 1, 0, len(arr) - 1) == 0)
print(binary_search(arr, 3, 0, len(arr) - 1) == 1)
print(binary_search(arr, 5, 0, len(arr) - 1) == 2)
print(binary_search(arr, 0, 0, len(arr) - 1) == -0 - 1)
print(binary_search(arr, 2, 0, len(arr) - 1) == -1 - 1)
print(binary_search(arr, 4, 0, len(arr) - 1) == -2 - 1)
print(binary_search(arr, 6, 0, len(arr) - 1) == -3 - 1)
"""
"""binary_search"""
def binary_search(x, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        cur = x[mid]
        if cur == key:
            return mid
        if cur > key:
            end = mid - 1
        else:
            start = mid + 1
    return start
    # return -(start) - 1 # если эл-т не найден


"""swap elem on new index"""
def swap(x, old, new):
    element = x.pop(old)
    x.insert(new, element)
    return x


"""bin sort"""
def sort(x):
    for i in range(1, len(x)):
        pos = binary_search(x[:i], x[i], 0, len(x[:i]) - 1)
        x[:i+1] = swap(x[:i+1], i, pos)
    return x


