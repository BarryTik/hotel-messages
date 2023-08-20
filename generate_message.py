# Import classes
from src.classes.companies import Company
from src.classes.guests import Guest
from src.classes.messages import Message
# Import utility functions
from src.utilities import (
    get_args
)

def main():
    args = get_args()

    NewGuest = Guest(args.guest_id, "data/Guests.json")
    NewCompany = Company(args.company_id, "data/Companies.json")
    NewMessage = Message("data/Messages.json", args.template, args.user_message)
    message = NewMessage.generate_message(NewCompany, NewGuest)
    
    print(message)

if __name__ == "__main__":
    main()