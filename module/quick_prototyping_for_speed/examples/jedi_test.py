a=100
b=30.5

for i in range(10):
    x = i + 1

def f(x):
    y, z = x, 3
    g = 5.0
    f = [0]*3
    d = "aaaaaa"
    for i in range(5):
        h = "aaaaa"+g
        z = z  + i * x
        y = y + x 
        print(i+z)

def func(a, b):
    print(a)
    a = 1
    b += a
    a = 'abc'
    return a, str(b)

class A:
    def f(self, i):
        i = 3

        
# conflict typing
def f():
    x=1
    x="aaa"

def standard_function():
    uu="aaa".upper()
    