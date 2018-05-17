def div32by(divideBy):
    try:
        return  32/ divideBy
    except ZeroDivisionError:
        print('ERROR! You cannot divide by zero!')

print(div32by(5))
print(div32by(4))
print(div32by(6))
print(div32by(0))
print(div32by(14))


def howManyCars(numOfCars):
    print('How many cars do you have? :')
    numOfCars = input()
    try:
        if int(numOfCars) >=3:
            print(numOfCars +' is quite a lot of cars!')
        else:
            print(numOfCars +' is not so many cars!')
    except ValueError:
        print('You did not enter a valid number!')


print(howManyCars(1))