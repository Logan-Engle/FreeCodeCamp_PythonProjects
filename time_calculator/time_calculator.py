def add_time(start, duration, day=""):
    """
    Given a start time and a duration returns the new time after that duration has elapsed
    When provided the optional start day parameter will also return the resulting day
    """

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # add the first 12 hours of the day for start times that are PM 
    if start.split(" ")[1] == "AM":
        start_minutes = ((int(start.split(" ")[0].split(":")[0]) * 60) 
                       + (int(start.split(" ")[0].split(":")[1])))
    else:
        start_minutes = ((int(start.split(" ")[0].split(":")[0]) * 60) 
                       + (int(start.split(" ")[0].split(":")[1])) + 720)

    duration_minutes = (int(duration.split(":")[0]) * 60) + (int(duration.split(":")[1]))
    total_minutes = start_minutes + duration_minutes
    number_of_days = total_minutes // 1440
    remaining_minutes = total_minutes % 1440
    new_minutes = (remaining_minutes % 60)
    new_hours = ((remaining_minutes // 60) % 12)
    if new_hours == 0:
        new_hours = 12

    # determine if new time is AM or PM
    if remaining_minutes < 720:
        suffix = "AM"
    else:
        suffix = "PM"

    # string to display the resulting time    
    new_time = f"{str(new_hours)}:{str(new_minutes).rjust(2, '0')} {suffix}"

    # handles case for day parameter passed
    if day != "":
        new_day = f", {days[((days.index(day.lower()) + number_of_days) % 7)].capitalize()}"
        if number_of_days == 0:
            return(f"{new_time}{new_day}")
        elif number_of_days == 1:
            return(f"{new_time}{new_day} (next day)")
        else:
            return(f"{new_time}{new_day} ({str(number_of_days)} days later)")

    # handles case for day parameter not passed
    else:
        if number_of_days == 0:
            return(f"{new_time}")
        elif number_of_days == 1:
            return(f"{new_time} (next day)")
        else:
            return(f"{new_time} ({str(number_of_days)} days later)")