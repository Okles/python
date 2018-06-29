Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> requests.get('https://automatetheboringstuff.com/files/rj.txt')
<Response [200]>
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> res.status_code
200
>>> len(res.text)
174130
>>> print(res.text[:500])
ï»¿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org/license


Title: Romeo and Juliet

Author: William Shakespeare

Posting Date: May 25, 2012 [EBook #1112]
Release Date: November, 1997  [Etext #1112]

Language: English


*** S
>>> res.raise_for_status() #raising an exception in case there is download error
			       
>>> badRes = requests.get('blblalalal')
			       
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    badRes = requests.get('blblalalal')
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\requests\api.py", line 72, in get
    return request('get', url, params=params, **kwargs)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\requests\api.py", line 58, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\requests\sessions.py", line 498, in request
    prep = self.prepare_request(req)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\requests\sessions.py", line 441, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\requests\models.py", line 309, in prepare
    self.prepare_url(url, params)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\requests\models.py", line 383, in prepare_url
    raise MissingSchema(error)
requests.exceptions.MissingSchema: Invalid URL 'blblalalal': No schema supplied. Perhaps you meant http://blblalalal?
>>> badRes.raise_for_status()
			       
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    badRes.raise_for_status()
NameError: name 'badRes' is not defined
>>> badRes.requests.get('http://automatetheboringstuff.com/dsadasda')
			       
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    badRes.requests.get('http://automatetheboringstuff.com/dsadasda')
NameError: name 'badRes' is not defined
>>> badRes= requests.get('http://automatetheboringstuff.com/dsadasda')
			       
>>> badRes.raise_for_status()
			       
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    badRes.raise_for_status()
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\requests\models.py", line 939, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://automatetheboringstuff.com/dsadasda
>>> playFile = open('RomeoandJuliet.txt', 'wb')
			       
>>> for chunk in res.iter_content(100000):
	playFile.write(chunk)

			       
100000
74130
>>> playFile.close()
			       
>>> 
