Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> shelfFile['cats']
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    shelfFile['cats']
NameError: name 'shelfFile' is not defined
>>> import shelve

>>> shelfFile = shelve.open('mydata')

>>> shelfFile['cats'] = ['Name1', 'Name2', 'Name3']
>>> shelfFile.close()

>>> shelfFile = shelve.open('mydata')

>>> shelfFile.keys()

KeysView(<shelve.DbfilenameShelf object at 0x01BFEBF0>)
>>> shelfFile['cats']
['Name1', 'Name2', 'Name3']
>>> list(shelfFile.values())
[['Name1', 'Name2', 'Name3']]
>>> 
