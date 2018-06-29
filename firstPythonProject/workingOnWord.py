Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import docx
>>> doc.Document(r'C:\examples\demo.docx')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    doc.Document(r'C:\examples\demo.docx')
NameError: name 'doc' is not defined
>>> d = doc.Document(r'C:\examples\demo.docx')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d = doc.Document(r'C:\examples\demo.docx')
NameError: name 'doc' is not defined
>>> d = docx.Document(r'C:\examples\demo.docx')
>>> d.paragraphs
[<docx.text.paragraph.Paragraph object at 0x03AFDED0>, <docx.text.paragraph.Paragraph object at 0x03AFDF10>, <docx.text.paragraph.Paragraph object at 0x03AFDF30>, <docx.text.paragraph.Paragraph object at 0x03AFDF70>, <docx.text.paragraph.Paragraph object at 0x03AFDFB0>, <docx.text.paragraph.Paragraph object at 0x03AFDCF0>, <docx.text.paragraph.Paragraph object at 0x03AFDDB0>]
>>> d.paragraphs[0]
<docx.text.paragraph.Paragraph object at 0x03AFDB70>
>>> d.paragraphs[0].textg
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d.paragraphs[0].textg
AttributeError: 'Paragraph' object has no attribute 'textg'
>>> d.paragraphs[0].text
'Document Title'
>>> p = d.paragraphs[1]
>>> p.runs
[<docx.text.run.Run object at 0x03AFDF10>, <docx.text.run.Run object at 0x03AFDCF0>, <docx.text.run.Run object at 0x03AFDE10>, <docx.text.run.Run object at 0x03AFDED0>, <docx.text.run.Run object at 0x03AFDB70>]
>>> p.runs[0].text
'A plain paragraph with'
>>> p.runs[1].text
' some '
>>> p.runs[2].text
'bold'
>>> p.runs[3].text
' and some '
>>> p.runs[4].text
'italic'
>>> p.runs[5].text
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    p.runs[5].text
IndexError: list index out of range
>>> p.runs[4].bold
>>> p.runs[4].bold == None
True
>>> p.runs[4].underline == None
True
>>> p.runs[3].text = 'italic and underlined'
>>> d.save(r'C:\examples\demo2.docx')
>>> p.runs[3].underline = True
>>> d.save(r'C:\examples\demo2.docx')
>>> p.style
_ParagraphStyle('Normal') id: 61857488
>>> p.style = 'Title'
>>> d.save(r'C:\examples\demo3.docx')
>>> d = docx.Document()
>>> d.add_paragraph('Some new paragraph')
<docx.text.paragraph.Paragraph object at 0x03B1FF10>
>>> d.add_paragraph('Another paragraph')
<docx.text.paragraph.Paragraph object at 0x03AFDED0>
>>> d.save(r'C:\examples\demo4.docx')
>>> p = d.paragraphs[0]
>>> p.add_run('This is a new run')
<docx.text.run.Run object at 0x03AFDE50>
>>> p.runs
[<docx.text.run.Run object at 0x03B3B330>, <docx.text.run.Run object at 0x03B3B170>]
>>> p.runs[1].bold = True
>>> d.save(r'C:\examples\demo5.docx')
>>> 
>>> 

>>> 
>>> 

>>> docx.Document()
