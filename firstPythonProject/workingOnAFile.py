# reading a file
fileLocalization = (r'C:\Users\Okles\Documents\PycharmProjects\firstPythonProject\fileLoading.txt')
testFile = open(fileLocalization)
content = testFile.read()
print(content)
testFile.close()

# writing to a file
testFile = open(fileLocalization,'w') #opening a file in a write mode
testFile.write('Writing some things\nIn multiline')
testFile.close()

# appending a file
testFile = open(fileLocalization,'a') #opening a file in a write mode
testFile.write('\n\nAdding some new text')
testFile.close()