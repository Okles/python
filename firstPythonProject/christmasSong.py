import re

lyrics = '''12 Drummers Drumming,
11 Pipers Piping,
10 Lords a Leaping,
9 Ladies Dancing,
8 Maids a Milking,
7 Swans a Swimming,
6 Geese a Laying,
5 Golden Rings,
4 Calling Birds,
3 French Hens,
2 Turtle Doves,
and 1 Partridge in a Pear Tree'''

xmasRegex = re.compile(r'\d+\s\w+') #one or more digits, onespace, one or more word
print(xmasRegex.findall(lyrics))