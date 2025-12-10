class House:
    # --- 1. Class Attribute ---
    # Shared by all instances of the class (all houses are considered real property)
    property_type = "Real Estate"

    # --- 2. Constructor (The Blueprint Setter) ---
    # The special method __init__ runs when a new object (instance) is created.
    # It sets up the initial state (attributes) of the object.
    def __init__(self, address, square_footage, price):
        # --- 3. Instance Attributes (Data) ---
        # Unique to each object (each house has its own address, size, and price)
        self.address = address
        self.square_footage = square_footage
        self.price = price
        self.is_sold = False # Default state/attribute

    # --- 4. Instance Methods (Behavior) ---
    # Functions that perform actions or operate on the object's data.

    def display_details(self):
        """Prints the key attributes of the house."""
        status = "Sold" if self.is_sold else "Available"
        return (f"--- Property Details ---\n"
                f"Address: {self.address}\n"
                f"Size: {self.square_footage} sq ft\n"
                f"Price: ${self.price:,.2f}\n"
                f"Status: {status}\n"
                f"Type: {self.property_type}") # Accessing the class attribute

    def sell(self):
        """Changes the state of the house from available to sold."""
        if not self.is_sold:
            self.is_sold = True
            print(f"**SUCCESS:** House at {self.address} has been marked as sold!")
        else:
            print(f"**NOTICE:** House at {self.address} is already sold.")

# =========================================================
# --- Creating Objects (Instantiation) ---
# =========================================================

# Creating the first object/instance from the House class
house1 = House(address="123 Oak St, Anytown", square_footage=2500, price=500000)

# Creating the second object/instance
house2 = House(address="456 Pine Ave, Otherville", square_footage=1800, price=350000)

print("---------------------------------")
print("1. Displaying Initial State (House 1)")
print(house1.display_details())

print("\n2. Calling a Method to Change State (House 1)")
house1.sell() # Calling the sell() method

print("\n3. Displaying Final State (House 1)")
print(house1.display_details())

print("\n4. State of the Second Object (House 2)")
# Note that house2's state is independent of house1's state
print(house2.display_details())

print("\n5. Accessing Class Attribute")
print(f"All houses share this type: {House.property_type}")
print("---------------------------------")