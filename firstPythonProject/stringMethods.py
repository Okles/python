import  pyperclip

spam = 'Hello world!'
print(spam.upper())
print(spam.lower())

#spam.isupper, spam.islower - return a bool value
#isalpha, isalnum, isdecimal, isspace, istitle

print('Do you want to play again?')
answer = input()

if answer.lower() == 'yes': #ignoring a case
    print('Playing again!')
else:
    print("Game over!")


#
# >>> 'hello'.isalpha()
# True
# >>> 'hello123'.isalnum()
# True
# >>> '123'.isnumeric
# <built-in method isnumeric of str object at 0x01C8D6A0>
# >>> '123'.isdecimal
# <built-in method isdecimal of str object at 0x01C8D6A0>
# >>> '123'.isdecimal()
# True
# >>> 'Hello World'.isspace()
# False
# >>> 'Hello World'[5].isspace()
# True
# >>> 'This is Title Case.'.istitle()
# False
# >>> 'This Is Title Case.'.istitle()
# True
# >>>
#
# >>> 'Hello world!'.startswith('H')
# True
# >>>
# >>> 'Hello world!'.endswith('D')
# False
# >>> 'Hello world!'.endswith('d')
# False
# >>> 'Hello world!'.endswith('!')
# True

# >>> ','.join(['cats','rats','bats'])
# 'cats,rats,bats'
# >>> ''.join(['cats','rats','bats'])
# 'catsratsbats'
# >>> ' '.join(['cats','rats','bats'])
# 'cats rats bats'
# >>> '\n'.join(['cats','rats','bats'])
# 'cats\nrats\nbats'
# >>> 'My Name is Lukasz'.split('k')
# ['My Name is Lu', 'asz']
# >>>

# >>> 'Hello'.rjust(55)
# '                                                  Hello'
# >>> 'Hello'.ljust(55)
# 'Hello                                                  '
# >>>>>> 'Hello'.ljust(55, '*')
# 'Hello**************************************************'
# >>> 'Hello'.center(25)
# '          Hello          '
# >>> 'Hello'.center(25,'=')
# '==========Hello=========='
# >>>

name = 'Lukasz'
print(name.center(20,'='))
print(name.strip()) #removes white spaces - lstrip and rstrip are also available
spam = 'SpamSpamSomeOtherWordsSpam'
print(spam.strip('ampS'))
print(spam.replace('S','REPLACEMENT'))

pyperclip.copy('Test!!!!')
print (pyperclip.paste())
