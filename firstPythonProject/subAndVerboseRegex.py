import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave secret documents to Agent Bob'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave secret documents to Agent Bob')) #substitute Agent with the rest with REDACTED

namesRegex2 = re.compile(r'Agent (\w)\w*') #one letter plus space plus other letters
print(namesRegex2.findall('Agent Alice gave secret documents to Agent Bob'))
print(namesRegex2.sub(r'Agent \1*****','Agent Alice gave secret documents to Agent Bob')) #1 stands for substitting 1st group in a regex pattern matching a pattern

##verbose format

re.compile(r'''
(\d\d\d-)|   #area code (without parens, with dash)
(\(\d\d\d\) ) # -or- area ode with parens and no dash
\d\d\d   #first 3 digits
-        #second dash
\d\d\d\d #last 4 digits
\sx\d{2,4} #extensions like x1234
''', re.VERBOSE | re.IGNORECASE) #using more arguments
