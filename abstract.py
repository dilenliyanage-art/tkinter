from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("i can walk, run, and sit")
class snake(Animal):
    def move(self):
        print("I can slither and hiss")
class dog(Animal):
    def move(self):
        print("i can bark and run")
class lion(Animal):
    def move(self):
        print("i can roar and run")
R = human()
R.move()
K = snake()
K.move()
R = dog()
R.move()
L = lion()
L.move()