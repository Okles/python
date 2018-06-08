"""
prints something like

***************
*             *
*             *
*             *
***************

"""


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("'Symbol' needs to be a string of length = 1")
    if (width < 2) or (height < 2):
        raise Exception('Height and width have to be more or equal to 2!')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)


# boxPrint('$', 25, 5)
# boxPrint('F', 5, 20)
boxPrint('$$', 25, 5)
boxPrint('$', 1, 1)