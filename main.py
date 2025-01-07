class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed
    def sleep(self):
        print(f"{self.name} zzzzzz...")
    
class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        self.aggresive = True

    def rrrr(self):
        print("stay away!")
    
    
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
        self.spoiled = True
    def __str__(self):
        return f"Puppy named {self.name}, breed: {self.breed}"
    def woof_woof(self):
        print("Woof Woof!")

puppy1 = Puppy(name="뚜비", breed="비숑")
puppy2 = Puppy(name="톰", breed="요크셔테리어")
puppy3 = Puppy(name="콩", breed="요크셔테리어")
puppy4 = Puppy(name="담비", breed="말티즈")

guard_dog1 = GuardDog(name="그리즈", breed="달마시안")

print(puppy1.name, puppy1.breed, puppy1.age)
print(puppy2.name, puppy2.breed, puppy2.age)
print(puppy3.name, puppy3.breed, puppy3.age)
print(puppy4.name, puppy4.breed, puppy4.age)

print(puppy1, puppy2, puppy3, puppy4)

puppy1.woof_woof()
guard_dog1.rrrr()
puppy1.sleep()
guard_dog1.sleep()