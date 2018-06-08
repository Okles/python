import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)  # disables this level and below

'''
Available levels:
DEBUG
INFO
WARNING
ERROR 
CRITICAL
'''
logging.debug('Beginning of a program')


def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.critical('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total


print(factorial(5))


logging.debug('End of program')
