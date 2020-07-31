import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# https? = (http|https). (www\.)? = w?w?w?\.?. 
# Ahhh, so () which are for groups, we can use the group() method.
# The first group is the (www\.), the next group is (\w+), and the final group is (\.\w+). group(1), group(2), group(3)
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# use the pattern we already created, then \(number of group) to reference a group. This format: \2\3, will replace any urls
# that are found in the urls string
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(1))





