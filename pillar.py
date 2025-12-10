# --- 1. Encapsulation ---
# Bundling data (attributes) and methods (functions) that operate on the data
# into a single unit (the class). It also involves restricting direct access
# to some components, typically using naming conventions like:
# - Single underscore (e.g., _internal_var): Conventionally protected (meant for internal use or subclasses).
# - Double underscore (e.g., __private_var): Name mangling makes it harder to access (effectively private).
class Car:
    def __init__(self, brand, model, year):
        # Public attribute (can be accessed directly)
        self.brand = brand
        # Protected attribute (conventionally meant for internal use or subclasses)
        self._model = model
        # Private attribute (Python performs name mangling to make it harder to access)
        self.__year = year
        self._engine_status = "Off"  # Encapsulated state

    # Public method (interface to interact with the object)
    def start_engine(self):
        if self._engine_status == "Off":
            self._engine_status = "On"
            print(f"The {self.brand} {self._model}'s engine is now **ON**.")
        else:
            print("Engine is already running.")

    # Encapsulated method to access the "private" year
    def get_manufacturing_year(self):
        # A good practice is to provide controlled access to private data
        return self.__year

    # Method demonstrating data hiding and control
    def get_info(self):
        return f"Car: {self.brand} {self._model} | Year: {self.get_manufacturing_year()} | Status: {self._engine_status}"

# Usage of Encapsulation
my_car = Car("Toyota", "Camry", 2020)
print(f"\n--- Encapsulation Demo ---")
print(my_car.get_info())

# Direct access to public attribute
print(f"Accessing public attribute: {my_car.brand}")
# Direct access to "protected" attribute (Python doesn't enforce, but it's a warning)
print(f"Accessing protected attribute: {my_car._model}")
# Direct access to "private" attribute (will usually fail or require name mangling: _ClassName__attribute)
# print(f"Accessing private attribute: {my_car.__year}") # This will raise an AttributeError!
print(f"Accessing private attribute via public method: {my_car.get_manufacturing_year()}")
my_car.start_engine()
my_car.start_engine()
print("-" * 30)


# --- 2. Inheritance ---
# Creating a new class (subclass/child) from an existing class (superclass/parent),
# inheriting its attributes and methods.
class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, brand, model, year, battery_range):
        # Call the parent class's constructor
        super().__init__(brand, model, year)
        self.battery_range = battery_range # New attribute for ElectricCar

    # Method Overriding: Changing the behavior of a method inherited from the parent
    def start_engine(self):
        if self._engine_status == "Off":
            self._engine_status = "On"
            # Accessing the protected attribute from the parent is common in subclasses
            print(f"The {self.brand} {self._model}'s electric motor hums to life. **ON**.")
        else:
            print("Motor is already running.")
            
    # New method specific to the subclass
    def charge(self):
        print(f"The {self.brand} is now charging.")

# Usage of Inheritance
my_ev = ElectricCar("Tesla", "Model 3", 2023, 300)
print(f"\n--- Inheritance Demo ---")
print(my_ev.get_info()) # Inherited method from Car
my_ev.start_engine()    # Overridden method in ElectricCar
my_ev.charge()          # New method in ElectricCar
print("-" * 30)


# --- 3. Abstraction ---
# Hiding the complex implementation details and showing only the essential features
# of the object. In Python, this is typically achieved using Abstract Base Classes (ABCs)
# from the 'abc' module. A class becomes abstract if it has an abstract method.
# It cannot be instantiated.
from abc import ABC, abstractmethod

class Vehicle(ABC): # Vehicle is an Abstract Base Class (Template)
    def __init__(self, color):
        self.color = color

    # Abstract Method: Subclasses MUST implement this method.
    @abstractmethod
    def move(self):
        pass

    # Concrete Method: A regular method that can be used directly or overridden.
    def show_color(self):
        print(f"This vehicle is {self.color}.")

class Motorcycle(Vehicle): # Motorcycle is a concrete implementation of Vehicle
    def __init__(self, color, max_speed):
        super().__init__(color)
        self.max_speed = max_speed

    # Must implement the abstract 'move' method!
    def move(self):
        print(f"The {self.color} Motorcycle is accelerating to {self.max_speed} mph. (Implementation details hidden)")

# Usage of Abstraction
# vehicle = Vehicle("Black") # This would raise a TypeError because Vehicle is abstract!
my_bike = Motorcycle("Red", 150)
print(f"\n--- Abstraction Demo ---")
my_bike.show_color() # Uses the concrete method
my_bike.move()       # Calls the specific implementation of the abstract method
print("-" * 30)


# --- 4. Polymorphism ---
# The ability of different objects to respond to the same message (method call)
# in their own way. "Poly" means many, "morph" means form.

# 4a. Method Overriding (already seen with ElectricCar.start_engine)
# The parent and child class have the same method name, but different implementations.

# 4b. Method Overloading (Not strictly supported in Python like in C++/Java,
# but can be simulated using default arguments or *args/kwargs).

# 4c. Duck Typing (The most common form of polymorphism in Python)
# "If it walks like a duck and quacks like a duck, then it must be a duck."
# It focuses on *what an object can do*, not *what it is* (its class).
class Driver:
    def operate_vehicle(self, vehicle):
        # This function doesn't care if 'vehicle' is a Car, ElectricCar, or Motorcycle,
        # as long as it has a 'start_engine' and a 'move' method.
        print("\nDriver operating a vehicle:")
        vehicle.start_engine()
        vehicle.move() # Calling 'move' on Car/ElectricCar will fail since they don't have it!
                       # Let's adjust Car/ElectricCar to have a simple 'move' method
                       # for this demonstration.

# Let's quickly add a 'move' method to Car (and thus ElectricCar via inheritance)
# to make the Duck Typing example work cleanly.

class Car(Car): # Redefining Car to add a move method for the demo
    def move(self):
        print(f"The {self.brand} {self._model} is driving on four wheels.")

class ElectricCar(ElectricCar): # Redefining ElectricCar to get the new Car.move
    def move(self):
        print(f"The {self.brand} {self._model} silently moves forward.")

# Create new instances with the added 'move' methods
my_car_poly = Car("Honda", "Civic", 2018)
my_ev_poly = ElectricCar("Lucid", "Air", 2024, 400)
my_bike_poly = Motorcycle("Blue", 120) # Motorcycle already has a move()

driver = Driver()
print(f"\n--- Polymorphism (Duck Typing) Demo ---")

# The SAME method call (operate_vehicle) works on DIFFERENT types of objects
# because they all implement the expected methods (start_engine and move).

driver.operate_vehicle(my_car_poly)
driver.operate_vehicle(my_ev_poly)
driver.operate_vehicle(my_bike_poly)
print("-" * 30)