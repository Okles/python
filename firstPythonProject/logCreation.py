Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import traceback
>>> try:
	raise Exception('Some error message')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_ext())
	errorFile.close()
	print('A trace has been saved into an error_log.txt file')

	
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    raise Exception('Some error message')
Exception: Some error message

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#8>", line 5, in <module>
    errorFile.write(traceback.format_ext())
AttributeError: module 'traceback' has no attribute 'format_ext'
>>> import traceback
>>> > try:
	raise Exception('Some error message')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('A trace has been saved into an error_log.txt file')
	
SyntaxError: invalid syntax
>>> try:
	raise Exception('Some error message')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('A trace has been saved into an error_log.txt file')

	
108
A trace has been saved into an error_log.txt file
>>> 
