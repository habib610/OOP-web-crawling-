class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("car name", self.name)
        print("car color", self.color)

myCar = Car("Corolla", "white")
Car.start(myCar)