class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

my_animal = Animal()
my_dog = Dog()
my_cat = Cat()

my_animal.make_sound()  
my_dog.make_sound()     
my_cat.make_sound()    


class car:
    def make_sound(self):
        print("Some sound")

class tata(car):
    def make_sound(self):
        print("Bark")

class toyato(car):
    def make_sound(self):
        print("Meow")

my_cars = car()
my_tata = tata()
my_toyato = toyato()

my_cars.make_sound()  
my_tata.make_sound()     
my_toyato.make_sound()     
