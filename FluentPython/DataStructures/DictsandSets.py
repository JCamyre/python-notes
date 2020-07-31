'''
Generic Mapping Types

All mapping types use the basic dict, meaning that the keys must be hashable, not the values tho
What is hashable? Idk, I'll find out tho.
Hashable basically means that an object has a hash value that is immutable, and can be compared to other objects.
Hashable objects that compare equal must have the same hash value.
This means that hashable objects must have a __hash__() method and a __eq__() method.
Hash value is basically where it converts a value to another
Hashes are used to index data, by mapping data to individual "buckets" within a hash table
Hash table: hash code is the index/key, and the buckets/slots are the values
Atomic operation: an operation that appears to be instantaneous from the perspective of all other threads
I need to learn about how threads work with compiling and such
Interestingly, you can hash tuples, but not lists
'''

tt = (1, 2, (3, 4))
print(hash(tt))
tl = (1, 2, [3, 4])
try:
	print(hash(tl))
except TypeError:
	print('You can\'t hash lists')
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

'''You can hash pretty much anything that is immutable built-in objects, except as seen with tuples not if it 
contains unhashable objects
Try the __eq__ method in a class
'''

# DICTIONARIES
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

DIAL_CODES = [
(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

print({code: country.upper() for country, code in country_code.items() if code < 66})

# If a key isn't in a dictionary, what to do???? Default value...

# setdefault() sets the key "key" to the value [], and then it appends new_value to the key "key"
# my_dict.setdefault(key, []).append(new_value)

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

# if a key doesn't exist yet, default to index[key] = list(), only works with the __getitem__ calls
index = collections.defaultdict(list)

with open('words.txt', encoding='utf-8') as fp:
	for line_no, line in enumerate(fp, 1):
		for match in WORD_RE.finditer(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			index[word].append(location)

for word in sorted(index, key=str.upper):
	print(word, index[word])

'''__missing__
It is not in the base dict class, but you can subclass dict and add your own __missing__
Whenever a key is not found dict.__getitem__(), instead of raising KeyError, it will run __missing__
'''

class StrKeyDict0(dict):
	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError(key)
		# self is the dict itself: self['key'] = 'value'
		return self[str(key)]

	def get(self, key, default=None):
		try: 
			return self[key]
		except KeyError:
			return default

	def __contains__(self, key):
		'''btw doing: key in self would run __contains__, making this infinite loop
		[Previous line repeated 996 more times]
		RecursionError: maximum recursion depth exceeded'''
		return key in self.keys() or str(key) in self.keys()

	def __repr__(self):
		return f'{self.items()}'



d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'], d[2])
print(d.get('4'), d.get(4), d.get(1, 'N/A'))
print(d)
print('2' in d)

'''VARIATIONS OF DICT
collections.OrderedDict (keeps the order that items were appended) .popitem() gets rid of first element
collections.ChainMap
collections.Counter'''

import collections
# import builtins

# print(collections.ChainMap(locals(), globals(), vars(builtins)))

ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(2))


# collections.UserDict

class StrKeyDict(collections.UserDict):

	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError(key)
		# if the key isn't a string, try again to see if string version of key works
		return self[str(key)]

	def __contains__(self, key):
		# self.data is the same as self when you inherited from dict
		return str(key) in self.data

	def __setitem__(self, key, item):
		# Is this self.data.__getitem__(str(key)) = item
		self.data[str(key)] = item

# Immutable Mappings (basically can't mess with dictionary items)

from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
try:
	d_proxy[2] = 'B'
except TypeError:
	print("You can't do that lol.")
d[2] = 'B'
print(d_proxy)

# You can't directly modify the proxy, but you can edit the original dictionary since MappingProxyType is dynamic

# Set Theory

a = {1, 2, 3}
b = {2, 3, 4, 5}
print(a | b, a & b, a - b)

'''A simple use case for sets are given a large "haystack", and a smaller set "needles", find which needles 
are in the haystack'''

empty_set = set()

# LEARN ABOUT BYTECODE

from dis import dis 

# load set, build set, return the value in the set
dis('{1}')
# load name of constructor, load constructor, build the list provided, call the function to build the set, return value
dis('set([1])')

print(frozenset(range(10)))

from unicodedata import name 

print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})

# Hash tables for searching, don't know about that. Conclusion: sets and dicts way faster than lists

'''More about hash tables:
It is a sparse array: always has empty cells
Python trys to keep at least 1/3 of the cells (aka buckets) empty, which is accomplished by copying the table
to make room for more buckets
Each bucket contains an item: a reference to the key and a reference to the value of the item
To put an item in the hash table, you must first calculate the hash value of the item key (using hash())
If 1 == 1.0, then hash(1) == hash(1.0), which is True
Since hash values want to scatter around the index space as much as possible, objects that are similar, but not
equal, should have hash values that differ widely, such as 1 and 1.000001
Random salt value...
'''
print(1 == 1.0, hash(1), hash(1.0))
print(1 == 1.00000001, hash(1), hash(1.00000001))

'''
DICTS:
THEY ARE VERY FAST FOR SEARCHING, BUT THEY ARE VERY MEMORY INTENSIVE, due to the hash tables

Say my_dict = {search_key: value}, and I want to find the value for the key search_key: my_dict[search_key]
This is what Python does:
First, find the has value of search_key, hash(search_key)
Then, it uses the hash value to find the bucket in the hash table
If found bucket is empty, then KeyError is raised
If found bucket contains an item, checks if search_key == found_key, if True, value is returned
If they don't match, this is called a hash collision
To resolve this, the searching algorithm uses other bits from the hash key to look in a different row of the 
hash table, and keep on checking the buckets
Hash collisions are one of the reasons why Python likes to keep 1/3 of buckets empty and indexes spread out
For inserting and updating items, same thing as searching, except once you find the bucket, add the item
or replace the value
'''

'''
For custom classes classes and you want to implement a unique __eq__ method, you must also implement a suitable
__hash__, but if you must have your __eq__ mutable, then __hash__ must raise a TypeError "MyClass"

One of the main issues with dict is the significant memory overhead, since the hash tables are so large
An example where you could use tuples is a list of tuples, rather than a list of dicts: [(key, val)]
However, if you are only dealing with a few MILLION objects, don't do this: "Optimization is the altar where
maintainability is sacrificied"

Insertion order for dicts dictate element ordering, may change it aswell
'''

d = {'one': 1, 'two': 2, 'three': 3}
d2 = {'two': 2, 'three': 3, 'one': 1}
d3 = {'three': 3, 'one': 1, 'two': 2}
print(d == d2 == d3)

'''
Sets:
Hash tables with buckets, same thing as dictionary except only a value in each bucket
Heavy memory, but very quick
Insertion order determines element order, and may change the current element order
'''