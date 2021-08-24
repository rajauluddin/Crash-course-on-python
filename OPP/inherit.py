class Fruit:
    def __init__(self, color, flavour):
        self.color = color
        self.flavour = flavour

class Apple(Fruit):
    pass

class Grapes(Fruit):
    pass

ram = Apple("red", "bitter")
sam = Grapes("purple", "sweet")

print(ram.color)
print(sam.flavour)
