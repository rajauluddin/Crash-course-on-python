animals = ["lion", "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
    chars+=len(animal)

print("total characters: {}, average length: {}".format(chars,chars/len(animals)))
print("---------------")

winners = ["ashley", "dylan", "resse"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1,person))