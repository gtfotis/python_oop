class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friendslist = []
        self.greeting_count = 0
        self.unique_greetings = []
    def __str__(self):
        return "%s" % (self.name)
    def greet(self, other_person):
        self.greeting_count += 1
        self.unique_greetings.append(other_person)
        return "Hello %s, I am %s!" % (other_person.name, self.name)
    def print_contact_info(self):
        return "%s's email: %s \n%s's phone number: %s" % (self.name,self.email,self.name,self.phone)
    def add_friend(self,other_person):
        self.friendslist.append(other_person)
        return "%s added %s as a friend." % (self.name,other_person)
    def num_friends(self):
        return len(self.friendslist)
    def unique_greetings_count(self):
        unique = set(self.unique_greetings)
        unique_greetings = unique
        return len(unique_greetings)

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
otis = Person("otis", "otis@gmail.com", "678-345-1234")

print(sonny.greeting_count)
print(jordan.greeting_count)

print(sonny.greet(jordan))
print(jordan.greet(sonny))

print(sonny.greeting_count)
print(jordan.greeting_count)

print(sonny.print_contact_info())
print(jordan.print_contact_info())
print(otis.print_contact_info())

print(sonny.add_friend(jordan))
print(jordan.add_friend(sonny))

print(sonny.num_friends())

print(sonny.greet(jordan))
print(jordan.greet(sonny))

print(sonny.greeting_count)
print(jordan.greeting_count)

print(sonny.unique_greetings_count())

print(sonny.greet(otis))

print(sonny.unique_greetings_count())

print(otis.unique_greetings_count())
print(otis.greet(jordan))
print(otis.greet(jordan))
print(otis.greet(jordan))
print(otis.unique_greetings_count())
print(otis.greet(sonny))
print(otis.unique_greetings_count())
print(otis.greeting_count)
