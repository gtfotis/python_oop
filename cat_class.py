# When you instantiate a class, write the class name capitalized
class Cat:
    # Attribute, a thing that it is
    species = 'mammal'
    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # Always have to have self in the constructor, it means it's pointing back at itSELF
    def describe(self):
        return "%s is %d years old." % (self.name, self.age)
tarmac = Cat("Tarmac", 3)
bee = Cat("Bee", 4)
# tarmac and bee are instances of the Cat class
print(tarmac.describe())
print(bee.describe())
