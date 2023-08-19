class Guest:
    def __init__(self, guest_id, first_name, last_name):
        self.id = guest_id
        self.first_name = first_name
        self.last_name = last_name
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def get_newest_reservation(self):
        return self.reservations[-1]