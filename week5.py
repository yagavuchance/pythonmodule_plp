# Parent Class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on.")

    def power_off(self):
        print(f"{self.brand} {self.model} is shutting down.")


# Child Class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Call the parent class constructor
        self.__os = os  # Encapsulated attribute
        self.__storage = storage  # Encapsulated attribute

    # Getter and Setter for OS (Encapsulation)
    def get_os(self):
        return self.__os

    def set_os(self, os):
        self.__os = os

    # Method specific to Smartphone
    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model}...")

    def show_specs(self):
        print(
            f"Smartphone Specs:\nBrand: {self.brand}\nModel: {self.model}\nOS: {self.__os}\nStorage: {self.__storage}GB"
        )


# Create objects
iphone = Smartphone("Apple", "iPhone 14", "iOS 17", 256)
samsung = Smartphone("Samsung", "Galaxy S23", "Android 13", 512)

# Call methods
iphone.power_on()
iphone.show_specs()
iphone.install_app("Instagram")
iphone.set_os("iOS 18")  # Update OS
print(f"Updated OS: {iphone.get_os()}")
iphone.power_off()
