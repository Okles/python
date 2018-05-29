import re

batRegex = re.compile(r'Bat(wo)?man') #appearing 1 or 0 times

mo = batRegex.search('The Adventures of Batman')
print (mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print (mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo2 = phoneRegex.search('My phone number is 344-212-4544')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)*man') #appearing  0 or more times
mo = batRegex.search('The Adventures of Batwowoman')
print (mo.group())


##If you want to match a special character, i.e. ? or *, use: /? or /*

batRegex = re.compile(r'Bat(wo)*man') #appearing  1 or more times
mo = batRegex.search('The Adventures of Batwowoman')
print(mo.group())


###

regex = re.compile(r'\+\*\?')
mo = regex.search("I've just learned about +*? regex syntax")
print(mo.group())

regex = re.compile(r'(\+\*\?)+')
mo = regex.search("I've just learned about +*?+*?+*?+*?  regex syntax")
print(mo.group())

haRegex = re.compile(r'(Ha){3,5}') #between 3 and 5 appearances, {3,} = 3 or more
mo = haRegex.search('He said HaHaHa')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}') #any 3 to 5 digits - greedy match, matches a longest string possible
mo = digitRegex.search('1234567890')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}?') #any 3 to 5 digits - non-greedy match, matches a shortest string possible
mo = digitRegex.search('1234567890')
print(mo.group())

