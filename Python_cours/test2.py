import math
from math import pi

"""filter/map/zip"""

a = ['ean', 'rrr']
l = [1, 2, 3, 4, 5, 6, 7, 9]

def do_filter(l):
    return list(filter(lambda x: x % 2 != 0, l))

def do_map(l):
    return list(map(lambda x: x + 2, l))

def create_pairs(a):
    return dict(zip(a[0], a[1]))

def do_lambda(l):
    return list(map(lambda y: y**2, filter(lambda x: x % 2 == 0, l)))


""" пример по ооп с  функциональным прогр
list for int
при добавлении других типов - выбросить исключение TypeError
вывод на экран через ;
длина - кол-во четных эл-в
"""
class MyList(list):
    def __init__(self):
        super(MyList, self).__init__() # обращение к конструктору класса родителя

    def __str__(self):
        return ";".join(list(map(str, self))) # join ожтдает на вход итерируемый объ., с помощью map гарантируем, что все эл-ы списка - строки (тк join)

    def __len__(self):
        return len(list(filter(lambda x: x % 2, self))) # self - объ нашего списка

    def append(self, item): # переопределяем метод
        if type(item) is int:
            super().append(item) # обращаемся к методу род класса
        else:
            raise TypeError('not int')
        
        
L = MyList()
L.append(1)
L.append(2)
L.append(3)
L.append(4)

try:
    L.append('e')
    print(L)
except TypeError as error: # обработка искл
    print(error)


"""
Напишите класс MyList, который наследуется от встроенного класса list.
Перепределите метод append так, чтобы в список попадали только числа.
"""
class MyList(list):
    def __init__(self):
        super(MyList, self).__init__()
    def append(self, item):
        if isinstance(item, (int, float)):
            super().append(item)
L1= MyList()
L1.append(1.0)
L1.append(2)
L1.append(3)
L1.append('y')


"""
Напишите класс MyStr, который наследуется от встроенного класса str.
Переопределите метод __len__ так, чтобы количество строки вычислялось как количество цифр в ней.
"""
class MyStr(str):
    def __init__(self, s):
        self.s = s
        super(MyStr, self).__init__()
    def __len__(self):
        digit_count = sum(1 for char in self.s if char.isdigit())
        return digit_count
L = MyStr('5ty7f')


"""
Напишите класс MyList, который наследуется от встроенного класса list.
Переопределите метод __len__() так, чтобы в качестве длины списка возвращалось количество чисел в нем.
"""
class MyList(list):
    def __init__(self):
        super(MyList, self).__init__()
    def __len__(self):
        return sum(1 for i in self if isinstance(i, (int, float)))
L2 = MyList()
L2.append(1)
L2.append(3.0)
L2.append('r')


"""tasks"""
def solve(l):
    return list(map(lambda x: round(math.sqrt(x), 2), filter(lambda x: x % 2 == 0, l)))

def is_digit(s):
    return s.isdigit()

def solve1(strings):
    return list(filter(lambda string: len(list(filter(is_digit,list(string)))) >= 3, strings))

strings = ["abc12", "def456", "ghi789", "jk777l", "mno12345"]
result = solve1(strings)

def solve2(x):
    return list(filter(lambda x: x[0].isupper() and len(list(filter(is_digit, list(x)))) == 0, x))

strings = ["Rabc", "def", "Ughi", "jk777l", "mno12345"]
result = solve2(strings)


"""output"""
class Circle:
    def __init__(self, radius=round(pi, 2), center=(0, 0)):
        self.radius = radius
        self.center = center
    def __str__(self):
        res = 'Circle: radius=' + str(self.radius) + ';' + ' center=' + str(self.center)
        return res
C = Circle()
#print(C)


