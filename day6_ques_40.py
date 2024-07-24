'''inheritance'''
class animal:
    def speak():
        return "animal is speaking"
#single inheritance
class dog(animal):
    def bark():
        return "bow..." 
obj=animal
obj1=dog
#print(obj1.speak())
#print(obj1.bark())
'''mutilevel'''
class puppy(dog):
    def puppy_speak():
        return "i am puppy"
obj2=puppy
print(obj2.speak())
print(obj2.bark())
print(obj2.puppy_speak())
