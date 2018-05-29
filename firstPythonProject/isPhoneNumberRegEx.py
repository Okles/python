import re

phoneNumRegex = re.compile(r'\(\d\d\d\)\d\d\d-\d\d\d\d') #raw strings in a defined pattern, \(...\) searches for literal strings, (character) stands for optional

print(phoneNumRegex.findall('Call me (333)432-4574 blablabla')) #finding a string that matches to a pattern

mo = phoneNumRegex.search('Call me (333)432-4574 blablabla')
print(mo.group())
# print(mo.group(1))

#pipe symbol:

batRegex = re.compile(r'Bat(man|mobile|copter)')

mo = batRegex.search('Batmobile lost a wheel')

print(mo.group())

'Batmobile'