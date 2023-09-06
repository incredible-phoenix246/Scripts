import pytz
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def convert_timezone(input_datetime, from_timezone, to_timezone):
    # Create timezone objects
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)

    # Convert the input datetime from the source timezone to the target timezone
    input_datetime = from_tz.localize(input_datetime)
    converted_datetime = input_datetime.astimezone(to_tz)

    return converted_datetime

def get_selected_datetime():
    # Get the selected date and time from the calendar and clock
    selected_date = cal.get_date()
    selected_time = clock.get()
    selected_datetime = datetime.combine(selected_date, selected_time)
    
    # Get the source and target time zones from the dropdown menus
    from_timezone = from_timezone_var.get()
    target_timezone = to_timezone_var.get()
    
    # Convert the selected datetime to the target timezone
    converted_datetime = convert_timezone(selected_datetime, from_timezone, target_timezone)
    
    # Update the result label
    result_label.config(text=f"{from_timezone} Time: {selected_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
                            f"{target_timezone} Time: {converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Create the main application window
app = tk.Tk()
app.title("Time Zone Converter")

# Create and configure the calendar widget
cal = Calendar(app, selectmode="day", date_pattern="yyyy-MM-dd")
cal.pack()

# Create and configure the clock widget
clock = ttk.Combobox(app, values=["00:00:00", "01:00:00", "02:00:00", "03:00:00", "04:00:00",
                                  "05:00:00", "06:00:00", "07:00:00", "08:00:00", "09:00:00",
                                  "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00",
                                  "15:00:00", "16:00:00", "17:00:00", "18:00:00", "19:00:00",
                                  "20:00:00", "21:00:00", "22:00:00", "23:00:00"])
clock.set("00:00:00")
clock.pack()

# Create dropdown menus for source and target time zones
available_timezones = pytz.all_timezones
from_timezone_var = tk.StringVar()
from_timezone_label = tk.Label(app, text="Select Source Timezone:")
from_timezone_dropdown = ttk.Combobox(app, textvariable=from_timezone_var, values=available_timezones)
from_timezone_label.pack()
from_timezone_dropdown.pack()

to_timezone_var = tk.StringVar()
to_timezone_label = tk.Label(app, text="Select Target Timezone:")
to_timezone_dropdown = ttk.Combobox(app, textvariable=to_timezone_var, values=available_timezones)
to_timezone_label.pack()
to_timezone_dropdown.pack()

# Create a button to perform the conversion
convert_button = tk.Button(app, text="Convert", command=get_selected_datetime)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(app, text="", justify="left")
result_label.pack()

app.mainloop()
import pytz
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def convert_timezone(input_datetime, from_timezone, to_timezone):
    # Create timezone objects
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)

    # Convert the input datetime from the source timezone to the target timezone
    input_datetime = from_tz.localize(input_datetime)
    converted_datetime = input_datetime.astimezone(to_tz)

    return converted_datetime

def get_selected_datetime():
    # Get the selected date and time from the calendar and clock
    selected_date = cal.get_date()
    selected_time = clock.get()
    selected_datetime = datetime.combine(selected_date, selected_time)
    
    # Get the source and target time zones from the dropdown menus
    from_timezone = from_timezone_var.get()
    target_timezone = to_timezone_var.get()
    
    # Convert the selected datetime to the target timezone
    converted_datetime = convert_timezone(selected_datetime, from_timezone, target_timezone)
    
    # Update the result label
    result_label.config(text=f"{from_timezone} Time: {selected_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
                            f"{target_timezone} Time: {converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Create the main application window
app = tk.Tk()
app.title("Time Zone Converter")

# Create and configure the calendar widget
cal = Calendar(app, selectmode="day", date_pattern="yyyy-MM-dd")
cal.pack()

# Create and configure the clock widget
clock = ttk.Combobox(app, values=["00:00:00", "01:00:00", "02:00:00", "03:00:00", "04:00:00",
                                  "05:00:00", "06:00:00", "07:00:00", "08:00:00", "09:00:00",
                                  "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00",
                                  "15:00:00", "16:00:00", "17:00:00", "18:00:00", "19:00:00",
                                  "20:00:00", "21:00:00", "22:00:00", "23:00:00"])
clock.set("00:00:00")
clock.pack()

# Create dropdown menus for source and target time zones
available_timezones = pytz.all_timezones
from_timezone_var = tk.StringVar()
from_timezone_label = tk.Label(app, text="Select Source Timezone:")
from_timezone_dropdown = ttk.Combobox(app, textvariable=from_timezone_var, values=available_timezones)
from_timezone_label.pack()
from_timezone_dropdown.pack()

to_timezone_var = tk.StringVar()
to_timezone_label = tk.Label(app, text="Select Target Timezone:")
to_timezone_dropdown = ttk.Combobox(app, textvariable=to_timezone_var, values=available_timezones)
to_timezone_label.pack()
to_timezone_dropdown.pack()

# Create a button to perform the conversion
convert_button = tk.Button(app, text="Convert", command=get_selected_datetime)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(app, text="", justify="left")
result_label.pack()

app.mainloop()
