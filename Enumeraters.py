names = ['Joe', 'Jeff', 'James']
index = 0

for name in names:
    print(index, name)
    index += 1
print('*' * 40)
# vs
for index in range(len(names)):
    print(index, names[index])
print('*' * 40)
# vs
for index, name in enumerate(names, start=0):
    print(index, name)

