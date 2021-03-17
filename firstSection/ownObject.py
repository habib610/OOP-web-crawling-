class Car:
    name = ""
    color = ""

    def start(self):
        print("Starting the engine")


car1 = Car
car1.name = "BMW"
car1.color = "Black"
print(car1.name)
car1.start()
