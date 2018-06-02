Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> for folderName, subfolders, filenames in os.walk(r'c:\delicious'):
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames inside ' + folderName + ' are: ' + str(filenames))
	print()

	
The folder is c:\delicious
The subfolders in c:\delicious are: ['cake', 'pate']
The filenames inside c:\delicious are: ['spam.txt', 'spamspamspam.txt']

The folder is c:\delicious\cake
The subfolders in c:\delicious\cake are: []
The filenames inside c:\delicious\cake are: ['cheesecake.txt.txt']

The folder is c:\delicious\pate
The subfolders in c:\delicious\pate are: []
The filenames inside c:\delicious\pate are: ['somepate.txt.txt']

>>> for file in filenames:
	if file.endswith('.txr'):
		shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')
KeyboardInterrupt
>>> import shutil
			    
>>> for file in filenames:
	if file.endswith('.txr'):
		shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')


for file in filenames:
	if file.endswith('.txr'):
		shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')
			    
SyntaxError: invalid syntax
>>> for file in filenames:
			    if file.endswith('.txr'):
			    shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')
					
SyntaxError: expected an indented block
>>> for file in filenames:
			    if file.endswith('.txr'):
				    shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')




KeyboardInterrupt
>>> 
