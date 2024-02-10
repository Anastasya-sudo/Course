import math

"""tasks"""

#1
s = list(input())
print("True") if len([i for i in s if i.isdigit() ]) == len(s)/2 else print("False")

#2
s = list(input())
replaced_s = map(lambda i: '-' if i % 3 == 0 else s[i], range(len(s)))
res = ''.join(replaced_s)
print(res)

#3
s = list(input())
p = list(filter(lambda x: x.isalpha() or x.isdigit(), s))
replaced = map(lambda i: p[i].upper() if p[i].isalpha() else p[i], range(len(p)))
res = ''.join(replaced)
print(res)

#4
s = input().split()
def is_upp(a):
    return (True) if len([i for i in a if i in 'aeiouyAEIOUY']) >= 3 else (False)

#5
res = [i for i in s if is_upp(i)]
print(res)

#6
s = input().split(' ')
res = [int(i) for i in s if s.count(i) > 2]
print(res)

#7
input_str = input()
numbers = list(map(int, input_str.split()))
filtered_numbers = [num for num in numbers if any(num % other == 0 for other in numbers if num != other)]
print(filtered_numbers)

#8
def solve(l):
    return list(map(lambda x: round(math.sqrt(x), 2), filter(lambda x: x % 2 == 0, l)))
print(solve([50, 98, 6]))

#9
def is_digit(s):
    return s.isdigit()
def solve(x):
    return list(filter(lambda x: x[0].isupper() and len(list(filter(is_digit, list(x)))) == 0, x))
print(solve(['zUHfBaNV', 'VIF9x', 'OkOeLg']))

#10
def check_inheritance(l):
    return list(filter(lambda x: issubclass(l[-1], x), [l[i] for i in range(0, len(l)-1)]))
print(check_inheritance([int, str, complex, dict, bool]))

#11
def check_instance(l):
    l1 = l[0]
    x1 = l[1]
    return list(filter(lambda x: issubclass(x1, x), l1))
print(check_instance([[int, str, complex, dict, bool], True]) )

#12
s = input()
def filter_elements(input_string):
    elements = list(map(int, input_string.split()))
    counts = {x: elements.count(x) for x in set(elements)}
    result = [x for x in elements if counts[x] > 2]
    print(result)
filter_elements(s)

#13
def check_instance(input_list):
    class_list, obj = input_list[0], input_list[1]
    instance_of_classes = []
    for cls in class_list:
        if isinstance(obj, cls):
            instance_of_classes.append(cls)
    return instance_of_classes
print(check_instance([[int, str, complex, dict, bool], True]))

