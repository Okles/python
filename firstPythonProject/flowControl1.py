print('What is your name?: ')
name = input()

if name == 'Lukasz':
    print('Hi ' + name + '. Access granted!')
elif name != 'Lukasz':
    print('Hi ' + name)
    print('You are not Lukasz, closing an app!')