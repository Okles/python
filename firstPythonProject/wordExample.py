# a program that reads a doc file to a plain string

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []

    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText(r'c:\examples\demo.docx'))
