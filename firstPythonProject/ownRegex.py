import re

vowelRegex = re.compile(r'[aeiouAEIOU]') #same as r'[a|e|i|o|u], we can even write [a-z] of [A-F]
print(vowelRegex.findall('Some example simple sentence'))


##two vowels in a row

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}') #same as r'[a|e|i|o|u], we can even write [a-z] of [A-F]
print(doubleVowelRegex.findall('Some example simple sentence about eating'))

##non-vowels

nonVowelRegex = re.compile(r'[^aeiouAEIOU]') #same as r'[a|e|i|o|u], we can even write [a-z] of [A-F]
print(nonVowelRegex.findall('Some example simple sentence'))