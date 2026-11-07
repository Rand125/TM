from Animal import Animal


class Cat(Animal):
    def init(self, name, age):
        super().init(name, age, breed="cat")

    def str(self):
        return f'{self.name} is {self.age} year old'

    def speak(self, sound):
        print(f'{self.name} the cat says: {sound}')


if name == "main":
    cat1 = Cat("Djoric", 17)
    cat2 = Cat("Marusya", 4)
    print(cat1.str(), '\n', cat2.str())
    cat1.speak('mya')
    cat2.speak('mi')
