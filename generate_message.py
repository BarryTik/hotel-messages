# Import classes
from src.classes.companies import Company
from src.classes.guests import Guest
from src.classes.reservations import Reservation
from src.classes.messages import Message
# Import utility functions
from src.utilities import (
    get_args
)

def main():
    args = get_args()

    company_id = args.company_id
    guest_id = args.guest_id
    template_message = args.template
    user_message = args.user_message

    NewGuest = Guest(guest_id, "data/Guests.json")
    NewCompany = Company(company_id, "data/Companies.json")
    NewMessage = Message("templates/hotel-messages.json", template_message, user_message)
    message = NewMessage.generate_message(NewCompany, NewGuest)
    
    print(message)

if __name__ == "__main__":
    main()