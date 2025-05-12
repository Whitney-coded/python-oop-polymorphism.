from classes import Car, Plane, Smartphone

def main():
    # Create instances of Car and Plane
    car = Car("Toyota", "Corolla")
    plane = Plane("Boeing", "747", wingspan=60)

    # Polymorphism: same method name, different behavior
    car.move()   # Output: Toyota Corolla is Driving 🚗
    plane.move() # Output: Boeing 747 is Flying ✈️

    # Smartphone example demonstrating encapsulation
    phone = Smartphone("Apple", "iPhone 13", "iOS")
    phone.info()  # Output: Smartphone: Apple iPhone 13, OS: iOS

    # Change OS using setter method
    phone.set_os("iOS 15")
    print("Updated OS:", phone.get_os())

if __name__ == "__main__":
    main()
