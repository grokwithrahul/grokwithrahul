from datetime import datetime

flight_locations = ["Delhi", "New York", "Sydney", "Beijing", "Berlin", "San Fransisco"]
flight_times = [100, 530, 1200, 1530, 1700, 1930, 2130, 2230]

now = 0

def flightsearch(location):
    if location in flight_locations:
        now = datetime.now()
        current_time = now.strftime("%H%M")
        current_time = int(current_time)
        for flightime in flight_times:
            if (flightime > current_time):
                next_flight = str(flightime)
                current_time = str(current_time)
                response = "The current time is " + current_time + ", and the next flight to " + location + " takes off at " + next_flight
                return(response)
                break
    else:
        response = "Sorry, there aren't any flights to " + location + " at this moment."
        return(response)
