"""
迭代器, 生成器
"""

# 生成一个generator生成器对象
s = (x * x for x in range(5))
print(s)

# 循环这个generator对象
for x in s:
    print(x)


# 斐波那契（Fibonacci）數列生成， 通过yield返回一个迭代器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'


f = fib(10)
for x in f:
    print(x)


# 手动调用生成器generator
g = fib(5)
while 1:
    try:
        x = next(g)
        print("g: ", x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
