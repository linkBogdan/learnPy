import holidays
import calendar
import json
import os

# Observation: I need to check if holiday is already weekend day to avoid double counting.
def get_working_hours_per_worker():
    '''
    This function retrieves the standard working hours per worker.
    '''
    working_days = calculate_working_days(year, month)
    hours = 8
    hours_per_worker = working_days * hours
    print(f"Working hours per worker in {calendar.month_name[month]} {year}: {hours_per_worker} hours")
    return hours_per_worker
    
    

def get_holidays(year, month):
    '''
    This function retrieves the holidays for a given month and year in Romania.
    '''

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

    month_name, month_days, weekend_days, holidays = get_month(year, month)
    working_days_count = month_days - weekend_days - holidays
    print (f"Working days: {working_days_count} ")
    # Meant for testing purposes
    working_days_plus_holidays = month_days - weekend_days
    print (f"Working days plus holidays: {working_days_plus_holidays} ")
    # Will remove later.
    return working_days_count

# Centralized function to get month details
def get_month(year, month):
    '''
    This function returns the month name, total days in the month,
    number of weekend days, and number of holidays for the given month and year.
    '''

    month_name = calendar.month_name[month]
    month_days = calendar.monthrange(year, month)[1]
    weekend_days = sum(1 for day in range(1, month_days + 1)
                   if calendar.weekday(year, month, day) in (5, 6))
    holidays = len(get_holidays(year, month))
    return month_name, month_days, weekend_days, holidays

def create_monthly_schedule(year, month):

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
    year = int(input("Enter year (e.g., 2024): "))
    month = int(input("Enter month (1-12): "))
    # Call for testing
    get_working_hours_per_worker()