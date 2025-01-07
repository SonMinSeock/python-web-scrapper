class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed
    
class GuardDog(Dog):
    def rrrr(self):
        print("stay away!")

class Puppy(Dog):
    def __str__(self):
        return f"Puppy named {self.name}, breed: {self.breed}"
    def woof_woof(self):
        print("Woof Woof!")

puppy1 = Puppy(name="뚜비", breed="비숑")
puppy2 = Puppy(name="톰", breed="요크셔테리어")
puppy3 = Puppy(name="콩", breed="요크셔테리어")
puppy4 = Puppy(name="담비", breed="말티즈")


print(puppy1.name, puppy1.breed, puppy1.age)
print(puppy2.name, puppy2.breed, puppy2.age)
print(puppy3.name, puppy3.breed, puppy3.age)
print(puppy4.name, puppy4.breed, puppy4.age)

print(puppy1, puppy2, puppy3, puppy4)

puppy1.introduce()