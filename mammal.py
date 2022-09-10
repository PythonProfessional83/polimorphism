# mammal.py
'''
Super class for polumorhism.
'''
class Mammal:
    def __init__(self, species):
        self.species = species
    
    def show_species(self):
        print(f"This is {self.species}")
    
    # this method will be overrided by the the same method name from the subclases
    def make_sound(self):  
        print('Wrrr')

class Dog(Mammal):
    def __init__(self):
        super().__init__('dog') # show_species() from super class will be used
    
    # overriding the super class method
    def make_sound(self):
        print('Hau, Hau')

class Cat(Mammal):
    def __init__(self):
        super().__init__('cat')
    
    def make_sound(self):
        print('Miau Miau')

'''
out:
This is animal
Wrrr

This is dog
Hau, Hau

This is cat
Miau Miau
'''
        
        