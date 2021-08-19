animals = ["lion", "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
    chars+=len(animal)

print("total characters: {}, average length: {}".format(chars,chars/len(animals)))
print("---------------")

#The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.
winners = ["ashley", "dylan", "resse"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1,person))