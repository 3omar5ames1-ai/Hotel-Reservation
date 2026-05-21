from abc import ABC, abstractmethod

# Requirement 1: The Blueprint (Abstraction)
class HotelOffering(ABC):
    def __init__(self, item_id, name, base_price):
        self.item_id = item_id
        self.name = name
        # Requirement 3: Data Protection (Encapsulation)
        self.__base_price = base_price  # Private attribute

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            print("❌ Error: Price cannot be negative.")
        else:
            self.__base_price = value

    @abstractmethod
    def calculate_item_cost(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

# Requirement 2: Specialization (Type A - Hotel Rooms)
class HotelRoom(HotelOffering):
    def __init__(self, item_id, name, base_price, bed_size, smoking_allowed):
        super().__init__(item_id, name, base_price)
        self.bed_size = bed_size
        self.smoking_allowed = smoking_allowed

    def calculate_item_cost(self):
        # Requirement 4: Smart Behavior (15% hospitality tax)
        return self.base_price * 1.15

    def display_details(self):
        status = "Smoking" if self.smoking_allowed else "Non-Smoking"
        return f"[Room] {self.name} ({self.bed_size}, {status}) - Base: ${self.base_price:.2f}"

# Requirement 2: Specialization (Type B - Spa/Dining Services)
class HotelService(HotelOffering):
    def __init__(self, item_id, name, base_price, duration_mins):
        super().__init__(item_id, name, base_price)
        self.duration_mins = duration_mins

    def calculate_item_cost(self):
        # Requirement 4: Smart Behavior (20% staff gratuity)
        return self.base_price * 1.20

    def display_details(self):
        return f"[Service] {self.name} ({self.duration_mins} mins) - Base: ${self.base_price:.2f}"

# Requirement 4: Dedicated CustomerReservation Structure
class CustomerReservation:
    def __init__(self):
        self.__bookings = []

    def add_item(self, item):
        self.__bookings.append(item)
        print(f"✅ Added {item.name} to your reservation.")

    def show_current_items(self):
        if not self.__bookings:
            print("\nYour reservation is empty.")
            return
        print("\n--- Current Reservation Items ---")
        for item in self.__bookings:
            print(f"- {item.display_details()}")

    def print_final_folio(self):
        if not self.__bookings:
            print("\n❌ No items to bill.")
            return
        
        print("\n" + "="*40)
        print("          FINAL HOTEL FOLIO          ")
        print("="*40)
        total_sum = 0
        for item in self.__bookings:
            cost = item.calculate_item_cost()
            total_sum += cost
            print(f"{item.name:<25} ${cost:>10.2f}")
        
        print("-" * 40)
        print(f"{'TOTAL AMOUNT DUE:':<25} ${total_sum:>10.2f}")
        print("="*40)
        print("Thank you for staying with us!\n")

# Requirement 5: Terminal Interaction
def main():
    # Setup some data
    offerings = {
        "1": HotelRoom("1", "Deluxe Suite", 200, "King", False),
        "2": HotelRoom("2", "Standard Room", 120, "Queen", True),
        "3": HotelService("3", "Deep Tissue Massage", 80, 60),
        "4": HotelService("4", "Gourmet Dinner", 50, 90)
    }
    
    reservation = CustomerReservation()

    while True:
        print("\n--- Smart Hotel Management System ---")
        print("1. View Hotel Offerings")
        print("2. Add to Reservation")
        print("3. View Current Reservation")
        print("4. Print Final Folio (Checkout)")
        print("5. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\n--- Available Offerings ---")
            for item in offerings.values():
                print(f"ID: {item.item_id} | {item.display_details()}")
        
        elif choice == "2":
            item_id = input("Enter the ID of the item to add: ").strip()
            if item_id in offerings:
                reservation.add_item(offerings[item_id])
            else:
                print("❌ Invalid ID. Please try again.")
        
        elif choice == "3":
            reservation.show_current_items()
            
        elif choice == "4":
            reservation.print_final_folio()
            break # Exit after printing bill
            
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        
        else:
            # Requirement 5: Error Handling
            print("❌ Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()