first_name = ['Joseph', 'Alex', 'Gurkaran', 'Chris', 'Erich']
middle_name = ['W', 'idk', 'idk', 'idk', 'idk']
last_name = ['Camyre', 'Shan', 'Singh', 'Luo', 'Bahm']

for first, middle, last in zip(first_name, middle_name, last_name):
    print(f'{first} {middle} {last}')

for x in zip(first_name, middle_name, last_name):
    print(x)
