#Let's define a class for our pets
class Sorceror:
    def __init__(self, name, health=50, morale=50, damagetaken=5, motivationloss=5):
        self.name = name
        self.health = health
        self.morale = morale
        self.damagetaken = damagetaken
        self.motivationloss = motivationloss
    def heal_sorc(self):
        self.health += 30
    def fight_curse(self):
        self.morale += 30
    def be_alive(self, damagetaken, motivationloss):
        self.health -= self.damagetaken
        self.morale -= self.motivationloss
#We're creating a class that inherits from another class, ExtraHeals is a SUBCLASS
#Subclasses inherit from SUPERCLASSES, also known as parent classes
class Faculty(Sorceror):
    pass



yuji = Sorceror("Yuji Itadori", 50, 20, 20, 1)
megumi = Sorceror("Megumi Fushiguro", 50, 20, 20, 1)
nobara = Sorceror("Nobara Kugisaki", 50, 20, 20, 1)
gojo = Faculty("Satoru Gojo", 100, 100, 5, 1)




# Define a dictionary that holds our pet's attributes.
sorceror = {
    "name": "Yuji Itadori",
    "health": 50,
    "morale": 20,
    "damagetaken": 7,
    "motivationloss": 4,
}

sorceror2 = {
    "name": "Megumi Fushiguro",
    "health": 50,
    "morale": 20,
    "damagetaken": 3,
    "motivationloss": 2
}
# Define a list that holds all of our pet's.
pets = [sorceror, sorceror2]

# Define functions that increase a pet's attribute levels.
def feed_pet(pet):
    pet["health"] += 10

def play_with_pet(pet):
    pet["morale"] += 10

# Decrease a pet's attribute levels.    
def get_hungry_and_mopey(pet):
    pet["health"] -= pet["damagetaken"]
    pet["morale"] -= pet["motivationloss"]

# Prompt the user to interact with the pet
while True:

    for pet in pets:
        print("""
%s's stats:
Health: %d
Morale: %d
""" % (pet["name"], pet["health"], pet["morale"]))
    
    choice = int(input("""
1. Heal sorceror
2. Fight curses
3. Do nothing
"""))
    if choice == 1:
        which_pet = input("Which Jujutsu Sorceror would you like to heal? ")
        if which_pet == "Itadori" or "Yuji" or "Itadori Yuji" or "Yuji Itadori":
            which_pet = int(0)
            feed_pet(pets[which_pet])
        elif which_pet == "Megumi" or "Fushiguro" or "Megumi Fushiguro" or "Fushiguro Megumi":
            which_pet = int(1)
            feed_pet(pets[which_pet])
        else:
            pass
    elif choice == 2:
        which_pet = input("Which Jujutsu Sorceror wants to exorcise curses? ")
        if which_pet == "Itadori" or "Yuji" or "Itadori Yuji" or "Yuji Itadori":
            which_pet = int(0)
            play_with_pet(pets[which_pet])
        elif which_pet == "Megumi" or "Fushiguro" or "Megumi Fushiguro" or "Fushiguro Megumi":
            which_pet = int(1)
            play_with_pet(pets[which_pet])
        else:
            pass
    else:
        pass

    # Each time the loop runs, the pet
    # will need some attention!
    for pet in pets:
        get_hungry_and_mopey(pet)    