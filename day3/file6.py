import holidays
import calendar
import json
import os


def get_input():
    '''
    This function prompts the user to input a year and month.
    '''
    year = int(input("Enter year (e.g., 2024): "))
    month = int(input("Enter month (1-12): "))
    return year, month

def get_worker_name():
    '''
    This function retrieves the name of a worker from a worker dictionary.
    '''
    worker_data = filter_eligible_workers()
    names = []

    for worker in worker_data:
        names.append(worker.get("name"))

    return names

# Create a helper funtion to get the schedule directory path
# This will help us reuse code instead of repeating the same code multiple times
def get_schedule_directory():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    schedule_dir = os.path.join(current_dir, "schedule")
    os.makedirs(schedule_dir, exist_ok=True) # Ensure schedule directory exists
    return current_dir, schedule_dir


def count_eligible_workers():
    '''
    This function counts and returns the number of eligible workers
    based on their status.
    '''
    eligible_workers = filter_eligible_workers()
    count = len(eligible_workers)
    print(f"Number of eligible workers: {count}")
    return count

def filter_eligible_workers():
    '''
    This function filters and returns the list of eligible workers
    based on their status.
    '''
    current_dir, schedule_dir = get_schedule_directory()
    path_to_workers = os.path.join(schedule_dir, "workers.json")

    with open(path_to_workers, "r") as f:
        workers = json.load(f)["workers"]

    leave_keys = ["concediu_medical", "concediu_odihna", "concediu_ingrijire_copil"]

    eligible_workers = [worker for worker in workers 
                        if not worker.get("busy", False)
                        and all(not worker.get(leave, False) for leave in leave_keys)
                        and worker.get("role") not in ["sef", "subsef"]
                        ]
    return eligible_workers

def get_working_hours_per_worker(year, month):
    '''
    This function retrieves the standard working hours per worker.
    '''
    if year is None or month is None:
        year, month = get_input()

    working_days = calculate_working_days(year, month)
    hours = 8
    hours_per_worker = working_days * hours
    print(f"Working hours per worker in {calendar.month_name[month]} {year}: {hours_per_worker} hours")
    return hours_per_worker
    
def get_holidays(year, month):
    '''
    This function retrieves the holidays for a given month and year in Romania.
    '''
    if year is None or month is None:
        year, month = get_input()

    ro_holidays = holidays.RO(years=year)

    month_holidays = [day for day in ro_holidays if day.month == month]
    print(f"Holidays in {calendar.month_name[month]} {year}: {month_holidays}")
    return month_holidays

# Function to calculate working days in a month
def calculate_working_days(year, month):
    '''
    This function calculates the number of working days in a given month and year,
    excluding weekends and holidays.
    '''
    if year is None or month is None:
        year, month = get_input()

    month_name, month_days, weekend_days, holidays = get_month(year, month)
    working_days_count = month_days - weekend_days - holidays
    print (f"Working days: {working_days_count} ")

    return working_days_count

# Centralized function to get month details
def get_month(year, month):
    '''
    This function returns the month name, total days in the month,
    number of weekend days, and number of holidays for the given month and year.
    '''
    if year is None or month is None:
        year, month = get_input()

    month_name = calendar.month_name[month]
    month_days = calendar.monthrange(year, month)[1]
    weekend_days = sum(1 for day in range(1, month_days + 1)
                   if calendar.weekday(year, month, day) in (5, 6))
    month_holidays = get_holidays(year, month)
    holidays = [day for day in month_holidays if day.weekday() < 5]  # Count only holidays that are not weekends
    holidays_count = len(holidays)
    print(f"{month_name} {year} has {month_days} days, {weekend_days} weekend days, and {holidays_count} holidays during the week.")
    return month_name, month_days, weekend_days, holidays_count

def create_monthly_schedule(year, month):

    if year is None or month is None:
        year, month = get_input()

    current_dir, schedule_dir = get_schedule_directory()

    month_name, month_days = get_month(year, month)[:2]
    print(f"Creating schedule for {month_name} {year} with {month_days}) days.")

    # Initialize schedule dictionary
    schedule = {f"{month_name} {day}": [] for day in range(1, month_days + 1)}    

    # Save schedule to JSON file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_name = f"{month_name}_{year}_schedule.json"
    json_file_path = os.path.join(current_dir, "schedule", json_name)
    
    with open(json_file_path, "w") as f:
        json.dump(schedule, f, indent=4)
    print(f"Schedule for {month_name} {year} has been created and saved to {json_name}.")


if __name__ == "__main__":
    
    # Call for testing
    count_eligible_workers()