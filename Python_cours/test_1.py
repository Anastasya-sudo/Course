"""dict"""

a = {
    "a":7,
    "w":8,
    "c":9,
    "b":6,
}

a[0] = "rrr"
a.update([(2, "tu"), (3, "three")])
a.update([(2, "dva")])
#print(a.pop("a"))
a.popitem()
#print(a.get("w"))

#print(dict.fromkeys(["a", "b"], 100))
a = input()

b = [b.strip() for b in a.split(" ")]
c = {}
for i in b:
    c[i] = True
#print(c)

a = ["a", "b", "c"]
for i in enumerate(a):
    print(i)

for x, y in enumerate(a):
    print(x, y)

"""matrix"""
m = [[0 for i in range(3)] for i in range(3)] # 3*3

"""generator"""
t = [i for i in range(10) if x % 2 == 0] # only chet

"""dict"""
#print({x: ord(x) for x in "QWer"})#{'Q': 81, 'W': 87, 'e': 101, 'r': 114}

d = {}
for i in "QWert":
    d.update({i: ord(i)})

"""set"""
r = {i for i in range(10)}

"""tuple"""
T = tuple(i for i in range(10))

"""dict"""
L = {key: value for key, value in enumerate(['a', 'b', 'c'])}#{0: 'a', 1: 'b', 2: 'c'}"""



b = [b.strip() for b in input().split("\t")]
r = []
for i in range(len(b)):
    r.append(b.count(b[i]))
#print(max(r))


r= {}
for i in input().split("\t"):
    s = i.strip()
    r[s] = 1 if r.get(s) is None else r[s] + 1
#print(max(r.values()))

d = {}
a = [i.strip() for i in input().split(" ")]
for i in a:
    d.update([(i, ord(i))])
#print(d)

def f(a, b):
    return a, b # возвращает коллекцию, если в рктерн > 1 pyfxtybz
a, b = f(3, 5)
#print(a)
#print(b)

"""global/local"""
def g():
    global d
    d += 10
    #print(d)
d = 20
g()

