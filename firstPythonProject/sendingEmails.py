Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import smtplib
>>> conn = smtplib.SMPT('smtp.gmail.com', 587)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    conn = smtplib.SMPT('smtp.gmail.com', 587)
AttributeError: module 'smtplib' has no attribute 'SMPT'
>>> conn = smtplib.SMTP('smtp.gmail.com', 587)
>>> type(conn)
<class 'smtplib.SMTP'>
>>> conn
<smtplib.SMTP object at 0x02F6A870>
>>> conn.hello()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    conn.hello()
AttributeError: 'SMTP' object has no attribute 'hello'
>>> conn.ehlo()
(250, b'smtp.gmail.com at your service, [93.105.177.191]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
>>> conn.starttls()
(220, b'2.0.0 Ready to start TLS')
>>> conn.login('login@gmail.com', 'password')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    conn.login('login@gmail.com', 'password')
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\smtplib.py", line 730, in login
    raise last_exception
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbtY\n5.7.14 TOVZnWxxluKPCqzui9pVy2sVFzh6GKnRLXQAsBCK0CFvD57pjtujrtfaQ-7gky-CPD3xNE\n5.7.14 0uEKxjGwUrNyFZ2DgGMW5Ee3dp8hEo6mx3BZnpn2tuq4iE9VobF_oykSE1yzH5y8ymolF2\n5.7.14 ib2J3iadXy455tINyXUaCzdHb18QwTeT6vApHY-bTaq-RjhNqN6iG8qMVJRl8NrmAbku43\n5.7.14 Lzt6GEXXCyq-feQ8Cb35fP077pDDE> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 o128-v6sm752486lfo.69 - gsmtp')
>>> conn.login('login@gmail.com', 'password')smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbtY\n5.7.14 TOVZnWxxluKPCqzui9pVy2sVFzh6GKnRLXQAsBCK0CFvD57pjtujrtfaQ-7gky-CPD3xNE\n5.7.14 0uEKxjGwUrNyFZ2DgGMW5Ee3dp8hEo6mx3BZnpn2tuq4iE9VobF_oykSE1yzH5y8ymolF2\n5.7.14 ib2J3iadXy455tINyXUaCzdHb18QwTeT6vApHY-bTaq-RjhNqN6iG8qMVJRl8NrmAbku43\n5.7.14 Lzt6GEXXCyq-feQ8Cb35fP077pDDE> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 o128-v6sm752486lfo.69 - gsmtp')
SyntaxError: invalid syntax
>>> conn.login('login@gmail.com', 'password')
(235, b'2.7.0 Accepted')
>>> conn.sendemail('login@gmail.com', 'login@gmail.com', 'Subject: Some test email...\n\nDearblablabla')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    conn.sendemail('login@gmail.com', 'login@gmail.com', 'Subject: Some test email...\n\nDearblablabla')
AttributeError: 'SMTP' object has no attribute 'sendemail'
>>> conn.sendmail('login@gmail.com', 'login@gmail.com', 'Subject: Some test email...\n\nDearblablabla')
{}
>>> conn.quit()
(221, b'2.0.0 closing connection o128-v6sm752486lfo.69 - gsmtp')
>>> 
