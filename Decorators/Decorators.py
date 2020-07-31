from functools import wraps 

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print(f'wrapper executed this before {original_function.__name__}')
		return original_function(*args, **kwargs)
	return wrapper_function

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		logging.info(
			f'Ran with args: {args}, and kwargs {kwargs}')
		print(f'Ran with args: {args}, and kwargs {kwargs}')
		return orig_func(*args, **kwargs)
	return wrapper
	

def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		# run the function, return the result later
		ran_func = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print(f'{orig_func.__name__} ran in {t2} seconds')
		return ran_func

	return wrapper


# class decorator_class(object):
# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print(f'call method executed this before {self.original_function.__name__}')
# 		return self.original_function(*args, **kwargs)
import time

@my_logger
def display():
	print('display function ran')

@my_logger
@my_timer
def display_info(name, age):
	time.sleep(1)
	print(f'Hello my name is {name} and I am {age} years old')

# display_info = my_logger(my_timer(display_info))

# display_info('Joseph', 16)

display_info('Joseph', 16)
