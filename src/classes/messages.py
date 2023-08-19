from ..utilities import get_json

class Message:
    def __init__(self, json_path, template_message, user_message):
        message_json = get_json(json_path)

        if template_message is not None:
            self.template = message_json[template_message]
        else:
            self.template = user_message

    def generate_message(self, Company, Guest):
        first_name = Guest.first_name
        last_name = Guest.last_name
        room_number = Guest.reservation["roomNumber"]
        company_name = Company.name
        company_city = Company.city
        time_of_day = Company.get_time_of_day()

        message = self.template.format(first_name = first_name, last_name = last_name, room_number = room_number, company_name = company_name, time_of_day = time_of_day, company_city = company_city)

        return message
