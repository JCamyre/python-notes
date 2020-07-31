'''The Python Data Model... sounds epic. "Formalizes the interfaces of the building blocks of the language: functions, classes, sequences, etc."

Magic methods == special methods == dunder methods

The special/magic methods: __add__ (+), __sub__ (-), and these are pretty interesting: __getitem__ (obj[key]), __len__ (len(obj)),
__contains__ (element in iteritable)
Ex: 
'''
info = {'name': 'Joseph Camyre'}
print(info['name'])
print(info.__getitem__('name'))

print(len(info['name']))
print(info['name'].__len__(), info['name'].__len__)

# A Pythonic Card Deck
import collections

# You can use the namedtuple() method to create 2d tuples with assigned names
Card = collections.namedtuple('card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JKQA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		# I didn't know you could do list comprehensions like this
		self._cards = [Card(rank, suit) for rank in self.ranks
										for suit in self.suits]

	# Wow, what other "regular" method looks like this. Maybe it's not...
	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]

	def __str__(self):
		return 'This is a standard deck of 52 cards.'

deck = FrenchDeck()
print(len(deck))
print(deck[0]) 
print(deck)

from random import choice

print(choice(deck))

print(deck[:3])
print(deck[12::13])

'''Can use the __contains__ method for the "in" keyword such as: 
	def __contains__(self, element):
		if self.arr[element]:
			return True
		return False
'''
print(Card('2', 'spades') in deck)
for card in deck[:5]:
	print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
	# Get the index of the card value
	rank_value = deck.ranks.index(card.rank)
	# Return that value multiplied by which suit the card is. So as long as it returns a number, any function can be a sorted key...
	return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
	print(card)

'''
How Special Methods Are Used:

So for user created objects, such as deck, using len() will call the __len__ magic method.
For built-in types, such as list, str, bytearray, etc, it will return an attribute of the object/type, interesting. CPython
'''

from math import hypot

class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Vector({self.x:int}, {self.y:int})'

	def __abs__(self):
		return hypot(self.x, self.y)

'''	Truthy or falsy. Essentially, user classes are considered truthy or falsy, unless either __bool__ or __len__ is implemented.
	So basically: remember when you do:
	if obj:
		print(obj)
	obj returned True because either there was a __bool__ method or the object had some length len() __len__ '''

	def __bool__(self):
		return bool(abs(self))
		# return self.x or self.y

	# So that's how you use __add__ lol
	# "Operand": the object being operated on (grape)
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)

'''83 special methods
unary operators, don't know enough about those
Len is not a method because as mentioned early, when len(str), len(list), etc, it just returns an attribute from that object'''


