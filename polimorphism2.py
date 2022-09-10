# polimorphism2.py
'''
Showing using of the function which will call any objects, which has the same methods.
Checking isinstance function.
'''
import mammal

def main():
    animal = mammal.Mammal('animal')
    dog = mammal.Dog()
    cat = mammal.Cat()
    for anim in [animal, dog, cat, 'this is a string']: 
        
        if isinstance(anim, mammal.Mammal):  #(object, super class)
            showAnimal(anim)
        else:
            print(anim,": This is not an animal.")
        print()
    
    
# all objects has the same metchods, so one function cal call the same 
# names of the methods in all objects.
def showAnimal(object):
    object.show_species()
    object.make_sound()
    
    
main()

'''
out:
This is animal
Wrrr

This is dog
Hau, Hau

This is cat
Miau Miau

this is a string : This is not an animal.
'''