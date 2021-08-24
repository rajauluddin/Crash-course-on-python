# Classes and Instances
# # Classes define the behavior of all instances of a specific class.

# # Each variable of a specific class is an instance or object.

# # Objects can have attributes, which store information about the object.

# # You can make objects do work by calling their methods.

# # The first parameter of the methods (self) represents the current instance.

# # Methods are just like functions, but they can only be used through a class.
class Apple:
    def __init__(self, color, floavour):
        self.color = color
        self.flavour = floavour
    def __str__(self):
        return "This apple is {} and {} in flavour.".format(self.color, self.flavour)
john = Apple("red", "sweet")
print(john)
print(help())