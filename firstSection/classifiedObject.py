class Car:
    name = "direct data attribute from Car class"  # this one is  called data attribute
    # color = "" # this are called data attribute

    def __init__(self, name, color):  #this is called object
        self.name = name #this one is an instance attribute
        self.color = color

    def start(self):
        print("Starting the engine", "::=>", self.name)
        print("Color of the car", "::=>", self.color)

my_car = Car("Corolla", "white")
my_car2 = Car("Tesla", "red")
my_car.manufacturer = "Toyota" # this attribute was not present in Car Class but we adjusted it as our own
print(my_car.name)
print(my_car.color)
print("Not present data attribute in Car class but we added as our own:: =>",my_car.manufacturer)

my_car.start()
print(Car.name)
my_car2.start()