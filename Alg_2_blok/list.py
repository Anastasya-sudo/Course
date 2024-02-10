x = (1, (2, (3, (4, (5, None)))))
y = (1, 5)

"""output list"""
def iter(x):
    while x is not None:
        print(x[0])
        x = x[1]


"""insert in first pos"""
def prepend(number, lst):
    new_node = (number, lst)
    return new_node


"""reverse list"""
def reverse(x):
    prev = None
    current = x
    while current is not None:
        value = current[0]
        rest = current[1]
        current = rest
        reversed_node = (value, prev)
        prev = reversed_node
    return prev


