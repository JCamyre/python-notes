def cube(x):
	return x * x * x

# A first-class function can be assigned as a value to a variable. Note this is different from 
# a function returning a value, you are assigning the actual function as a value to a variable
f = cube
print(cube)
print(f(5))


def map_func(func, arr):
	return_arr = []
	for x in arr:
		return_arr.append(func(x))
	return return_arr


# A first-class function can be passed as an argument for another function 
print(map_func(cube, [1, 2, 3, 4, 5]))

def logger(msg):
	def log_msg():
		print(f'Log: {msg}')
	return log_msg

log = logger('Hi!')
log()

# A first-class function can be returned by another function
def html_tag(tag):
	
	def wrap_text(msg):
		print(f'<{tag}>{msg}</{tag}>')
	return wrap_text

h1_tag = html_tag('h1')
h1_tag('This is a heading')

p_tag = html_tag('p')
p_tag('This is a paragraph')

