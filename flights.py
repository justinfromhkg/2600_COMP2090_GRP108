class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        # encapsulation
        self._flight_number = flight_number
        self._origin = origin
        self._destination = destination
        self._departure_time = departure_time
        self._capacity = capacity
        self._booked_passengers = []

    # -------------------------
    # Getter methods
    # -------------------------
    def get_flight_number(self):
        return self._flight_number

    def get_origin(self):
        return self._origin

    def get_destination(self):
        return self._destination

    def get_departure_time(self):
        return self._departure_time

    def get_available_seats(self):
        return self._capacity - len(self._booked_passengers)

    def get_passenger_list(self):
        return self._booked_passengers

    # -------------------------
    # Setter
    # -------------------------
    def set_departure_time(self, new_time):
        self._departure_time = new_time

    # -------------------------
    # Booking logic
    # -------------------------
    def get_passenger_list(self):
        return self._booked_passengers
    
    def add_passenger(self, passenger):
        if self.get_available_seats() > 0:
            self._booked_passengers.append(passenger)
            return True
        return False

    def remove_passenger(self, passenger):
        if passenger in self._booked_passengers:
            self._booked_passengers.remove(passenger)
            return True
        return False

    def __str__(self):
        return (f"Flight: {self._flight_number} | "
                f"{self._origin} → {self._destination} | "
                f"Departure: {self._departure_time} | "
                f"Available Seats: {self.get_available_seats()}")