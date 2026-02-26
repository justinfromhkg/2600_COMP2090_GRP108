from person import Person


class Passenger(Person):

    def __init__(self, username, name, email, password):
        super().__init__(username, name, email, password)

    # Polymorphism
    def display_role(self):
        return "Passenger"

    def __str__(self):
        return (f"Role: {self.display_role()}\n"
                f"Username: {self.get_username()}\n"
                f"Name: {self.get_name()}\n"
                f"Email: {self.get_email()}")

    # -------------------------
    # Functionalities
    # -------------------------

    def search_flight(self, system, keyword):
        return system.search_flight(keyword)

    def book_flight(self, system, flight_number):
        return system.book_flight(self, flight_number)

    def cancel_booking(self, system, flight_number):
        return system.cancel_booking(self, flight_number)