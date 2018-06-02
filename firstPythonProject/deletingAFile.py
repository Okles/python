Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #deleting files
>>> import os
>>> os.getcwd()
'C:\\Users\\Okles\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.chdir(r'C:\delicious')
>>> os.rmdir(r'C:\delicious')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    os.rmdir(r'C:\delicious')
PermissionError: [WinError 32] Proces nie może uzyskać dostępu do pliku, ponieważ jest on używany przez inny proces: 'C:\\delicious'
>>> os.rmdir(r'C:\delicious')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.rmdir(r'C:\delicious')
PermissionError: [WinError 32] Proces nie może uzyskać dostępu do pliku, ponieważ jest on używany przez inny proces: 'C:\\delicious'
>>> os.rmdir(r'C:\delicious\cake')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.rmdir(r'C:\delicious\cake')
OSError: [WinError 145] Katalog nie jest pusty: 'C:\\delicious\\cake'
>>> #folder not empty
>>> 
>>> import shutil
>>> shutil.rmtree(r'c:\delicious\cake')
>>> 

>>> import os
>>> for filename in os.listdir():
	if filename.endswith('.rxt'):
		#os.unlink(filename)
		print(filename)

		
>>> os.chdir(r'C:\users\okles\desktop')
>>> for filename in os.listdir():
	if filename.endswith('.rxt'):
		#os.unlink(filename)
		print(filename)

		
>>> for filename in os.listdir():
	if filename.endswith('.txt'):
		#os.unlink(filename)
		print(filename)

		
>>> for filename in os.listdir():
	if filename.endswith('.txt'):
		#os.unlink(filename)
		print(filename)

		
test.txt
>>> 
>>> 
>>> 
>>> import send2trash
>>> 
>>> send2trash.send2trash(r'C:\users\okles\desktop\test.txt')
>>> #has moved a file to a trashbin
>>> 
