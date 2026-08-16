# VEHICLE PARKING MANAGEMENT SYSTEM:
class Parking:

    def __init__(self):
        self.slots = [None] * 100

    def park(self):
        vehicle = input("Enter vehicle number: ")
        type = input("Enter type (Car/Bike): ").lower()

        for i in range(100):
            if self.slots[i] is None:
                self.slots[i] = [vehicle, type]
                print("Vehicle parked in Slot", i + 1)
                return

        print("Parking is full")

    def remove(self):
        vehicle = input("Enter vehicle number: ")

        for i in range(100):
            if self.slots[i] is not None:
                if self.slots[i][0] == vehicle:
                    self.slots[i] = None
                    print("Vehicle removed from Slot", i + 1)
                    return

        print("Vehicle not found")

    def display(self):
        for i in range(100):
            if self.slots[i] is None:
                print("Slot", i + 1, ": Empty")
            else:
                print("Slot", i + 1, ":", self.slots[i][0],
                      "-", self.slots[i][1])


parking = Parking()

while True:

    print("\n--- VEHICLE PARKING SYSTEM ---")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Display Slots")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        parking.park()

    elif choice == "2":
        parking.remove()

    elif choice == "3":
        parking.display()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")