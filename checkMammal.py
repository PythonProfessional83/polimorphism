# checkMammal.py
'''
Showing how the polimorphism works.
'''
import mammal

def main():
    animal = mammal.Mammal('animal')
    animal.show_species()
    animal.make_sound()
    
    dog = mammal.Dog()
    print()
    dog.show_species()
    # overriding
    dog.make_sound()
    print()
    
    cat = mammal.Cat()
    cat.show_species()
    cat.make_sound()

main()