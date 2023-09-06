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
    # Ask the user for the source timezone
    from_timezone = input("Enter the source timezone (e.g., UTC, America/New_York): ")

    # Ask the user for the target timezone
    target_timezone = input("Enter the target timezone (e.g., UTC, America/New_York): ")

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
