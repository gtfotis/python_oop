class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print("%s %s %s" % (self.year,self.make,self.model))
myVolt = Vehicle("Chevrolet", "Volt", "2017")

print(myVolt.make, myVolt.model, myVolt.year)
myVolt.print_info()