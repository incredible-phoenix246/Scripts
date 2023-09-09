import re

# Function to analyze log entries
def analyze_logs(log_file):
    error_count = 0
    login_count = 0
    logout_count = 0

    with open(log_file, "r") as file:
        for log_entry in file:
            timestamp, log_level, message = parse_log_entry(log_entry.strip())
            
            if log_level == "ERROR":
                error_count += 1
                print(f"Error at {timestamp}: {message}")
            elif "User logged in" in message:
                login_count += 1
                print(f"User login at {timestamp}")
            elif "User logged out" in message:
                logout_count += 1
                print(f"User logout at {timestamp}")

    print(f"Total Errors: {error_count}")
    print(f"Total Logins: {login_count}")
    print(f"Total Logouts: {logout_count}")

# Function to parse a log entry
def parse_log_entry(log_entry):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+): (.+)"
    match = re.match(pattern, log_entry)
    if match:
        timestamp, log_level, message = match.groups()
        return timestamp, log_level, message
    else:
        return None, None, None

if __name__ == "__main__":
    log_file = input("Enter the path to the log file: ")
    analyze_logs(log_file)
