a = "hello"

print(a[1])
print(a[-1])
print(a[-1 :])
print(a[1 : -1])
print(bool(1))
print(int(1.51))
print(float(True))

print("Practical Extraction and Report Language" > "Python")

thistuple = ("apple",)
print(type(thistuple))

string = ''.join('X' for i in range(78))
print(len(string))

size = 5
li = [[0] * size for _ in range(size)]
print(li)

print(8.0 / 5)
print(8 / 5)
print(8 // 5)
print(8 % 5)
print(2 ** 3)
print(round(0.5))

def abc():
    a = 1

print(abc())

class Bar(object):
    def run(self):
        print("Func")

a = Bar()
x = a.run

x()

class Test:
    var = None
    def set(self):
        self.var = 1
        
a = Test()
print(Test.var)

a.set()
print(Test.var)

a = [1, 2]
b = (1, 2)
c = [a, b]
a += [3]
b += (3,4)
print(c)

print('xy' in 'asxy')
print('xy' in ['asxy', 'abc'])

print([x for x in range(5, 0, -1) if x % 2 == 0])


for x in range (0, 5, 1):
    print(x) 


def f(a, b, *c, **d):
    print(c)
    print(d)

f(1, 2, 3, 4, c = 5, d = 6)

print(",".join(map(lambda x: str(x), (1, 3, 5))))

def Foo(n):
    def multiplier(x):
        return x * n
    return multiplier

a = Foo(5)
b = Foo(5)
print(a(b(2)))

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
def ordinary():
    print("I am ordinary")  

pretty = make_pretty(ordinary)
pretty()


address = 5

if address in range(1,10):
    print(address)

def add_to_list(value, original_list=[]):
    original_list.append(value)
    return original_list

li=add_to_list(2,[1])
print(li)
li=add_to_list(3)
print(li)
li=add_to_list(4,[7])
print(li)
li=add_to_list(5)
print(li)


import operator

def bonus():
    d = {}
    file = open('a.txt', 'r')
    lines = file.read().splitlines()

    for line in lines:
        if line not in d:
            d[line] = '1'
        else:
            d[line] = str(int(d[line]) + 1)

    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    
    for key in sorted_d:
        print(sorted_d[key] + " " + key)

bonus()

import time

def inRange():
    address = 5
    start = 0
    end = 10000
    start_time = time.time()

    if address in range (start, end):
        print("InRange--- %s seconds ---" % (time.time() - start_time))
    
def comparison():
    address = 5
    start = 0
    end = 10000
    start_time = time.time()

    if address > start and address < end:
        print("Comparison--- %s seconds ---" % (time.time() - start_time))
    
inRange()
comparison()