'''method over riding'''
class animal: 
      def speak():
        return "animal is speaking"
class dog(animal):
    def speak():
        return "bow..."
class puppy(dog):
    def speak():
        return "i am puppy"
obj2=animal
print(obj2.speak())

