Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import imapclient
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import imapclient
ModuleNotFoundError: No module named 'imapclient'
>>> import imapclient
>>> conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
>>> conn.login('babolerazm@gmail.com', 'waldekmirek')
b'babolerazm@gmail.com authenticated (Success)'
>>> conn.select_folder('INBOX'), readonly=True)
SyntaxError: invalid syntax
>>> conn.select_folder('INBOX', readonly=True)
{b'PERMANENTFLAGS': (), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing'), b'UIDVALIDITY': 1, b'EXISTS': 266, b'RECENT': 0, b'UIDNEXT': 267, b'HIGHESTMODSEQ': 16460, b'READ-ONLY': [b'']}
>>> conn.search(['SINCE 10-Jan-2018'])
Traceback (most recent call last):
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 882, in _search
    data = self._raw_command_untagged(b'SEARCH', args)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1266, in _raw_command_untagged
    typ, data = self._raw_command(command, args, uid=uid)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1328, in _raw_command
    return self._imap._command_complete(to_unicode(command), tag)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\imaplib.py", line 1022, in _command_complete
    raise self.error('%s command error: %s %s' % (name, typ, data))
imaplib.IMAP4.error: SEARCH command error: BAD [b'Could not parse command']

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    conn.search(['SINCE 10-Jan-2018'])
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 857, in search
    return self._search(criteria, charset)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 895, in _search
    criteria='"%s"' % criteria if not isinstance(criteria, list) else criteria
imapclient.exceptions.InvalidCriteriaError: b'Could not parse command'

This error may have been caused by a syntax error in the criteria: ['SINCE 10-Jan-2018']
Please refer to the documentation for more information about search criteria syntax..
https://imapclient.readthedocs.io/en/master/#imapclient.IMAPClient.search
>>> UIDs = conn.search(['from: babolerazm@gmail.com '])
Traceback (most recent call last):
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 882, in _search
    data = self._raw_command_untagged(b'SEARCH', args)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1266, in _raw_command_untagged
    typ, data = self._raw_command(command, args, uid=uid)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1328, in _raw_command
    return self._imap._command_complete(to_unicode(command), tag)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\imaplib.py", line 1022, in _command_complete
    raise self.error('%s command error: %s %s' % (name, typ, data))
imaplib.IMAP4.error: SEARCH command error: BAD [b'Could not parse command']

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    UIDs = conn.search(['from: babolerazm@gmail.com '])
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 857, in search
    return self._search(criteria, charset)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 895, in _search
    criteria='"%s"' % criteria if not isinstance(criteria, list) else criteria
imapclient.exceptions.InvalidCriteriaError: b'Could not parse command'

This error may have been caused by a syntax error in the criteria: ['from: babolerazm@gmail.com ']
Please refer to the documentation for more information about search criteria syntax..
https://imapclient.readthedocs.io/en/master/#imapclient.IMAPClient.search
>>> UIDs = conn.search(['from: babolerazm@gmail.com'])
Traceback (most recent call last):
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 882, in _search
    data = self._raw_command_untagged(b'SEARCH', args)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1266, in _raw_command_untagged
    typ, data = self._raw_command(command, args, uid=uid)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1328, in _raw_command
    return self._imap._command_complete(to_unicode(command), tag)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\imaplib.py", line 1022, in _command_complete
    raise self.error('%s command error: %s %s' % (name, typ, data))
imaplib.IMAP4.error: SEARCH command error: BAD [b'Could not parse command']

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    UIDs = conn.search(['from: babolerazm@gmail.com'])
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 857, in search
    return self._search(criteria, charset)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 895, in _search
    criteria='"%s"' % criteria if not isinstance(criteria, list) else criteria
imapclient.exceptions.InvalidCriteriaError: b'Could not parse command'

This error may have been caused by a syntax error in the criteria: ['from: babolerazm@gmail.com']
Please refer to the documentation for more information about search criteria syntax..
https://imapclient.readthedocs.io/en/master/#imapclient.IMAPClient.search
>>> UIDs = conn.search('(SINCE "01-Jan-2016" BEFORE "02-Jan-2017")')
>>> UIDs = conn.search('(SINCE "01-Jan-2016")')
>>> UIDs
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266]
>>> rawMessage = conn.fetch([120], ['BODY[]', 'FLAGS'])
>>> import pyzmail
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    import pyzmail
ModuleNotFoundError: No module named 'pyzmail'
>>> import pyzmail
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import pyzmail
ModuleNotFoundError: No module named 'pyzmail'
>>> import pyzmail
>>> conn.fetch([120], ['BODY[]', 'FLAGS'])
defaultdict(<class 'dict'>, {120: {b'SEQ': 120, b'FLAGS': (), b'BODY[]': b'Delivered-To: babolerazm@gmail.com\r\nReceived: by 10.74.117.67 with SMTP id g3csp2856654oof;\r\n        Mon, 2 Apr 2018 11:33:58 -0700 (PDT)\r\nX-Google-Smtp-Source: AIpwx4/dMlsHt+11Wl4zPHj2TFs0BKM0u2OrudoqpwCNJ1vOwq7ceI8Xo9Er07w8zF4tw3wcdt2m\r\nX-Received: by 2002:a24:d309:: with SMTP id n9-v6mr2240092itg.0.1522694038407;\r\n        Mon, 02 Apr 2018 11:33:58 -0700 (PDT)\r\nARC-Seal: i=1; a=rsa-sha256; t=1522694038; cv=none;\r\n        d=google.com; s=arc-20160816;\r\n        b=HLL/XVjaWUcRcCaRMSKuphjoHRCv/4RegyNT8rs3s3D7rRwFLQYOT4DlSIAgY6m4GE\r\n         dcvgiZlTh3Kg4SOkXSwnzuzzjcj7JYzkM3a9bplVRABUAQ5BRdqSuofBmT8X3U1iZlN7\r\n         2jSCyPTpnaH+IEdmi++1uVa8rRjS+isbacXGqVC38EMqXCSE8cliFP+C3s93iB78ozIA\r\n         wxlBKqmoEGkUD7L6NWNwvm/+05RRq1uMMPO1I1g56Nkt2Byzvr3cQeImKftLMKKTTji/\r\n         xDbjK50JbUM/KO8UkO5qFhjO+vKcprRLJ8VZ+pedG640aicNyG1aUlp1pOLmeglOcIZk\r\n         NaWg==\r\nARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\r\n        h=mime-version:message-id:feedback-id:list-unsubscribe:errors-to\r\n         :reply-to:from:subject:to:date:dkim-signature\r\n         :arc-authentication-results;\r\n        bh=ifXQLFeFWFUWjqYtoIZUVLwkbmLXbOHLhRx4zOYuToQ=;\r\n        b=c8g8W/IJj6E8+FEFZdzmcj2Wt0lJ6eRFMMVkii2jbcvZaPYoAfTN8cuyYL+bMDeiQl\r\n         FMlccXqs23Qg4J/lj2Zo0XM2nKoxlQ8EXmUMYuJSDAzf2Qch9JL4BUzvcf6/7TykiYrZ\r\n         p6TarTq4iu1dIyvuCmjC3vak8k6sPgnjkJKk+pUw9WcN2PLja+0ii7bQ8BGroYK/qdye\r\n         i2sG2MFC6e0ER+qC7rSsha2pLK9xYYS5XusuA9i9m9GHh52dksLKztFVBcZriaQl2Q4k\r\n         Krc1zOo76V3wWI+gD4oOriz+mvZBx+YTxbfdQ8jc2POaHPQwNjFXuoe/yRJx/mNeNUOM\r\n         LPzg==\r\nARC-Authentication-Results: i=1; mx.google.com;\r\n       dkim=pass header.i=@facebookmail.com header.s=s1024-2013-q3 header.b=n/ij2FVF;\r\n       spf=pass (google.com: domain of notification+kr4wraaagarn@facebookmail.com designates 66.220.155.149 as permitted sender) smtp.mailfrom=notification+kr4wraaagarn@facebookmail.com;\r\n       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=facebookmail.com\r\nReturn-Path: <notification+kr4wraaagarn@facebookmail.com>\r\nReceived: from mx-out.facebook.com (66-220-155-149.mail-mail.facebook.com. [66.220.155.149])\r\n        by mx.google.com with ESMTPS id 196-v6si843579ity.76.2018.04.02.11.33.57\r\n        for <babolerazm@gmail.com>\r\n        (version=TLS1 cipher=ECDHE-RSA-AES128-SHA bits=128/128);\r\n        Mon, 02 Apr 2018 11:33:58 -0700 (PDT)\r\nReceived-SPF: pass (google.com: domain of notification+kr4wraaagarn@facebookmail.com designates 66.220.155.149 as permitted sender) client-ip=66.220.155.149;\r\nAuthentication-Results: mx.google.com;\r\n       dkim=pass header.i=@facebookmail.com header.s=s1024-2013-q3 header.b=n/ij2FVF;\r\n       spf=pass (google.com: domain of notification+kr4wraaagarn@facebookmail.com designates 66.220.155.149 as permitted sender) smtp.mailfrom=notification+kr4wraaagarn@facebookmail.com;\r\n       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=facebookmail.com\r\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=facebookmail.com;\r\n\ts=s1024-2013-q3; t=1522694036;\r\n\tbh=ifXQLFeFWFUWjqYtoIZUVLwkbmLXbOHLhRx4zOYuToQ=;\r\n\th=Date:To:Subject:From:MIME-Version:Content-Type;\r\n\tb=n/ij2FVF/LAC8AQRdpcZPAKTWG1E9Emu0N6f9owtKHyKWNJFdhuMCcqK23d8hjBnR\r\n\t KpUcZUEBBh+qfzQ+gtpgJ2RzkMxzQUCHOjbbPUzhNJUzYB9+y3h3g71fCXEheoBV0U\r\n\t HLxwnAHt2tpPU3ALdbsi4XSMEBodg1AWsP5RoWAE=\r\nReceived: from facebook.com (uizyyjVj43ZWsyFEni9fQ+tmnUkpk5fDP+27Ikb67YAf5tKL+J+jVKLPFSeCGKnR 2401:db00:1030:51cf:face:0000:000b:0000)\r\n by facebook.com with Thrift id 66da07e836a411e8b86f000af7a31f42-b6021dc8;\r\n Mon, 02 Apr 2018 11:33:56 -0700\r\nX-Facebook: from 2401:db00:1030:416b:face:0:72:0 ([MTI3LjAuMC4x]) \r\n\tby async with HTTPS (ZuckMail);\r\nDate: Mon, 2 Apr 2018 11:33:56 -0700\r\nTo: Erazm Babol <babolerazm@gmail.com>\r\nSubject: =?UTF-8?B?RXJhem0sIG1hc3ogMTcg?=\r\n =?UTF-8?B?bm93eWNoIHBvd2lhZG9t?=\r\n =?UTF-8?B?aWXFhCBpIDMgem1pYW55IA==?=\r\n =?UTF-8?B?c3RhdHVzdSBuYSBzdHJv?=\r\n =?UTF-8?B?bmllIGdydXB5?=\r\nX-Priority: 3\r\nX-Mailer: ZuckMail [version 1.00]\r\nReturn-Path: notification+kr4wraaagarn@facebookmail.com\r\nFrom: "Facebook" <notification+kr4wraaagarn@facebookmail.com>\r\nReply-to: noreply <noreply@facebookmail.com>\r\nErrors-To: notification+kr4wraaagarn@facebookmail.com\r\nX-Facebook-Notify: stale_notifications; mailid=568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b\r\nList-Unsubscribe: <https://www.facebook.com/o.php?k=AS1DNL7gofDkZ9x9&u=100024318549518&mid=568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b>\r\nFeedback-ID: 9:stale_notifications:Facebook\r\nX-FACEBOOK-PRIORITY: 1\r\nX-Auto-Response-Suppress: All\r\nMessage-ID: <0d8794ac0d835dfa64119eaa189833f5@async>\r\nMIME-Version: 1.0\r\nContent-Type: multipart/alternative;\r\n\tboundary="b1_0d8794ac0d835dfa64119eaa189833f5"\r\n\r\n\r\n--b1_0d8794ac0d835dfa64119eaa189833f5\r\nContent-Type: text/plain; charset="UTF-8"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=\r\n=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D\r\nPrzejd=C5=BA do Facebooka\r\nhttps://www.facebook.com/n/?aref=3D1522694035641265&medium=3Demail&mid=3D5=\r\n68e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b&bcode=3D2.1522694036.AbxsUlKS9=\r\nhSZawIYLFY&n_m=3Dbabolerazm%40gmail.com&lloc=3D2nd_cta\r\n\r\n\r\nPoka=C5=BC powiadomienia\r\nhttps://www.facebook.com/n/?notifications&aref=3D1522694035641265&medium=\r\n=3Demail&mid=3D568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b&bcode=3D2.1522=\r\n694036.AbxsUlKS9hSZawIYLFY&n_m=3Dbabolerazm%40gmail.com&lloc=3D1st_cta\r\n\r\n=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=\r\n=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D\r\n\r\nWitaj, Erazm!\r\n\r\nWiele si=C4=99 dzia=C5=82o na Facebooku od Twojego ostatniego logowania. =\r\nOto kilka powiadomie=C5=84 od Twoich znajomych, kt=C3=B3re =\r\nprzegapi=C5=82e=C5=9B(a=C5=9B).\r\n\r\n"=C2=A0=C2=A0=C2=A0=C2=A0=C2=A0=C2=A03 zmiany statusu na stronie grupy\r\n=C2=A0=C2=A0=C2=A0=C2=A0=C2=A0=C2=A017 nowych powiadomie=C5=84"\r\n\r\nDzi=C4=99kujemy\r\nZesp=C3=B3=C5=82 Facebooka\r\n\r\n\r\n\r\n=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=\r\n=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D\r\nTa wiadomo=C5=9B=C4=87 zosta=C5=82a wys=C5=82ana na adres =\r\nbabolerazm@gmail.com. Je=C5=9Bli nie chcesz otrzymywa=C4=87 takich =\r\nwiadomo=C5=9Bci e-mail z Facebooka w przysz=C5=82o=C5=9Bci, skorzystaj z =\r\nponi=C5=BCszego linku, aby zrezygnowa=C4=87 z subskrypcji.\r\nhttps://www.facebook.com/o.php?k=3DAS1DNL7gofDkZ9x9&u=3D100024318549518&mi=\r\nd=3D568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b\r\nFacebook, Inc., Attention: Community Support, 1 Hacker Way, Menlo Park, CA =\r\n94025\r\n\r\n\r\n--b1_0d8794ac0d835dfa64119eaa189833f5\r\nContent-Type: text/html; charset="UTF-8"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional =\r\n//EN"><html><head><title>Facebook</title><meta http-equiv=3D"Content-Type" =\r\ncontent=3D"text/html; charset=3Dutf-8" /><style>@media all and (max-width: =\r\n480px){*[class].ib_t{min-width:100% =\r\n!important}*[class].ib_row{display:block =\r\n!important}*[class].ib_ext{display:block !important;padding:10px 0 5px =\r\n0;vertical-align:top !important;width:100% =\r\n!important}*[class].ib_img,*[class].ib_mid{vertical-align:top =\r\n!important}*[class].mb_blk{display:block =\r\n!important;padding-bottom:10px;width:100% =\r\n!important}*[class].mb_hide{display:none =\r\n!important}*[class].mb_inl{display:inline =\r\n!important}*[class].d_mb_flex{display:block !important}}.d_mb_show{display=\r\n:none}.d_mb_show_center{display:table;margin:auto}.d_mb_flex{display:flex}=\r\n@media only screen and (max-device-width: 480px){.d_mb_hide{display:none =\r\n!important}.d_mb_show{display:block !important}.d_mb_flex{display:block =\r\n!important}}.mb_text h1,.mb_text h2,.mb_text h3,.mb_text h4,.mb_text =\r\nh5,.mb_text h6{line-height:normal}.mb_work_text =\r\nh1{font-size:18px;line-height:normal;margin-top:4px}.mb_work_text =\r\nh2,.mb_work_text =\r\nh3{font-size:16px;line-height:normal;margin-top:4px}.mb_work_text =\r\nh4,.mb_work_text h5,.mb_work_text =\r\nh6{font-size:14px;line-height:normal}.mb_work_text =\r\na{color:#1270e9}.mb_work_text p{margin-top:4px}</style></head><body =\r\nstyle=3D"margin:0;padding:0;" dir=3D"ltr" bgcolor=3D"#ffffff"><table =\r\nborder=3D"0" cellspacing=3D"0" cellpadding=3D"0" align=3D"center" =\r\nid=3D"email_table" style=3D"border-collapse:collapse;"><tr><td =\r\nid=3D"email_content" style=3D"font-family:Helvetica Neue,Helvetica,Lucida =\r\nGrande,tahoma,verdana,arial,sans-serif;background:#ffffff;"><table =\r\nborder=3D"0" width=3D"100%" cellspacing=3D"0" cellpadding=3D"0" =\r\nstyle=3D"border-collapse:collapse;"><tr style=3D""><td height=3D"20" =\r\nstyle=3D"line-height:20px;" colspan=3D"3">&nbsp;</td></tr><tr><td =\r\nheight=3D"1" colspan=3D"3" style=3D"line-height:1px;"><span =\r\nstyle=3D"color:#FFFFFF;display:none !important;font-size:1px;">=C2=A0 =\r\nWiele si=C4=99 dzia=C5=82o na Facebooku od Twojego ostatniego logowania. =\r\nOto kilka powiadomie=C5=84 od Twoich znajomych, kt=C3=B3re =\r\nprzegapi=C5=82e=C5=9B(a=C5=9B). =C2=A0 =C2=A0=C2=A0=C2=A0 Erazm Babol =\r\n=C2=A0 =C2=A0 =C2=A0=C2=A0=C2=A0 =C2=A0=C2=A0=C2=A0 3 zmiany statusu na =\r\nstronie grupy =C2=A0 =C2=A0=C2=A0=C2=A0 =C2=A0=C2=A0=C2=A0 17 nowych =\r\npowiadomie=C5=84 =C2=A0 =C2=A0</span></td></tr><tr><td width=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nstyle=3D""><table border=3D"0" width=3D"100%" cellspacing=3D"0" =\r\ncellpadding=3D"0" style=3D"border-collapse:collapse;"><tr style=3D""><td =\r\nheight=3D"16" style=3D"line-height:16px;" =\r\ncolspan=3D"3">&nbsp;</td></tr><tr><td width=3D"32" align=3D"left" =\r\nvalign=3D"middle" style=3D"height:32;line-height:0px;"><a =\r\nhref=3D"https://www.facebook.com/n/?find-friends%2Fbrowser%2F&amp;aref=3D1=\r\n522694035641265&amp;medium=3Demail&amp;mid=3D568e18b8290dfG5af8b9f9de0eG56=\r\n8e1d51893b1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=3Dbab=\r\nolerazm%40gmail.com&amp;lloc=3Dlogo" =\r\nstyle=3D"color:#3b5998;text-decoration:none;"><img =\r\nsrc=3D"https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/vd4aB0GIe9z.png" =\r\nwidth=3D"32" height=3D"32" style=3D"border:0;" /></a></td><td width=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nwidth=3D"100%" style=3D""><a href=3D"https://www.facebook.com/n/?find-frie=\r\nnds%2Fbrowser%2F&amp;aref=3D1522694035641265&amp;medium=3Demail&amp;mid=3D=\r\n568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b&amp;bcode=3D2.1522694036.Abxs=\r\nUlKS9hSZawIYLFY&amp;n_m=3Dbabolerazm%40gmail.com&amp;lloc=3Dlogo" =\r\nstyle=3D"color:#3b5998;text-decoration:none;font-family:Helvetica =\r\nNeue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:19p=\r\nx;line-height:32px;">Masz nowe powiadomienia.</a></td></tr><tr =\r\nstyle=3D"border-bottom:solid 1px #e5e5e5;"><td height=3D"16" =\r\nstyle=3D"line-height:16px;" colspan=3D"3">&nbsp;</td></tr></table></td><td =\r\nwidth=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td></tr><tr><td =\r\nwidth=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nstyle=3D""><table border=3D"0" width=3D"100%" cellspacing=3D"0" =\r\ncellpadding=3D"0" style=3D"border-collapse:collapse;"><tr style=3D""><td =\r\nheight=3D"28" style=3D"line-height:28px;">&nbsp;</td></tr><tr><td =\r\nstyle=3D""><span class=3D"mb_text" style=3D"font-family:Helvetica =\r\nNeue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16p=\r\nx;line-height:21px;color:#141823;">Wiele si=C4=99 dzia=C5=82o na Facebooku =\r\nod Twojego ostatniego logowania. Oto kilka powiadomie=C5=84 od Twoich =\r\nznajomych, kt=C3=B3re przegapi=C5=82e=C5=9B.</span></td></tr><tr =\r\nstyle=3D""><td height=3D"14" =\r\nstyle=3D"line-height:14px;">&nbsp;</td></tr><tr><td style=3D""><table =\r\nborder=3D"0" width=3D"100%" cellspacing=3D"0" cellpadding=3D"0" =\r\nstyle=3D"border-collapse:collapse;"><tr><td style=3D"font-size:11px;font-f=\r\namily:LucidaGrande,tahoma,verdana,arial,sans-serif;border:solid 1px =\r\n#e5e5e5;border-radius:2px;padding:10px;display:block;"><table border=3D"0" =\r\ncellspacing=3D"0" cellpadding=3D"0" =\r\nstyle=3D"border-collapse:collapse;"><tr><td style=3D""><a =\r\nhref=3D"https://www.facebook.com/n/?find-friends%2Fbrowser%2F&amp;aref=3D1=\r\n522694035641265&amp;medium=3Demail&amp;mid=3D568e18b8290dfG5af8b9f9de0eG56=\r\n8e1d51893b1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=3Dbab=\r\nolerazm%40gmail.com&amp;lloc=3Dprofile_pic" =\r\nstyle=3D"color:#3b5998;text-decoration:none;"><img src=3D"https://scontent=\r\n-ort2-2.xx.fbcdn.net/v/t1.0-1/c188.0.100.100/p100x100/27540175_10776912004=\r\n3706_4426440577620048966_n.jpg?_nc_cat=3D0&amp;_nc_ad=3Dz-m&amp;_nc_cid=3D=\r\n0&amp;oh=3Dba9ec551202e7806143b2da993f434c9&amp;oe=3D5B6B6891" =\r\nwidth=3D"50" height=3D"50" style=3D"border:0;" /></a></td><td width=3D"10" =\r\nstyle=3D"display:block;width:10px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nwidth=3D"100%" style=3D""><table border=3D"0" cellspacing=3D"0" =\r\ncellpadding=3D"0" style=3D"border-collapse:collapse;"><tr><td =\r\nstyle=3D""><a href=3D"https://www.facebook.com/n/?find-friends%2Fbrowser%2=\r\nF&amp;aref=3D1522694035641265&amp;medium=3Demail&amp;mid=3D568e18b8290dfG5=\r\naf8b9f9de0eG568e1d51893b1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9hSZawIYLFY=\r\n&amp;n_m=3Dbabolerazm%40gmail.com&amp;lloc=3Dprofile_pic" =\r\nstyle=3D"color:#141823;text-decoration:none;font-family:Helvetica =\r\nNeue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16p=\r\nx;line-height:21px;font-weight:bold;">Erazm =\r\nBabol</a></td></tr></table></td></tr><tr style=3D""><td height=3D"10" =\r\nstyle=3D"line-height:10px;">&nbsp;</td></tr><tr><td colspan=3D"3" =\r\nstyle=3D""><table border=3D"0" width=3D"100%" cellspacing=3D"0" =\r\ncellpadding=3D"0" align=3D"center" style=3D"border-collapse:collapse;"><tr =\r\nstyle=3D"border-top:solid 1px #e5e5e5;"><td height=3D"15" =\r\nstyle=3D"line-height:15px;">&nbsp;</td></tr><tr><td width=3D"34" =\r\nstyle=3D"display:block;width:34px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nvalign=3D"middle" style=3D""><a href=3D"https://www.facebook.com/n/?notifi=\r\ncations%2F&amp;aref=3D1522694035641265&amp;medium=3Demail&amp;mid=3D568e18=\r\nb8290dfG5af8b9f9de0eG568e1d51893b1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9h=\r\nSZawIYLFY&amp;n_m=3Dbabolerazm%40gmail.com" =\r\nstyle=3D"color:#3b5998;text-decoration:none;"><img =\r\nsrc=3D"https://static.xx.fbcdn.net/rsrc.php/v3/yI/r/0pjqWL1NfkE.png" =\r\nstyle=3D"border:0;" /></a></td><td width=3D"10" =\r\nstyle=3D"display:block;width:10px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nwidth=3D"100%" valign=3D"middle" style=3D""><span class=3D"mb_text" =\r\nstyle=3D"font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana=\r\n,arial,sans-serif;font-size:16px;line-height:21px;color:#141823;"><a =\r\nhref=3D"https://www.facebook.com/n/?notifications%2F&amp;aref=3D1522694035=\r\n641265&amp;medium=3Demail&amp;mid=3D568e18b8290dfG5af8b9f9de0eG568e1d51893=\r\nb1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=3Dbabolerazm%4=\r\n0gmail.com" style=3D"color:#3b5998;text-decoration:none;"><b>3</b> zmiany =\r\nstatusu na stronie grupy</a></span></td></tr><tr style=3D""><td =\r\nheight=3D"3" style=3D"line-height:3px;">&nbsp;</td></tr><tr><td =\r\nwidth=3D"34" =\r\nstyle=3D"display:block;width:34px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nvalign=3D"middle" style=3D""><a href=3D"https://www.facebook.com/n/?notifi=\r\ncations%2F&amp;aref=3D1522694035641265&amp;medium=3Demail&amp;mid=3D568e18=\r\nb8290dfG5af8b9f9de0eG568e1d51893b1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9h=\r\nSZawIYLFY&amp;n_m=3Dbabolerazm%40gmail.com" =\r\nstyle=3D"color:#3b5998;text-decoration:none;"><img =\r\nsrc=3D"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/xYUm9_Gy-Oy.gif" =\r\nstyle=3D"border:0;" /></a></td><td width=3D"10" =\r\nstyle=3D"display:block;width:10px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nwidth=3D"100%" valign=3D"middle" style=3D""><span class=3D"mb_text" =\r\nstyle=3D"font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana=\r\n,arial,sans-serif;font-size:16px;line-height:21px;color:#141823;"><a =\r\nhref=3D"https://www.facebook.com/n/?notifications%2F&amp;aref=3D1522694035=\r\n641265&amp;medium=3Demail&amp;mid=3D568e18b8290dfG5af8b9f9de0eG568e1d51893=\r\nb1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=3Dbabolerazm%4=\r\n0gmail.com" style=3D"color:#3b5998;text-decoration:none;"><b>17</b> nowych =\r\npowiadomie=C5=84</a></span></td></tr><tr style=3D""><td height=3D"3" =\r\nstyle=3D"line-height:3px;">&nbsp;</td></tr></table></td></tr></table></td>=\r\n</tr></table></td></tr><tr style=3D""><td height=3D"14" =\r\nstyle=3D"line-height:14px;">&nbsp;</td></tr></table></td><td width=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td></tr><tr><td =\r\nwidth=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nstyle=3D""><table border=3D"0" width=3D"100%" cellspacing=3D"0" =\r\ncellpadding=3D"0" style=3D"border-collapse:collapse;"><tr style=3D""><td =\r\nheight=3D"2" style=3D"line-height:2px;" =\r\ncolspan=3D"3">&nbsp;</td></tr><tr><td class=3D"mb_blk" style=3D""><a =\r\nhref=3D"https://www.facebook.com/n/?aref=3D1522694035641265&amp;medium=3De=\r\nmail&amp;mid=3D568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b&amp;bcode=3D2.=\r\n1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=3Dbabolerazm%40gmail.com&amp;lloc=\r\n=3D2nd_cta" style=3D"color:#3b5998;text-decoration:none;"><table =\r\nborder=3D"0" width=3D"100%" cellspacing=3D"0" cellpadding=3D"0" =\r\nstyle=3D"border-collapse:collapse;"><tr><td style=3D"border-collapse:colla=\r\npse;border-radius:2px;text-align:center;display:block;border:solid 1px =\r\n#c9ccd1;box-shadow:0 1px 0 rgba(0, 0, 0, =\r\n0.04);background:#f6f7f8;padding:7px 16px 11px 16px;"><a =\r\nhref=3D"https://www.facebook.com/n/?aref=3D1522694035641265&amp;medium=3De=\r\nmail&amp;mid=3D568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b&amp;bcode=3D2.=\r\n1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=3Dbabolerazm%40gmail.com&amp;lloc=\r\n=3D2nd_cta" =\r\nstyle=3D"color:#3b5998;text-decoration:none;display:block;"><center><font =\r\nsize=3D"3"><span style=3D"font-family:Helvetica Neue,Helvetica,Lucida =\r\nGrande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold=\r\n;vertical-align:middle;color:#525252;text-shadow:0 1px 0 =\r\n#ffffff;font-size:14px;line-height:14px;">Przejd=C5=BA&nbsp;do&nbsp;Facebo=\r\noka</span></font></center></a></td></tr></table></a></td><td width=3D"10" =\r\nstyle=3D"display:block;width:10px;" =\r\nclass=3D"mb_hide">&nbsp;&nbsp;&nbsp;</td><td class=3D"mb_blk" =\r\nstyle=3D""><a href=3D"https://www.facebook.com/n/?notifications&amp;aref=\r\n=3D1522694035641265&amp;medium=3Demail&amp;mid=3D568e18b8290dfG5af8b9f9de0=\r\neG568e1d51893b1G32b&amp;bcode=3D2.1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=\r\n=3Dbabolerazm%40gmail.com&amp;lloc=3D1st_cta" =\r\nstyle=3D"color:#3b5998;text-decoration:none;"><table border=3D"0" =\r\nwidth=3D"100%" cellspacing=3D"0" cellpadding=3D"0" =\r\nstyle=3D"border-collapse:collapse;"><tr><td style=3D"border-collapse:colla=\r\npse;border-radius:2px;text-align:center;display:block;border:solid 1px =\r\n#344c80;box-shadow:inset 0 1px 1px rgba(255, 255, 255, 0.1),0 1px 0 =\r\nrgba(0, 0, 0, 0.1);background:#4c649b;padding:7px 16px 11px 16px;"><a =\r\nhref=3D"https://www.facebook.com/n/?notifications&amp;aref=3D1522694035641=\r\n265&amp;medium=3Demail&amp;mid=3D568e18b8290dfG5af8b9f9de0eG568e1d51893b1G=\r\n32b&amp;bcode=3D2.1522694036.AbxsUlKS9hSZawIYLFY&amp;n_m=3Dbabolerazm%40gm=\r\nail.com&amp;lloc=3D1st_cta" =\r\nstyle=3D"color:#3b5998;text-decoration:none;display:block;"><center><font =\r\nsize=3D"3"><span style=3D"font-family:Helvetica Neue,Helvetica,Lucida =\r\nGrande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold=\r\n;vertical-align:middle;color:#ffffff;text-shadow:0 -1px 0 =\r\n#415686;font-size:14px;line-height:14px;">Poka=C5=BC&nbsp;powiadomienia</s=\r\npan></font></center></a></td></tr></table></a></td><td width=3D"100%" =\r\nclass=3D"mb_hide" style=3D""></td></tr><tr style=3D""><td height=3D"32" =\r\nstyle=3D"line-height:32px;" colspan=3D"3">&nbsp;</td></tr></table></td><td =\r\nwidth=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td></tr><tr><td =\r\nwidth=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td =\r\nstyle=3D""><table border=3D"0" width=3D"100%" cellspacing=3D"0" =\r\ncellpadding=3D"0" align=3D"left" style=3D"border-collapse:collapse;"><tr =\r\nstyle=3D"border-top:solid 1px #e5e5e5;"><td height=3D"16" =\r\nstyle=3D"line-height:16px;">&nbsp;</td></tr><tr><td =\r\nstyle=3D"font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana=\r\n,arial,sans-serif;font-size:11px;color:#aaaaaa;line-height:16px;">Ta =\r\nwiadomo=C5=9B=C4=87 zosta=C5=82a wys=C5=82ana na adres <a =\r\nhref=3D"mailto:babolerazm&#064;gmail.com" style=3D"color:#3b5998;text-deco=\r\nration:none;">babolerazm&#064;gmail.com</a>. Je=C5=9Bli nie chcesz =\r\notrzymywa=C4=87 takich wiadomo=C5=9Bci e-mail z Facebooka w =\r\nprzysz=C5=82o=C5=9Bci, <a href=3D"https://www.facebook.com/o.php?k=3DAS1DN=\r\nL7gofDkZ9x9&amp;u=3D100024318549518&amp;mid=3D568e18b8290dfG5af8b9f9de0eG5=\r\n68e1d51893b1G32b" style=3D"color:#3b5998;text-decoration:none;">zrezygnuj =\r\nz subskrypcji</a>.<br />Facebook, Inc., Attention: Community Support, 1 =\r\nHacker Way, Menlo Park, CA 94025</td></tr></table></td><td width=3D"15" =\r\nstyle=3D"display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td></tr><tr =\r\nstyle=3D""><td height=3D"20" style=3D"line-height:20px;" =\r\ncolspan=3D"3">&nbsp;</td></tr></table><span style=3D""><img =\r\nsrc=3D"https://www.facebook.com/email_open_log_pic.php?mid=3D568e18b8290df=\r\nG5af8b9f9de0eG568e1d51893b1G32b" style=3D"border:0;width:1px;height:1px;" =\r\n/></span></td></tr></table></body></html>\r\n\r\n\r\n\r\n--b1_0d8794ac0d835dfa64119eaa189833f5--\r\n\r\n'}})
>>> pyzmail.PyzMessage.factory(rawMessage[120][b'BODY[]'])
<pyzmail.parse.PyzMessage object at 0x033CAE70>
>>> message = pyzmail.PyzMessage.factory(rawMessage[120][b'BODY[]'])
>>> message.get_subject()
'Erazm, masz 17 nowych powiadomień i 3 zmiany statusu na stronie grupy'
>>> message.get_addresses('from')
[('Facebook', 'notification+kr4wraaagarn@facebookmail.com')]
>>> #checking what type of an email was it
>>> message.text_part
MailPart<*text/plain charset=UTF-8 len=1275>
>>> message.html_part
MailPart<*text/html charset=UTF-8 len=13284>
>>> message.text_part.get_payload().decode('UTF-8')
'========================================\r\nPrzejdź do Facebooka\r\nhttps://www.facebook.com/n/?aref=1522694035641265&medium=email&mid=568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b&bcode=2.1522694036.AbxsUlKS9hSZawIYLFY&n_m=babolerazm%40gmail.com&lloc=2nd_cta\r\n\r\n\r\nPokaż powiadomienia\r\nhttps://www.facebook.com/n/?notifications&aref=1522694035641265&medium=email&mid=568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b&bcode=2.1522694036.AbxsUlKS9hSZawIYLFY&n_m=babolerazm%40gmail.com&lloc=1st_cta\r\n\r\n========================================\r\n\r\nWitaj, Erazm!\r\n\r\nWiele się działo na Facebooku od Twojego ostatniego logowania. Oto kilka powiadomień od Twoich znajomych, które przegapiłeś(aś).\r\n\r\n"\xa0\xa0\xa0\xa0\xa0\xa03 zmiany statusu na stronie grupy\r\n\xa0\xa0\xa0\xa0\xa0\xa017 nowych powiadomień"\r\n\r\nDziękujemy\r\nZespół Facebooka\r\n\r\n\r\n\r\n========================================\r\nTa wiadomość została wysłana na adres babolerazm@gmail.com. Jeśli nie chcesz otrzymywać takich wiadomości e-mail z Facebooka w przyszłości, skorzystaj z poniższego linku, aby zrezygnować z subskrypcji.\r\nhttps://www.facebook.com/o.php?k=AS1DNL7gofDkZ9x9&u=100024318549518&mid=568e18b8290dfG5af8b9f9de0eG568e1d51893b1G32b\r\nFacebook, Inc., Attention: Community Support, 1 Hacker Way, Menlo Park, CA 94025\r\n\r\n'
>>> conn.list_folders()
[((b'\\HasNoChildren',), b'/', 'INBOX'), ((b'\\HasChildren', b'\\Noselect'), b'/', '[Gmail]'), ((b'\\HasNoChildren', b'\\Trash'), b'/', '[Gmail]/Kosz'), ((b'\\Flagged', b'\\HasNoChildren'), b'/', '[Gmail]/Oznaczone gwiazdką'), ((b'\\HasNoChildren', b'\\Junk'), b'/', '[Gmail]/Spam'), ((b'\\HasNoChildren', b'\\Important'), b'/', '[Gmail]/Ważne'), ((b'\\Drafts', b'\\HasNoChildren'), b'/', '[Gmail]/Wersje robocze'), ((b'\\All', b'\\HasNoChildren'), b'/', '[Gmail]/Wszystkie'), ((b'\\HasNoChildren', b'\\Sent'), b'/', '[Gmail]/Wysłane')]
>>> # deleting an email
>>> conn.select_folder('INBOX', readonly=False)
{b'PERMANENTFLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing', b'\\*'), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing'), b'UIDVALIDITY': 1, b'EXISTS': 266, b'RECENT': 0, b'UIDNEXT': 267, b'HIGHESTMODSEQ': 16478, b'READ-WRITE': True}
>>> UIDs = conn.search(['ON 29-Jun-2018'])
Traceback (most recent call last):
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 882, in _search
    data = self._raw_command_untagged(b'SEARCH', args)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1266, in _raw_command_untagged
    typ, data = self._raw_command(command, args, uid=uid)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 1328, in _raw_command
    return self._imap._command_complete(to_unicode(command), tag)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\imaplib.py", line 1022, in _command_complete
    raise self.error('%s command error: %s %s' % (name, typ, data))
imaplib.IMAP4.error: SEARCH command error: BAD [b'Could not parse command']

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    UIDs = conn.search(['ON 29-Jun-2018'])
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 857, in search
    return self._search(criteria, charset)
  File "C:\Users\Okles\AppData\Local\Programs\Python\Python36-32\lib\site-packages\imapclient\imapclient.py", line 895, in _search
    criteria='"%s"' % criteria if not isinstance(criteria, list) else criteria
imapclient.exceptions.InvalidCriteriaError: b'Could not parse command'

This error may have been caused by a syntax error in the criteria: ['ON 29-Jun-2018']
Please refer to the documentation for more information about search criteria syntax..
https://imapclient.readthedocs.io/en/master/#imapclient.IMAPClient.search
>>> conn.delete_messages(266)
{266: (b'\\Seen', b'\\Deleted')}
>>> 