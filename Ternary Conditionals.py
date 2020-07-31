condition1 = True
if condition1:
    x = 1
else:
    x = 0
print(x)

condition2 = True
y = 1 if condition2 else 0
print(y)

z = condition2 or condition1 or False
print(z)

