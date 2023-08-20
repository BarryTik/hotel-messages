# hotel-messages
This python script is intended to simulate automated hotel messaging.
It accepts JSON data for companies, guests and message templates and outputs a message with guest, company and time variables filled in.

## Quick Start
Run this script with the command:
```
python generate_message.py <company_id> <guest_id> -t roomReady
```
where `company_id` and `guest_id` are IDs from the data files. 

Continue reading for more run options.

## Usage

This script was developed using Python version 3.7.3

### Required input files
- `data/Companies.json`: a JSON file with data about a company. It should be an array of objects where each object is a company. A company object requires keys for `id` (int), `company` (string), `city` (string) and `timezone` (string, an IANA formatted timezone)
Example company object:
```
    {
        "id": 1,
        "company": "Hotel California",
        "city": "Santa Barbara",
        "timezone": "US/Pacific"
    }
```

- `data/Guests.json`: a JSON file with data about a guest. It should be an array of objects where each object is a guest. A guest object requires keys for `id` (int), `firstName` (string), `lastName` (string) and `reservation`, an object containing `roomNumber` (int). Additional keys are allowed but not currently used.
Example guest object:
```
  {
        "id": 1,
        "firstName": "Candy",
        "lastName": "Pace",
        "reservation": {
            "roomNumber": 529,
            "startTimestamp": 1486654792,
            "endTimestamp": 1486852373
        }
  }
```

- `data/Messages.json`: a JSON file with message templates. An object where keys are message names and values are python formatable strings. See the **Creating Templates** section below.

Example message template:
```
"roomReady": "Good {time_of_day} {first_name}, and welcome to {company_name}! Room {room_number} is now ready for you. Enjoy your stay, and let us know if you need anything."
```

### Command Line Arguments
#### Required Positional Arguments
- `company_id` An integer corresponding to an `id` key in the `Companies.json` file.
- `guest_id` An integer corresponding to an `id` key in the `Guests.json` file.

#### Flag Arguments
One of the following options must be used.
- `--template` or `-t` A string corresponding to a key in the `Messages.json` file.
- `--message` or `-m` A python formatable string. See the **Creating Templates** section below.

### Creating Templates
A template can be placed in the `Messages.json` file or input as a command line argument with the `--message` flag.

A template is a string with braces `{}` in the middle. These braces are to be filled with a variable name (below) that will be replaced. For more information see [Python's documentation on string formatting](https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method).

Currently supported replacement strings are:
1. `first_name`: Will be replaced with the guest's first name
2. `last_name`: Will be replaced with the guest's last name
3. `room_number`: Will be replaced with the guest's reservation room number
4. `company_name`: Will be replaced with the company's name
5. `company_city`: Will be replaced with the company's city
6. `time_of_day`: Will be replaced with a time of day string matching the current time of day at the company's timezone. `morning`, `afternoon` or `evening`.


## Development Process

### Why Python?
When I hear object-oriented I think classes. Python is a language that I both use in my current role and have experience working with classes in. It is also widely used, easy to start a project in and already installed on my personal computer, which I used for this project.

### Design Decisions

#### Goals

This project was fairly open ended. I was given a bulet point list of requirements, but there was freedom in how to accomplish them.

I had ideas for expanding on these requirements and handling more use cases than were presented, but decided to persue a minimally viable product where it works for the cases supplied, and any other features could be added later.

#### File Layout

I wanted the script that was being run to look fairly simple. Get the arguments, build some objects, and output a message. The outcome of this is a short, intuitive script. 
- The user asked for a specific company, so lets build it.
- The user asked for a specific guest, so here it is.
- The user has a message template they want to populate, so lets grab that.

Then simply throw them all together and thats the message!

To keep this looking clean, I had to do the heavy lifting somwhere else and import it. I put each class in its own file so that they also were clean looking and easy to find. I put shared functions in their own file. You read the import, open that file, and thats whats there. No scrolling through long files searching for what you're looking for. Future people working on this would be able to say, 'I need to add a feature to the guest class' then open `src/classes/guest.py` and its right there. 

#### Input Data

When working with data there is a lot to consider.
What does it look like? 
How representative is the sample I have?
Where on the system will it be compared to my script?
Who is going to access or change it?

I considered more expansive and adaptable solutions, but in the end decided to assume that all of the data this program used would always look exactly like my sample, and end up in the same place. The rest seemed out of scope for this exercise. In the **Next Steps** section I breifly discuss handling incomplete data and different file paths.

I played around with several different ways to structure the message template JSON, and landed on one that is quite simple. While having every template as a key value pair could be hard to search through if the file fills up, having multiple files seemed unreasonable for the small amount of data and having nested layers of categories led to too much user input to find the desired template. 

#### Time of Day

Outside of overarching design decisions this was the most intensive part of writing this script. I discuss incrimentally building and testing it below.
A particularly interesting part of this was deciding when it is appropriate to use what greeting. I based my cut-off hour on the [wikipedia article for morning](https://en.wikipedia.org/wiki/Morning#:~:text=As%20a%20general%20rule%2C%20the,is%20used%20as%20the%20latter.) but left these cut-offs as variables that could be edited in the `Company` class. I didn't see a user changing these regularly so I didn't make them into a command line argument, but wanted them clearly noticible so that if an internal policy decision was made they could be easily modified.


### Testing

The part of this script that I spent the most time testing was the `get_time_of_day` method. As I worked through the intricacies of the `datetime` package I repeatedly ran this function. I made timezone_test.py which imported it, ran it for several different timezone input strings and printed the outputs. As I built out the function I progressed from printing entire datetime strings, to hours, to time of day strings. I later decided this would be a better fit as a class method, so I moved it and this test script won't work anymore.

Once I had everthing connected, I tested the whole script by adding some new objects to the provided data JSONs. My particular interest was in ensuring that the time of day functionality worked so I tested objects with timezones all across the world.

### Next Steps

1. Input validation. 

    Currently there is no input validation in this script.
    A user can input invalid data files or command line arguments and the program will error without any helpful messages. 
    
    My next steps would be to enforce command line argument types, throw helpful error messages to the user when they input IDs that do not appear in data files, and require the user to pick either -t or -m as the script will not run without one of these.

    Potential future steps would include validation of JSON files to ensure the data they supply is in the correct format, and adapting the code to allow for incomplete data by either supplying defaults or preventing users from using templates that ask for missing data.

1. Flexible data file input

    Currently the JSON paths are hard coded to the supplied files. I would like to give the user an option to supply their own filepaths through the command line.

1. Support for more template variables

    Templates currently accept the 6 variables listed above. I would like to support more variables, such as the reservation timestamps in the supplied `Guests.json`. This could easily be done by modifying the `generate_message` method in the `Message` class.