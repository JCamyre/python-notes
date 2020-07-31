print('Hello'.center(30, '*'))
print('Hello'.rjust(30, '-'))
print('Hello'.ljust(30, '.'))



name = 'Joseph Camyre'
age = 16
print(f'Name: {name:25}, Age: {age:25}')



int_arr = list(range(10))
print(*int_arr)



arr = [1, 2, 3]
cmd = 'pop'
index = 2
print(arr)
exec(f'arr.{cmd}({index})')
print(arr)



from itertools import groupby

for key, i in groupby([1, 2, 2, 2, 1, 1, 3, 3, 3, 4, 5, 6, 6, 6, 6]):
	print((len(list(i)), int(key)), end=' ')

# vs

from collections import Counter

print(Counter([1, 2, 2, 2, 1, 1, 3, 3, 3, 4, 5, 6, 6, 6, 6]))



class Deque:
	def __init__(self, arr=[]):
		self.arr = arr

	def append(self):
		pass

	def appendleft(self):
		pass

	def extend(self, vals):
		pass

	def extendleft(self, vals):
		pass

	def pop(self):
		pass

	def popleft(self):
		self.arr[::-1].pop()

	def remove(self, val):
		pass

	def reverse(self):
		pass

	def rotate(self, rotations):
		pass



print(pow(4, 4), 4**4, pow(4, 4, 3), 4**4 % 3)


# find the last occurence of an element in a list
arr = ['a', 'a', 'a', 'b', 'c']
element = 'a'
i = next(i for i, j in enumerate(reversed(arr)) if j == element)
print(i)
# or 
i = next(i for i, j in enumerate(arr) if j != element) - 1
print(i)



# Round to three decimal places:
print('%.3f'%(0.224652))
print('%.3f'%(0.224252))



# Convert *arr of strings to a list of floats
# list(map(float, input().split()))
# *map(float, input().split())
print(list(map(len, ['Joseph', 'Camyre', 'says', 'hello'])))
print(list(map(lambda x: x**2, [432, 54325, 1])))



# Multiple lists zip, star expression (*) very crucial
student_scores = [[100, 90, 95, 80, 45], [89, 74, 67, 80, 60]]
for i in list(zip(*student_scores)):
	print(i)
print(*student_scores)



print(any([False and False, 0 > 1, False or True]))

print(all([False and False, 0 > 1, False or True]))

# all(i>=0 for i in arr), any(((i==reversed(i)) for i in arr))
# all() is basically used as list comprehension, but ele > 3 instead of just [ele for ele in test_list]



# reduce() method, takes three arguments: a function to act on an array, an array, and a possible third value. BRUH ARGUMENT, PARAMETER
from functools import reduce 

print(reduce(lambda x, y : x + y,[1,2,3]))

from math import gcd
print(reduce(gcd, [2,4,8], 3))





'''
Input: 
0 4 5
1 7 6
0 5 9
1 7 2
'''
import math

# class Points(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __sub__(self, no):
#         return Points(self.x - no.x, self.y - no.y, self.z - no.z)

#     def dot(self, no):
#         # return Points(self.x * no.x, self.y * no.y, self.z * no.z)
#         return self.x * no.x + self.y * no.y + self.z * no.z

#     def cross(self, no):
#         return Points((self.y * no.z) - (self.z * no.y), (self.z * no.x) - (self.x * no.z), (self.x * no.y) - (self.y * no.x))
        
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

# if __name__ == '__main__':
#     points = list()
#     for i in range(4):
#         a = list(map(float, input().split()))
#         points.append(a)

#     a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
#     x = (b - a).cross(c - b)
#     y = (c - b).cross(d - c)
#     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

#     print("%.2f" % math.degrees(angle))



def fib(n):
	arr = [0, 1]
	for i in range(n):
		arr.append(arr[i-2] + arr[i-1])
	return arr[:n]

# LEARNING REGULAR EXPRESSIONS
import re

text = 'First Name: Joseph, Last Name: Camyre'
text_search = re.findall(r'[a-e:]', text)
if text_search:
	print(text_search)

text_search = re.findall(r'[aeiou]', text)
if text_search:
	print(text_search)

text_search = re.findall(r'[^aeiou]', text)
if text_search:
	print(text_search)

pattern = re.compile('Joseph')
text_search = re.findall(pattern, text)
if text_search:
	print(text_search)

text = 'First Name: Joseph, Last Name: Camyre'
text_search = re.search(r': \w', text)
if text_search:
	print(text_search.group())

text = 'First Name: Joseph, Last Name: Camyre'
text_search = re.search(r': \w+', text)
if text_search:
	print(text_search.group())
	print(text_search.end())

text_search = re.search(r'\D', text)
if text_search:
	print(text_search.group())
	print(text_search.end())


text_search = re.search(r'\D+', text)
if text_search:
	print(text_search.group())
	print(text_search.start())
	print(text_search.end())

m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(0), m.group(1), m.group(2), m.group(3), m.group(1, 2, 3), m.groups())

m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())


# https://www.rexegg.com/regex-quickstart.html


phone_num = '9587456281'

first_digit = re.match(r'\d', phone_num)
print(first_digit.group())
if int(re.match(r'\d', phone_num).group()) in [7, 8, 9] and re.findall(r'\D', phone_num) == []:
    print('YES')
else:
    print('NO')
# https://developers.google.com/edu/python/regular-expressions
# https://www.w3schools.com/python/python_regex.asp
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html#5



# Overriding a subclass
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    '''Plan of attack for attributes, new method or if statements in the existing methods?'''
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attr in attrs:
                print(f'-> {attr[0]} > {attr[1]}')
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)    

# parser = MyHTMLParser()
# parser.feed(input())




print('1'.isdigit())



# Sorting by a column in a 2d array
arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
k = 1
sorted_arr = sorted(arr, key=lambda x: x[k])
for i in sorted_arr:
    print(*i)



class Num:
	def __add__(self, no):
		return no * 2

a = Num()
# __add__() is one of the "magic" methods. Basically __add__ replaces what "+" normally does. So I put no * 2, so now
# with an instance of the Num class, what ever I add to the instance, it is multiplied by 2. no == 4, 4 * 2 == 8
print(a + 4)


# You can also put an actual function, not just a lambda. Just put filter(func, arr)
filtered_arr = list(filter(lambda x: x%2==0, list(range(100))))
print(filtered_arr)

mapped_arr = list(map(lambda x: x**3, list(range(100))))
print(mapped_arr)

import numpy as np

# fairly similar to the classic: list(map(int, input().split()))
A = np.array('1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9'.split(), float)

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))

# rather than nm = input.split(), n = int(nm[0]). Continuing on simplifying inputs, if multiple for loops, use a list 
# comprehension to get the input()

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# np.concatenate, np.transpose, np.array().flatten

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = np.reshape(arr, (3, 3))

print(arr)

print(np.sum(arr), np.sum(arr, axis=0), np.sum(arr, axis=1))
print(np.prod(arr), np.prod(arr, axis=0), np.prod(arr, axis=1))
print(np.min(arr), np.min(arr, axis=0), np.min(arr, axis=1))
print(np.max(arr), np.max(arr, axis=0), np.max(arr, axis=1))

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = np.reshape(arr2, (3, 3))
print(np.dot(arr, arr2), np.cross(arr, arr2))

# def is_vowel(letter):
    # return letter in ['a', 'e', 'i', 'o', 'u', 'y']

s = "The quick brown fox jumps over the lazy dog"
print(s.replace(' ', '').lower())

import string

s = 'middle-Outz'
k = 2

lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase

arr = list(s)
shift_lowerchar = lambda char: lower_char[(lower_char.index(char) + k) % 26]
shift_upperchar = lambda char: upper_char[(upper_char.index(char) + k) % 26]

print(list(map(lambda x: shift_lowerchar(x) if x in lower_char else (shift_upperchar(x) if x in upper_char else x), arr)))

s = 'SOSSOSSOS'
rads = 0
for i, char in enumerate(s):
    print(i, char, 'SOS'[i % 3])
    if not char == 'SOS'[i % 3]:
        rads += 1
print(rads)

# When dealing with consecutive letters, use the * with regex


# I FINALLY DID A DATA STRUCTURE CHALLENGE, WE REALLY BE LEVELING UP
def insertNodeAtTail(head, data):
    if head:
        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = SinglyLinkedListNode(data)
        return head
    else:
        return SinglyLinkedListNode(data)

# inserting at a specific index shows how efficient linkedlists are: you only have to update two node's positions, the node
# in front of and behind the inserted node, rather than having to update every node's index after the inserted node. Crazy

def insertNodeAtPosition(head, data, position):
    cur_node = head
    if head:
        for _ in range(position-1):
            cur_node = cur_node.next
        moved_node = cur_node.next
        inserted_node = SinglyLinkedListNode(data) 
        cur_node.next = inserted_node
        inserted_node.next = moved_node
        return head
    else:
        return SinglyLinkedListNode(data)


from time import time

nums = [3,2,4]
target = 6
time_initial = time()
for i, _ in enumerate(nums):
	complement = target - nums[i]
	print(nums[i+1:], nums[:i])
	if complement in nums[i:] or complement in nums[:i]:
		print([i, nums.index(complement)])
print(f'{time()-time_initial:.1000000000}')


