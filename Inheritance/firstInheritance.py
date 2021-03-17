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

    def change_gear(self, gear_name):
        print(self.name, "is changing gear to", gear_name)
    """Method Changing for Gear"""


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "RED")
    c.drive()
    c.brake()
    c.change_gear("P")