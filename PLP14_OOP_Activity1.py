
class Passenger:
    #Base class representing a standard airline passenger.#

    def __init__(self, name: str, location: str, destination: str, date: str):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date

    def get_weight_allowance(self) -> int:
        """Returns the default luggage weight allowance in kg."""
        return 20

    def get_passenger_info(self) -> str:
        """Returns formatted base ticket information."""
        return (
            f"Passenger Name : {self.name}\n"
            f"Route          : {self.location} -> {self.destination}\n"
            f"Travel Date    : {self.date}\n"
            f"Baggage Limit  : {self.get_weight_allowance()} kg"
        )
        
Python
class EconomyPassenger(Passenger):
    """Child class for Economy Class passengers."""

    def __init__(
        self,
        name: str,
        location: str,
        destination: str,
        date: str,
        seat_preference: str,
    ):
        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference

    def get_passenger_info(self) -> str:
        base_info = super().get_passenger_info()
        return (
            f"=== ECONOMY CLASS TICKET ===\n"
            f"{base_info}\n"
            f"Seat Preference: {self.seat_preference}"
        )

class BusinessPassenger(Passenger):
   """Child class for Business Class passengers."""

   def __init__(
       self,
       name: str,
       location: str,
       destination: str,
       date: str,
       lounge_pass_code: str,
   ):
       super().__init__(name, location, destination, date)
       self.lounge_pass_code = lounge_pass_code

   def get_weight_allowance(self) -> int:
       """Overrides default luggage allowance to 100 kg."""
       return 100

   def get_passenger_info(self) -> str:
       base_info = super().get_passenger_info()
       return (
           f"=== BUSINESS CLASS TICKET ===\n"
           f"{base_info}\n"
           f"Lounge Pass    : {self.lounge_pass_code}"
       )


Python
class FirstClassPassenger(Passenger):
    """Child class for First Class passengers."""

    def __init__(
        self,
        name: str,
        location: str,
        destination: str,
        date: str,
        suite_number: str,
        chauffeur_service: bool,
    ):
        super().__init__(name, location, destination, date)
        self.suite_number = suite_number
        self.chauffeur_service = chauffeur_service

    def get_passenger_info(self) -> str:
        base_info = super().get_passenger_info()
        chauffeur_status = "Included" if self.chauffeur_service else "Not Requested"
        return (
            f"=== FIRST CLASS TICKET ===\n"
            f"{base_info}\n"
            f"Suite Number   : {self.suite_number}\n"
            f"Chauffeur      : {chauffeur_status}"
        )


# --- Helper Functions for Input Validation ---


def get_non_empty_input(prompt: str) -> str:
    """Prompts the user until a non-empty string is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")


def get_yes_no_input(prompt: str) -> bool:
    """Prompts the user for a yes/no response and returns a boolean."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Error: Please enter 'y' for Yes or 'n' for No.")


Python
# --- Terminal Booking Workflow ---


def run_booking_cli():
    print("=========================================")
    print("   WELCOME TO THE AIRLINE BOOKING CLI    ")
    print("=========================================")
    print("Select Ticket Class:")
    print("[1] Economy")
    print("[2] Business")
    print("[3] First Class")

    # 1. Select Class with validation
    while True:
        choice = input("Enter choice (1, 2, or 3): ").strip()
        if choice in ("1", "2", "3"):
            break
        print("Invalid selection. Please enter 1, 2, or 3.")

    print("\n--- Enter Passenger Details ---")
    # 2. Collect Base Flight Details
    name = get_non_empty_input("Full Name: ")
    location = get_non_empty_input("Departure City: ")
    destination = get_non_empty_input("Destination City: ")
    date = get_non_empty_input("Travel Date (e.g., YYYY-MM-DD): ")

    # 3. Dynamic Data Entry & Instantiation
    if choice == "1":
        seat_pref = get_non_empty_input("Seat Preference (Window/Aisle/Middle): ")
        passenger = EconomyPassenger(name, location, destination, date, seat_pref)

    elif choice == "2":
        lounge_code = get_non_empty_input("Lounge Pass Code: ")
        passenger = BusinessPassenger(name, location, destination, date, lounge_code)

    else:  # choice == "3"
        suite_num = get_non_empty_input("Suite Number: ")
        chauffeur = get_yes_no_input("Include Chauffeur Service? (y/n): ")
        passenger = FirstClassPassenger(
            name, location, destination, date, suite_num, chauffeur
        )

    # 4. Summary Output
    print("\n=========================================")
    print("         BOOKING CONFIRMATION            ")
    print("=========================================")
    print(passenger.get_passenger_info())
    print("=========================================")


if __name__ == "__main__":
    run_booking_cli()


