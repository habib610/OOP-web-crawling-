class Car:
    name= "premio"
    color = "blue"

# print("name of the car", Car.name)
# print("Color of the car", Car.color)
class OurCar:
    name = ""
    color = ""

    def start():
        print("Starting th engine")

OurCar.name = "Lamborghini"
OurCar.color = "Yellow"

print(OurCar.name)
print(OurCar.color)
OurCar.start()