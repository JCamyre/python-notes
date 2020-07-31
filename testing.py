import os

list1 = [x for x in range(10)]
print(list1[:len(list1)-2:-1])
# start at the last element, and end at the second to last element
userandpass = {'64361565': 'Josephhpesoj12', 'mewinwin': 'Josephhpesoj12', 'goatlover239': 'Josephhpesoj12'}

for x in userandpass:
    print(x)
print(len(userandpass))

print(os.environ.get('EMAIL_PASS'))
