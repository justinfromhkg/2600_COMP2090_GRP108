from person import Person


class Admin(Person):

    def __init__(self, username, name, email, password, adminLevel=1):
        super().__init__(username, name, email, password)
        self._adminLevel = adminLevel

    def display_role(self):
        return "Admin"

    def __str__(self):
        return (f"Role: {self.display_role()}\n"
                f"Username: {self.get_username()}\n"
                f"Name: {self.get_name()}\n"
                f"Email: {self.get_email()}\n"
                f"Admin Level: {self._adminLevel}")

    def get_admin_level(self):
        return self._adminLevel

    def set_admin_level(self, level):
        self._adminLevel = level

    # -------------------------
    # Admin Permissions
    # -------------------------

    def add_flight(self, system, flight):
        if self._adminLevel >= 2:
            return system.add_flight(flight)
        return "Permission denied"

    def remove_flight(self, system, flight_number):
        if self._adminLevel >= 3:
            return system.remove_flight(flight_number)
        return "Permission denied"

    def update_flight_time(self, system, flight_number, new_time):
        if self._adminLevel >= 3:
            return system.update_flight_time(flight_number, new_time)
        return "Permission denied"

    def view_all_flights(self, system):
        return system.get_all_flights()