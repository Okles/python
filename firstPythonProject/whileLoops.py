count = 0
while count < 5:
    # print('Hello world!')
    count = count + 1
    if count == 3:
        continue
    print('Count is: ' + str(count))

name = ''
# ==========

while True:
    print('Please type your name: ')
    name = input()
    if name == 'Lukasz':
        break

print ('Thank you ' + name)



