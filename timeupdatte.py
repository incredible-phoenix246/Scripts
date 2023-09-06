import pytz
from datetime import datetime

def convert_timezone(input_datetime, from_timezone, to_timezone):
    # Create timezone objects
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)

    # Convert the input datetime from the source timezone to the target timezone
    input_datetime = from_tz.localize(input_datetime)
    converted_datetime = input_datetime.astimezone(to_tz)

    return converted_datetime

if __name__ == "__main__":
    # Get a list of available time zones
    available_timezones = pytz.all_timezones

    # Prompt the user to select the source timezone
    print("Available time zones:")
    for i, tz in enumerate(available_timezones):
        print(f"{i + 1}. {tz}")
    
    source_timezone_index = int(input("Enter the number of the source timezone: ")) - 1
    from_timezone = available_timezones[source_timezone_index]

    # Prompt the user to select the target timezone
    target_timezone_index = int(input("Enter the number of the target timezone: ")) - 1
    target_timezone = available_timezones[target_timezone_index]

    # Ask the user for the year, month, day, hour, minute, and second
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day (1-31): "))
    hour = int(input("Enter the hour (0-23): "))
    minute = int(input("Enter the minute (0-59): "))
    second = int(input("Enter the second (0-59): "))

    # Create the input datetime based on user input
    input_datetime = datetime(year, month, day, hour, minute, second, tzinfo=pytz.utc)

    # Convert the datetime based on user input
    converted_datetime = convert_timezone(input_datetime, from_timezone, target_timezone)

    print(f"{from_timezone} Time: {input_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"{target_timezone} Time: {converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}")
