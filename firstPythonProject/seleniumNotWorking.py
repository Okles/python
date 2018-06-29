Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
Traceback (most recent call last):
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\selenium\webdriver\common\service.py", line 76, in start
    stdin=PIPE)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\subprocess.py", line 997, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] Nie można odnaleźć określonego pliku

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    browser = webdriver.Firefox()
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\selenium\webdriver\firefox\webdriver.py", line 160, in __init__
    self.service.start()
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 

>>> from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
>>> binary = FirefoxBinary(r'‪C:\Program Files\Mozilla Firefox\firefox.exe')
>>> browser = webdriver.Firefox(firefox_binary=binary)
Traceback (most recent call last):
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\selenium\webdriver\common\service.py", line 76, in start
    stdin=PIPE)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\subprocess.py", line 997, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] Nie można odnaleźć określonego pliku

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    browser = webdriver.Firefox(firefox_binary=binary)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\selenium\webdriver\firefox\webdriver.py", line 160, in __init__
    self.service.start()
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 

>>> 
