import math
import matplotlib.pyplot as plt
import numpy as np


# class Dog:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def description(self):
#         return f'{self.name} is {self.age} years old, and is a {self.breed}.'
    
#     def speak(self, sound):
#         return f'{self.name} says {sound}'


# my_dog = Dog('Fido', 38, 'German Shepard')
# their_dog = Dog('George', 79, 'Bulldog')

# my_dog.age += 1

# # print(my_dog.age, their_dog.breed)

# print(my_dog.description(), their_dog.description())
# print(my_dog.speak('Arf'))




class Quad:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def calculate(self, val):
        return self.a*(val**2) + (self.b*val) + self.c
    
    def discriminant(self):
        return math.sqrt(((self.b**2) - (4*self.a*self.c)))
    
    def xints(self):
        if self.discriminant() < 0:
            return None
        else:
            self.x1 = ((self.b*-1) + math.sqrt(((self.b**2) - (4*self.a*self.c))))/ 2*self.a
            self.x2 = ((self.b*-1) - math.sqrt(((self.b**2) - (4*self.a*self.c))))/ 2*self.a
            return f'x1 = {self.x1}, x2 = {self.x2}'
    
    def vertex(self):
        vertx = (-1*self.b)/(2*self.a)
        verty = self.a*(vertx**2) + (self.b*vertx) + self.c
        return vertx, verty
    
    def plotquad(self):
        x = np.linspace(self.vertex()[0]-20, self.vertex()[0]+20, 100)
        y = self.a*(x**2) + (self.b*x) + self.c

        plt.plot(x, y)
        plt.plot((self.vertex()[0]-0.001, self.vertex()[0]-0.001), (self.vertex()[1]-0.001, self.vertex()[1]+0.001), 'ro')
        plt.grid(True)
        plt.show()
    

quad = Quad(1, 0, -4)

print(quad.plotquad())