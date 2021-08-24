class Apple:
    def __init__(self, color, floavour):
        self.color = color
        self.flavour = floavour
    def __str__(self):
        return "This apple is {} and {} in flavour.".format(self.color, self.flavour)
john = Apple("red", "sweet")
print(john)
print(help())