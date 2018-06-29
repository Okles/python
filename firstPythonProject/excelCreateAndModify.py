Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##creating and modifying excel sheets
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb
<openpyxl.workbook.workbook.Workbook object at 0x02593B90>
>>> wb.get_sheet_names()

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: Call to deprecated function get_sheet_names (Use wb.sheetnames).
['Sheet']
>>> wb.sheetnames()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    wb.sheetnames()
TypeError: 'list' object is not callable
>>> wb.sheetnames
['Sheet']
>>> sheet['A1'] == 42
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sheet['A1'] == 42
NameError: name 'sheet' is not defined
>>> sheet = wb.sheetnames
>>> sheet['A1'] == 42
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sheet['A1'] == 42
TypeError: list indices must be integers or slices, not str
>>> sheet['A2'] == 'Hello'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sheet['A2'] == 'Hello'
TypeError: list indices must be integers or slices, not str
>>> wb.sheetname
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    wb.sheetname
AttributeError: 'Workbook' object has no attribute 'sheetname'
>>> sheet = wb.get_sheet_by_name('Sheet')

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> wb.sheetname('Sheet')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    wb.sheetname('Sheet')
AttributeError: 'Workbook' object has no attribute 'sheetname'
>>> wb['Sheet']
<Worksheet "Sheet">
>>> sheet['A1'].value
>>> sheet['A1'].value == None
True
>>> sheet['A1'] = 42
>>> sheet['A2'] = 'Hello'
>>> 
>>> 
>>> import os
>>> os.chdir(r'C:\examples')
>>> wb.save('newFile.xlsx')
>>> sheet2 = wb.create_sheet()
>>> wb.sheetnames
['Sheet', 'Sheet1']
>>> sheet2.title
'Sheet1'
>>> sheet2.title = 'Sheet2'
>>> wb.sheetnames
['Sheet', 'Sheet2']
>>> wb.save('newFile.xlsx')
>>> wb.create_sheet(index = 0, title = 'Other Sheet')
<Worksheet "Other Sheet">
>>> wb.save('newerFile.xlsx')
>>> 
