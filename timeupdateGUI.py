import pytz
from datetime import datetime, date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from tktimepicker import TimePicker

def convert_timezone(input_datetime, from_timezone, to_timezone):
    # Create timezone objects
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)

    # Convert the input datetime from the source timezone to the target timezone
    input_datetime = from_tz.localize(input_datetime)
    converted_datetime = input_datetime.astimezone(to_tz)

    return converted_datetime

def convert_button_clicked():
    from_timezone = source_timezone_combobox.get()
    target_timezone = target_timezone_combobox.get()
    
    selected_date = calendar.get_date()
    selected_time = time_picker.get()
    
    try:
        year, month, day = map(int, selected_date.split("-"))
        hour, minute = map(int, selected_time.split(":"))
        input_datetime = datetime(year, month, day, hour, minute, tzinfo=pytz.utc)

        converted_datetime = convert_timezone(input_datetime, from_timezone, target_timezone)

        result_label.config(text=f"{from_timezone} Time: {input_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
                                  f"{target_timezone} Time: {converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    except ValueError:
        messagebox.showerror("Error", "Invalid date or time format. Please enter a valid date and time.")

# Create a Tkinter window
window = tk.Tk()
window.title("Time Zone Converter")

# Create and populate the source timezone combobox
source_timezone_label = ttk.Label(window, text="Source Timezone:")
source_timezone_label.pack()
source_timezone_combobox = ttk.Combobox(window, values=pytz.all_timezones)
source_timezone_combobox.pack()

# Create and populate the target timezone combobox
target_timezone_label = ttk.Label(window, text="Target Timezone:")
target_timezone_label.pack()
target_timezone_combobox = ttk.Combobox(window, values=pytz.all_timezones)
target_timezone_combobox.pack()

# Create a calendar widget
calendar_label = ttk.Label(window, text="Select Date:")
calendar_label.pack()
calendar = Calendar(window)
calendar.pack()

# Create a time picker widget
time_label = ttk.Label(window, text="Select Time:")
time_label.pack()
time_picker = TimePicker(window)
time_picker.pack()

# Create a button to trigger the conversion
convert_button = ttk.Button(window, text="Convert", command=convert_button_clicked)
convert_button.pack()

# Create a label to display the result
result_label = ttk.Label(window, text="")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
