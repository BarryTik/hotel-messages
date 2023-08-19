from ..utilities import get_json

class Guest:
    def __init__(self, guest_id, json_path):
        self.id = guest_id

        guest_json = get_json(json_path)

        for guest in guest_json:
            if int(guest["id"]) == int(guest_id):
                self.first_name = guest["firstName"]
                self.last_name = guest["lastName"]
                self.reservation = guest["reservation"]