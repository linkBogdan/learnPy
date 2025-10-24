import calendar
import json
import os

def create_monthly_schedule(year, month):

    month_name = calendar.month_name[month]
    num_days = calendar.monthrange(year, month)[1]

    schedule = {f"{month_name} {day}": [] for day in range(1, num_days + 1)}    

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_name = f"{month_name}_{year}_schedule.json"
    json_file_path = os.path.join(current_dir, json_name)
    
    with open(json_file_path, "w") as f:
        json.dump(schedule, f, indent=4)
    print(f"Schedule for {month_name} {year} has been created and saved to {json_name}.")

if __name__ == "__main__":
    year = int(input("Enter year (e.g., 2024): "))
    month = int(input("Enter month (1-12): "))
    create_monthly_schedule(year, month)