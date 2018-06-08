# Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
# Type "copyright", "credits" or "license()" for more information.
# >>> import os
# >>> os.sep
# '\\'
# >>> os.getcwd()
# 'C:\\Users\\Okles\\AppData\\Local\\Programs\\Python\\Python36-32'
# >>> os.chdir('c:\\')
# >>> os.getcwd()
# 'c:\\'
# >>> os.chdir('C:\\ProgramData\\blabla'
# 	     )
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     os.chdir('C:\\ProgramData\\blabla'
# FileNotFoundError: [WinError 2] Nie można odnaleźć określonego pliku: 'C:\\ProgramData\\blabla'
# >>> os.chdir('C:\\ProgramData\\')
#
# >>> os.path.abspath('spam.png')
#
# 'C:\\ProgramData\\spam.png'
# >>> os.path.abspath('..\\..\\spam.png')
#
# 'C:\\spam.png'
# >>> os.path.isabs('..\spam.png')
#
# False
# >>> os.path.isabs('c:\\spam.png')
#
# True
# >>> os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
#
# 'folder2\\spam.png'
# >>> os.path.dirname('c:\\folder1\\folder2\\spam.png')
#
# 'c:\\folder1\\folder2'
# >>> os.path.basename('c:\\folder1\\folder2\\spam.png')
#
# 'spam.png'
# >>> os.path.isfile('c:\\folder1\\folder2\\spam.png')
#
# False
# >>> os.path.isdir('c:\\folder1\\folder2')
#
# False
# >>> os.path.isdir('c:\\windows\\')
#
# True
# >>> os.path.getsize('c:\\windows\\system32\\calc.exe')
#
# 816128
# >>> os.listdir('c:\\users\\')
#
# ['All Users', 'Default', 'Default User', 'desktop.ini', 'MsDtsServer110', 'MSSQLFDLauncher', 'MSSQLSERVER', 'MSSQLServerOLAPService', 'Okles', 'Public', 'ReportServer', 'Tata', 'XFrostPL']
# >>>
#
# >>>
#
# >>> totalSize = 0
#
# >>> for filename in os.listdir('c:\\windows'):
# 	     if os.path.isfile(os.path.join('c:\\windows', filename)):
# 		     continue
# 	     totalSize = totalSize + os.path.getsize(os.path.join('c:\\windows', filename))
#
#
# >>> totalsize
#
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     totalsize
# NameError: name 'totalsize' is not defined
# >>> totalSize
#
# 20103168
# >>> os.makedirs('c:\\delicious\\cake')
#
# >>> os.listdir(..)
#
# SyntaxError: invalid syntax
# >>> os.listdir('..')
#
# ['$Recycle.Bin', '$SysReset', 'AMD', 'bootmgr', 'BOOTNXT', 'chromedriver.exe', 'Config.Msi', 'cpuz', 'delicious', 'Documents and Settings', 'eclipse', 'found.000', 'Fraps', 'gacutil', 'geckodriver.exe', 'GOG Games', 'GrandeDevice', 'hiberfil.sys', 'inetpub', 'Install.log', 'Intel', 'LGH815', 'logs', 'MSI Afterburner', 'MSOCache', 'ohydny.wav', 'PerfLogs', 'Phaser_3010', 'Program Files', 'Program Files (x86)', 'ProgramData', 'score.wps', 'selenium-java-3.7.1', 'selenium-server-standalone-3.8.1.jar', 'sparkraw.log', 'swapfile.sys', 'System Volume Information', 'Temp', 'totalcmd', 'Users', 'Windows', 'Windows.old', 'Xerox', 'XeroxPhaser_3010']
# >>>
