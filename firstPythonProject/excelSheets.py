Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import openpyxl
>>> import os
>>> os.chdir('c:\\examples')
>>> workbook = openpyxl.load_workbook('example.xlsx')
>>> type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> sheet = workbook.get_sheet_by_name('Sheet1')

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> workbook.get_sheet_names()

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: Call to deprecated function get_sheet_names (Use wb.sheetnames).
['Sheet1', 'Sheet2', 'Sheet3']
>>> print(sheet)
<Worksheet "Sheet1">
>>> print(workbook.sheetnames)
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet['A1']
<Cell 'Sheet1'.A1>
>>> cell = sheet['A1']
>>> cell.value
datetime.datetime(2015, 4, 5, 13, 34, 2)
>>> str(cell.value)
'2015-04-05 13:34:02'
>>> cell = (\sheet['A1'].value)
SyntaxError: unexpected character after line continuation character
>>> cell = (sheet['A1'].value)
>>> sheet['A1'].value
datetime.datetime(2015, 4, 5, 13, 34, 2)
>>> sheet['C2'].value
85
>>> sheet.cell(row=1, column=2)
<Cell 'Sheet1'.B1>
>>> sheet.cell(row=1, column=2).value
'Apples'
>>> 
>>> for i in range(1,8):
	print(i, sheet.cell(row=i, column=2).value)

	
1 Apples
2 Cherries
3 Pears
4 Oranges
5 Apples
6 Bananas
7 Strawberries
>>> 
