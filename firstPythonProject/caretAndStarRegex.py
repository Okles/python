import re

beginsWithHelloRegex = re.compile(r'Hello')
print(beginsWithHelloRegex.search('Hello there!'))

endsWithWorldRegex = re.compile(r'world!$') ## $ - the end of the string has to match
print(endsWithWorldRegex.search('Hello world!'))

allDigitsRegex = re.compile(r'^\d+$') ## ^ caret (entire text has to egin with it), one or more numeric digit, has to end with given pattern
print(allDigitsRegex.search('233434534'))

atRegex = re.compile(r'.at') #dot - any SINGLE character followed by at EXCEPT a new line character and only until it reaches it
print(atRegex.findall('A cat in the hat sat on the flat mat'))

atRegex = re.compile(r'.{1,2}at') #dot - any 1 or 2 characters followed by at
print(atRegex.findall('A cat in the hat sat on the flat mat'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Lukasz Last Name: Oklesinski'))

## .* is greedy, .*? is a non-greedy one

serve = '<To serve humans> for dinner.>'
nonGreedy = re.compile(re.compile(r'<(.*?)>'))
print(nonGreedy.findall(serve))

greedy = re.compile(re.compile(r'<(.*)>'))
print(greedy.findall(serve))

##dotStar newline example

prime = 'Some sentence.\nThat is a multi-line one\nTo show how dotstar works by default'
dotStar = re.compile(r'.*')
print(dotStar.search(prime))

##how to overcome this:

dotStarAll = re.compile(r'.*',re.DOTALL)
print(dotStarAll.search(prime))

##ignoring a case

vowelRegex = re.compile(r'[aeiou]',re.I) ##ignore case
print(vowelRegex.findall('Some Example of A sentence'))