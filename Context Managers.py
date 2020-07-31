"""
THIS IS JUST SAD, GOOD THING TIM TAUGHT ME BETTER
f = open('test.txt', 'r')
file_contents = f.read()
f.close()
MANAGE ANY TYPE OF RESOURCE
"""

with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
for x in words:
    print(x, end=' ')
print(words)
