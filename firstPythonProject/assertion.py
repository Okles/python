glowna_kolejowa = {'ns' : 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'None of the lights is red!' + str(intersection)


print(glowna_kolejowa)
switchLights(glowna_kolejowa)
print(glowna_kolejowa)