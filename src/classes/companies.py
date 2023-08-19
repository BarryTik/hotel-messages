from datetime import datetime
import pytz

class Company:
    def __init__(self, company_id, company_name, city, timezone):
        self.id = company_id
        self.name = company_name
        self.city = city
        self.timezone = timezone

    def get_time_of_day(self):
        """
        Gets the time of day in greeting format, 'morning', 'afternoon' or 'evening'
        Adjust intervals by changing the _start_hour variables.
        :returns time_of_day: String, 'morning', 'afternoon' or 'evening' 
        """
        # set time of day cutoffs
        morning_start_hour = 3
        afternoon_start_hour = 12
        evening_start_hour = 17

        # get hour of day (0 - 24) at input timezone
        local_timezone = pytz.timezone(self.timezone)
        local_time = datetime.now(local_timezone)
        hour = local_time.hour

        # decide time of day string based on hour
        time_of_day = "evening"
        if morning_start_hour <= hour < afternoon_start_hour:
            time_of_day = "morning"
        elif hour < evening_start_hour:
            time_of_day = "afternoon"

        return time_of_day        