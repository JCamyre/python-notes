my_list = [n*n for n in range(1, 11)]
print(my_list)

my_list = [n for n in range(1, 11) if n%2==0]
print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

my_dict = dict(zip('abcd', range(4)))
print(my_dict)

first_name = ['John', 'James']
last_name = ['Smith', 'Smith']

my_dict = {first: last for first, last in zip(first_name, last_name) if first != 'John'}
print(my_dict)

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
print(set(nums))
my_set = {n for n in nums if n%2==0}
print(my_set)

# When you aren't printing out the values of a generator, zero run time
my_gens = (x * x for x in range(1, 11))

# When you are, actual run time
print(list(my_gens))
for x in my_gens:
	print(x)


