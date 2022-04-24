'''class Vehicle:

    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show(self):
        print("The vehicle's max speed is", self.max_speed, "km/h and mileage is", self.mileage, "km/L")

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

class Car(Vehicle):
    pass

v = Vehicle("Tesla Chor", 60, 100)
v.show()
b = Bus("School Volvo", 180, 12)
print("Color:", b.color, "Vehicle Name:", b.name, "Speed:", b.max_speed, "Mileage:", b.mileage)
print(b.seating_capacity())
c = Car("Aud Q5", 240, 18)
print(c.seating_capacity(25))
print("Color:", c.color, "Vehicle Name:", c.name, "Speed:", c.max_speed, "Mileage:", c.mileage)'''


'''class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())'''


'''class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))
# use Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle))'''


'''class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def drive(self):
        print("I am driving at", self.max_speed, "with mileage of", self.mileage)

class Bus(Vehicle):

    def fare(self):
        f = super().fare()
        return f + (10/100*f)

    def drive(self):
        print("I am driving a bus:", self.name, "at", self.max_speed, "with mileage of", self.mileage)

class Car(Vehicle):

    def drive(self):
        print("I am driving a car:", self.name, "at", self.max_speed, "with mileage of", self.mileage)
    

class Truck(Vehicle):
    def drive(self):
        print("I am driving a truck:", self.name, "at", self.max_speed, "with mileage of", self.mileage)
        
vehicles = []
vehicles.append(Bus("Volvo V8", 15, 60))
vehicles.append(Bus("Volvo V9", 18, 70))
vehicles.append(Car("Skoda Octavia", 20, 80))
vehicles.append(Car("Volkswagon Polo", 22, 75))
vehicles.append(Car("Suzuki Kizashi", 25, 90))
vehicles.append(Truck("Tata Xcident", 10, 50)) 

for i in range(len(vehicles)): 
    v = vehicles[i]
    v.drive()'''
