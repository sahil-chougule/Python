class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

bird = Bird()
dog = Dog()
cat = Cat()

make_sound(bird)
make_sound(dog)
make_sound(cat)
