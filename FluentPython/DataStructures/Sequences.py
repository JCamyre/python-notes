'''
Container vs flat sequences: (list vs str)
Container sequences can hold multiple data types, while flat sequences can only hold one.

Mutable vs immutable sequences: (list vs str)
Self explanatory, but on a low level how do these two differ?

Mutable sequences have 9 extra methods, including those two add/remove from the sequence
'''

# Listcomps and Genexps
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
	codes.append(ord(symbol))
print(codes)

codes = [ord(symbol) for symbol in symbols]

twod = [(x, y) for x in range(3)
				for y in range(3, 0, -1)]
print(twod)

# listcomps > filter and map
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]

codes = list(filter(lambda c: c > 127, map(ord, symbols)))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for size in sizes
						for color in colors]
# Sorts by size since for size in sizes is before colors
print(tshirts)

# Genexps
print(tuple(ord(symbol) for symbol in symbols))

import array 
print(array.array('I', (ord(symbol) for symbol in symbols)))

# Generator expressions save don't have to build the entire list at once, saving time since less memory is being used
for tshirt in (f'{color} {size}' for size in sizes for color in colors):
	print(tshirt)

'''Tuples actually have some use, who would've known?
Due to their immutable nature, they are commonly used for records, and the data values' index within the tuple 
contain meaning'''
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
	print(f'{passport[0]} {passport[1]}')

# Example of tuple unpacking, sometimes known as iterable unpacking
for country, _ in traveler_ids:
	print(country)

latitude, longitude = lax_coordinates
print(latitude, longitude)

a, b = 1, 2
b, a = a, b
print(a, b)

t = (20, 8)
print(divmod(*t))

import os 

_, filename = os.path.split('C:/Users/JWcam/Desktop/NCT 127 - Regular.wav')
print(filename)

a, b, *rest = range(10)
print(rest)

a, *middle, b, c = range(10)
print(middle, b, c)

metro_areas = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))

for name, cc, pop, (latitude, longitude) in metro_areas:
	if longitude <= 0:
		# :15 is total spaces, 9.4 is 9 spaces and 4 sig figs
		print(f'{name:15} | {latitude:9.4} | {longitude:9.4}')

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
# It's like creating an instance of a class, PogU
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # Same thing as City(*delhi_data)
print(delhi)
print(delhi._asdict())
for key, value in delhi._asdict().items():
	print(f'{key}: {value}')

# The difference between reversed() and .reverse() is reversed() doesn't modify the list, while .reverse() does

l = [10, 20, 30, 40, 50, 60]
print(l[2:], l[:2], l[3:], l[:3])

# How python reads a slice: given list l and slicing every other element, starting at index 1
print(l.__getitem__(slice(1, 5, 2)))

# Make your own named slice objects

invoice = """
0....5.................................40........52...55........
1909 Pimoroni PiBrella 					$17.50 	3 		$52.50
1489 6mm Tactile Switch x20 			$4.95 	2	 	$9.90
1510 Panavise Jr. - PV-201 				$28.00 	1	 	$28.00
1601 PiTFT Mini Kit 320x240 			$34.95 	1	 	$34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
	print(item[UNIT_PRICE], item[DESCRIPTION])


l = list(range(10))
l[2:4] = [30, 50]
print(l)
del l[2:4]
print(l)

board = [['-'] * 3 for _ in range(3)]
print(board)
board[1][2] = 'X'
print(board)

'''+= __iadd__, *= __imul__
Same list object when *= with a mutable sequence, different tuple object when *= with an immutable sequence, 
making it inefficient'''
l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l), l)

t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t), t)

# This is Python bytecode
import dis
dis.dis('s[a] += b')
# TOP OF STACK (monkaTOS)... https://www.geeksforgeeks.org/stack-in-python/. Need to learn ig

'''list.sort() modifies the list, not return a new list object, thus it returns None. Sorted() returns a new modified 
list, so it does not return None
An interesting tidbit about sorting algorithms is the algorithm used in Python, Timsort, is "stable", meaning that
for elements that have equal value according to the key, their initial indexes/positions will be conserved'''


# bisect module: binary search algorithm poggers

import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
	for needle in reversed(NEEDLES):
		position = bisect_fn(HAYSTACK, needle)
		offset = position * ' |'
		print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':

	if sys.argv[-1] == 'left':
		bisect_fn = bisect.bisect_left
	else:
		bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
'''The function is using bisect.bisect, aka bisect_right, where if the "needle" we are using is the exact same value
as one in the list we are searching through, we will insert the needle right(i + 1) after the exact same value.
for bisect_left, we insert at that iindex.'''
demo(bisect_fn)

# def test() -> int:
# 	return 1

# print(test.__name__, test())

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
	i = bisect.bisect(breakpoints, score)
	return grades[i]

# bisect.bisect(arr, element) is quicker than arr.index(element), but arr has to be sorted()
print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

import random
# bisect.insort() inserts elements so that the list is always sorted

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
	new_item = random.randrange(SIZE*2)
	bisect.insort(my_list, new_item)
	# {new_item:.2f}
	print(f'{new_item:2d} ->', my_list)

'''Linus Tech Tip: There are plenty of scenarios where lists aren't the best option
For example, if you need to store millions of data values, arrays are the best since they don't
store the actual int objects, just the "machine values" for them, thus much more efficient and less memory'''

# ARRAYS
from array import array

'''floats = array('d', (random.random() for i in range(10**7)))
print(floats[-1])
with open('floats.bin', 'wb') as file:
	floats.tofile(file)

floats2 = array('d')
with open('floats.bin', 'rb') as file:
	floats2.fromfile(file, 10**7)

print(floats2[-1])'''

# array() is much faster to import from a file, less than half memory usage, PogU

# Memory Views with arrays, idk what that is

'''Basically convert array to memv, then cast the elements to typecode 'B', honestly idk, only thing I can
think of is 1111 = 1024
'''
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)


# NumPy and SciPy
# Need to 10 million float values first lol, do it later, but the time.perf_counter() is interesting

# import numpy
# import scipy 

# a = numpy.arange(12)
# print(a)
# print(type(a), a.shape)
# a.shape = 3, 4
# print(a, a[1], a[2, 2], a[:, 1])
# print(a.transpose())

# floats = numpy.loadtxt('floats-10M-lines.txt')
# print(floats[-3:])
# floats *= 0.5
# print(floats[-3:])
# from time import perf_counter as pc 
# print(t0 = pc(); floats /= 3; pc() - t0)
# numpy.save('floats-10M', floats)
# floats2 = numpy.load('floats-10M.npy', 'r+')
# floats2 *= 6
# floats2[-3:]

'''Queues
Some uses include quick inserting/removing from both ends (much more efficient than lists), which is needed
for a "last seen items" thing
However, if you need to access middle values, choos something else'''

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
print(dq.rotate(3))
print(dq)
print(dq.rotate(-4))
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

# There are many other queue data structures
# Maybe read his soapbox things?


