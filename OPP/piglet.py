class Animal:
    sound= ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound= self.sound))

class Piglet(Animal):
    sound = "Oink!"
hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Mooow"
milky = Cow("Milky white")
milky.speak()

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()