import re

# Repeating character stuff, not good at it.
text = '1234444556221'
# So I g this is basically saying out of all the digits (\d+) group, only the four has four copies of itself: (\d+)\1\1\1
pattern = re.compile(r'(\d+)\1\1\1')
print(pattern.findall(text))

text = '''
#hello
{background-color: #123
#hi
{background-color: #5423
#goodbye
{background-color: #4235342
#nihao
{background-color: #234562'''

pattern = re.compile(r'[\w]*\n{')
print(pattern.findall(text))

pattern = re.compile(r'#[\d]{3,6}[^\n{]')
print(pattern.findall(text))

text = '''
35
.arrow-up {
	width: 0;
	height: 0;
	border-left: 5px solid transparent;
	border-right: 5px solid transparent;

	border-bottom: 5px solid black;
}

.arrow-down {
	width: 0;
	height: 0;
	border-left: 20px solid transparent;
	border-right: 20px solid transparent;

	border-top: 20px solid #f00;
}

.arrow-right {
	width: 0;
	height: 0;
	border-top: 60px solid transparent;
	border-bottom: 60px solid transparent;

	border-left: 60px solid green;
}

#f0f {
	width: 0;
	height: 0;
	border-top: 10px solid transparent;
	border-bottom: 10px solid transparent;

	border-right:10px solid blue;
}
'''

# shouldn't the next character be a ;, not a {?
pattern = re.compile(r'#[0-9A-Fa-f]{3,6}[^\n{|^ {]')
print(pattern.findall(text))

