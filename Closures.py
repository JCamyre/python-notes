def outer_func(msg):
	message = msg

	def inner_func():
		print(message)

	return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

# Now these act just like the inner_func(), and still have the message variable remembered from the local scope of the the outer_func
hi_func()
hello_func()

def html_tag(tag):
	def wrapper(text):
		print(f'<{tag}>{text}</{tag}>')
	return wrapper

h1_tag = html_tag('h1')

# Wow it remembered the 'h1' that we passed, so interesting!
h1_tag('This is a heading')


