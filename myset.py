myset = {"apple", "banana", "vanilla", "nutmeg"}
name = "Jay"

for character in name:
    print(character)

for z in myset:
    print(z,"", len(z), character)

ev_data = [['vehicle', 'range', 'price'],
           ['Tesla Model 3 LR', '310', '49900'],
           ['Hyundai Ioniq EV', '124', '30315'],
           ['Chevy Bolt', '238', '36620']]

for i in ev_data[1:]:
    ev_range = i[1]
    ev_range = int(ev_range)
    i[1] = ev_range

print(ev_data)
