class System:

    def __init__(self):
        self._flights = []
        self._users = []

    # -------------------------
    # User Management
    # -------------------------
    def register_user(self, user):
        self._users.append(user)
        return "User registered successfully"

    def get_all_users(self):
        return self._users

    # -------------------------
    # Flight Management
    # -------------------------
    def add_flight(self, flight):
        self._flights.append(flight)
        return "Flight added successfully"

    def remove_flight(self, flight_number):
        for flight in self._flights:
            if flight.get_flight_number() == flight_number:
                self._flights.remove(flight)
                return "Flight removed successfully"
        return "Flight not found"

    def get_all_flights(self):
        return self._flights

    def search_flight(self, keyword):
        result = []
        for flight in self._flights:
            if (keyword.lower() in flight.get_flight_number().lower()
                    or keyword.lower() in flight.get_origin().lower()
                    or keyword.lower() in flight.get_destination().lower()):
                result.append(flight)
        return result

    def update_flight_time(self, flight_number, new_time):
        for flight in self._flights:
            if flight.get_flight_number() == flight_number:
                flight.set_departure_time(new_time)
                return "Flight time updated"
        return "Flight not found"

    # -------------------------
    # Booking Logic
    # -------------------------
    def book_flight(self, passenger, flight_number):
        for flight in self._flights:
            if flight.get_flight_number() == flight_number:
                if flight.add_passenger(passenger):
                    return "Booking successful"
                return "No available seats"
        return "Flight not found"

    def cancel_booking(self, passenger, flight_number):
        for flight in self._flights:
            if flight.get_flight_number() == flight_number:
                if flight.remove_passenger(passenger):
                    return "Booking cancelled"
                return "Passenger not booked on this flight"

        return "Flight not found"
