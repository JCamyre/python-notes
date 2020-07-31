class Person(object):
    pass


joseph = Person()

# first_key = 'first'
# first_value = 'Joseph'
#
# setattr(joseph, first_key, first_value)  # U CAN SET ATTRIBUTES USING VARIABLES!q!!@!!!
#
# print(getattr(joseph, first_key))

person_info = {'first': 'Joseph', 'last': 'Camyre'}

for key, value in person_info.items():
    setattr(joseph, key, value)

print(joseph.first)
print(joseph.last)

for key in person_info.keys():
    print(getattr(joseph, key))

print(person_info.items())
print(person_info.keys())
