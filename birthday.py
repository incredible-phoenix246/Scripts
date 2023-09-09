import datetime

# Dictionary to store birthday data (name as key, birthday as value)
birthday_dict = {}

# Function to add a new birthday
def add_birthday():
    name = input("Enter the name: ")
    dob = input("Enter the date of birth (YYYY-MM-DD): ")

    try:
        dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d")
        birthday_dict[name] = dob_date
        print(f"{name}'s birthday added successfully!")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Function to edit a birthday
def edit_birthday():
    name = input("Enter the name whose birthday you want to edit: ")

    if name in birthday_dict:
        new_dob = input("Enter the new date of birth (YYYY-MM-DD): ")
        try:
            dob_date = datetime.datetime.strptime(new_dob, "%Y-%m-%d")
            birthday_dict[name] = dob_date
            print(f"{name}'s birthday updated successfully!")

        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    else:
        print(f"{name} not found in the birthday list.")

# Function to search for a birthday by name
def search_birthday():
    name = input("Enter the name to search for: ")

    if name in birthday_dict:
        print(f"{name}'s birthday: {birthday_dict[name].strftime('%Y-%m-%d')}")
    else:
        print(f"{name} not found in the birthday list.")

# Function to display upcoming birthdays in a month
def upcoming_birthdays():
    month = int(input("Enter the month (1-12) to see upcoming birthdays: "))
    today = datetime.datetime.now()

    upcoming = []
    for name, dob in birthday_dict.items():
        if dob.month == month and dob >= today:
            upcoming.append((name, dob))

    if not upcoming:
        print("No upcoming birthdays in the specified month.")
    else:
        upcoming.sort(key=lambda x: x[1])
        print("Upcoming birthdays in the specified month:")
        for name, dob in upcoming:
            print(f"{name}: {dob.strftime('%Y-%m-%d')}")

# Main menu
while True:
    print("\nBirthday List Management System")
    print("1. Add Birthday")
    print("2. Edit Birthday")
    print("3. Search Birthday")
    print("4. Upcoming Birthdays")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_birthday()
    elif choice == "2":
        edit_birthday()
    elif choice == "3":
        search_birthday()
    elif choice == "4":
        upcoming_birthdays()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
