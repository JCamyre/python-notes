from dis import dis

a = lambda x: x + 1
print(a(1))

print((lambda x: x + 1)(1))

high_ord_func = lambda x, func: x + func(x)
square = lambda x: x ** 2
print((high_ord_func)(4, square))

high_ord_func2 = lambda x, func: x + func(x)
print((high_ord_func2)(4, lambda x: x ** 2))
print(dis(high_ord_func2))
print(type(high_ord_func2))


def add_square(x): x + x ** 2


print(add_square(4))
print(type(add_square))

print(25 % 2 and 'odd' or 'even')

arr = 'This is a typing test with the logitech g710 keyboard with cherry mx blue switches.'

print(sorted(arr.split(), key=lambda x: len(x)))

arr = list(range(10))
for i in arr:
	print((lambda x: True if x > 5 else False)(i))
