def spam():
    eggs = 99
    bacon()
    print(eggs)
    #global variableName creates a global variable inside a function


def bacon():
    ham = 101
    eggs = 0
    print(eggs)


spam()

eggs = 42
print(eggs)