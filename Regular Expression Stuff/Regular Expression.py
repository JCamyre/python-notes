import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

cat 
bat 
mat 

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# \t is normally intrepeted as a tab, so to pass regex patterns, we must put an r in front of the string to specific a raw string
print('\tHello')
print(r'\tHello')

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)
for match in matches:
	print(match, match.span())

print(text_to_search[1:4])

def find_matches(pattern, words):
    matches = pattern.finditer(words)
    for match in matches:
        print(match, match.span())	

# Use \. to search for periods, since . is a specific regex character
# pattern = re.compile(r'\.')
# find_matches(pattern, text_to_search)

# pattern = re.compile(r'coreyms\.com')
# find_matches(pattern, text_to_search)

# pattern = re.compile(r'\w')
# find_matches(pattern, text_to_search)

# pattern = re.compile(r'\bHa')
# find_matches(pattern, text_to_search)

# pattern = re.compile(r'\bMr.')
# find_matches(pattern, text_to_search)

# pattern = re.compile(r'^\w+')
# find_matches(pattern, sentence)

# pattern = re.compile(r'\w+$')
# find_matches(pattern, sentence)

# if you want to find . or -, but you don't care how many of them, do [-.]+
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
find_matches(pattern, text_to_search)

with open('data.txt', 'r') as file:
	text = file.read()

	pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
	# find_matches(pattern, text)

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
find_matches(pattern, text_to_search)

# use ^ to find everything EXCEPT something. ie: ^[a-z]: find everything except for lowercase alphabet characters
# find any word that ends in at, and doesn't start with b
pattern = re.compile(r'[^b]at')
find_matches(pattern, text_to_search)

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
find_matches(pattern, text_to_search)

'''The difference between \w* and \w+ is because Mr. T's last name is only one letter, so if we used \w+ after the capital 
letter of their last name, regex wouldn't detect it. With \w*, having letters after the capital letter is optional 
(0 or more), so it includes Mr. T'''
# (a|b|c), divides into groups, a or b or c.
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
find_matches(pattern, text_to_search)

# other methods: pattern.findall(), pattern.match()
print(pattern.findall(text_to_search))

pattern = re.compile(r'\w+')
print(pattern.match(sentence))

pattern = re.compile(r'\w+')
print(pattern.search(sentence))

pattern = re.compile(r'start', re.IGNORECASE)
print(pattern.search(sentence))

# FOR re.sub/pattern.sub, you can add a method: pattern.sub(METHOD, text) or re.sub(pattern, method, text)
s = '''
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
'''
pattern = re.compile(r' (&&|\|\|) ')
print(pattern.sub(lambda x: ' and ' if x.group() == ' && ' else ' or ', s))
