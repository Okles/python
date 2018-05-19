import pprint #pretty print module

message = 'Progi podatkowe w 2018 roku będą takie same jak w roku 2017, choć należy mieć na uwadze, że od przyszłego roku zmianie ulegną przepisy ustawy o podatku od osób fizycznych w zakresie kwoty wolnej o podatku'
count = {}

for roman in message.upper():
    count.setdefault(roman,0)
    count[roman] = count[roman] +1


text = pprint.pformat(count)
print(text)