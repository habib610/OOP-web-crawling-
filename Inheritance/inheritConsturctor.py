class Vehicle:

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.name, self.manufacturer, self.color)

    def turn(self, direction):
        print("Turning", direction)

    def brake(self):
        print(self.name, "is stopped")


class Car(Vehicle):
    """Car Class"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4
        print("A new car has been created. Name:", self.name)
        print("It has", self.wheels, "wheels")
        print("The car was built in ", self.year)

    def change_gear(self, gear_name):
        """Method Changing for Gear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "RED", "2017")

