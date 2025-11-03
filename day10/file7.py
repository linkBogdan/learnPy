# Refactor for this:

from datetime import date


def get_day():
    # We define when we started working
    start_date = date(2025, 10, 22)
    today = date.today()

    days_passed = (today - start_date).days + 1 # +1 if day 1 = start day
    
    return days_passed

