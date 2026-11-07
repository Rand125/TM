from Animal import Animal


class Dog(Animal):
    def init(self, name, age, breed):
        super().init(name, age, breed)

    def str(self):
        return f'This {self.breed} - {self.name} is {self.age} year old'

    def speak(self, sound):
        print(f'{self.name} the dog says: {sound}')


if name == "main":
    dog1 = Dog("Rex", 5, "husky")
    dog2 = Dog("Bobik", 2, "corgi")
    print(dog1, '\n', dog2)
    dog1.speak('woof')
    dog2.speak('gav')
