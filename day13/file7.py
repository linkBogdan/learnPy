# Refactor for this:

from datetime import date
import os

def get_path(): 
    """ Retrun the path to the root. """
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    return root_path

def create_today_dir():
    """ Create a directory with current day"""
    dir_name = get_day()
    root = get_path()
    full_path = os.path.join(root, dir_name)

    os.makedirs(full_path, exist_ok=True)
    print(f"Directory ready: {full_path}")
    return full_path

def get_day():
    """ Return today's day folder name and start date"""

    start_date = date(2025, 10, 22)
    today = date.today()

    days_passed = (today - start_date).days + 1 # +1 if day 1 = start day
    dir_format_name = f"day{days_passed}"
    
    return dir_format_name

if __name__ == "__main__":
    create_today_dir()