
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


