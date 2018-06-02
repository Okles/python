#! python3

import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345 
(
((\d\d\d) | (\d\d\d\)))?     # area code (optional)
(\s|-)   # first separator
 \d\d\d   # first 3 digits
-    # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x) # extension (optional) word part
(\d{2,5}))?   # extension (optional) number part
) # putting everything in a big group so that it's not returned in two-poles
''',re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@something.com

[a-zA-Z0-9_.+]+   # name part
@    # @ symbol
[a-zA-Z0-9_.+]+   # domain name
''',re.VERBOSE)

# ODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0]) #first string only from i.e. '501-371-2026', '501', '501', '', '-', '', '', '', '', ''

# for debug only
print(allPhoneNumbers)
print(extractedEmail)

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n'.join(extractedEmail) #one phone number and email per line
pyperclip.copy(results)