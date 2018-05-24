name = 'Lukasz'
place = 'Warsaw'
time = '2pm'
food = 'pizza'
print('Hello ' + name + ' you are invited to a party in ' + place + ' at ' + time +
      '. Please bring ' + food + '.')

#can be replaced by:

print('Hello %s, you are invited to a party in %s at %s. Please bring %s.' % (name, place, time, food))