Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import shutil
>>> shutil.copy('c:\\spam\\spam.txt', 'c:\\delicious')
'c:\\delicious\\spam.txt'
>>> shutil.copy('c:\\spam\\spam.txt', 'c:\\delicious\spamspamspam.txt')
'c:\\delicious\\spamspamspam.txt'
>>> shutil.copytree('c:\\delicious','c:\\delicious_backup')
'c:\\delicious_backup'
>>> shutil.move('c:\\spam\\spam.txt', 'c:\\delicious\\cake')
'c:\\delicious\\cake\\spam.txt'
>>> #renaming -
>>> shutil.move('c:\\delicious\\cake\\spam.txt, c:\\delicious\\cake\\zdzislaw.txt')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    shutil.move('c:\\delicious\\cake\\spam.txt, c:\\delicious\\cake\\zdzislaw.txt')
TypeError: move() missing 1 required positional argument: 'dst'
>>> shutil.move('c:\\delicious\\cake\\spam.txt, 'c:\\delicious\\cake\\zdzislaw.txt')
		
SyntaxError: invalid syntax
>>> shutil.move('c:\\delicious\\cake\\spam.txt', 'c:\\delicious\\cake\\zdzislaw.txt')
		
'c:\\delicious\\cake\\zdzislaw.txt'
>>> 
