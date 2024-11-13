#05-DaysoftheMonth

# Dictionary mapping month numbers to the number of days in each month
month_days = {
    1: 31,    # January
    2: 28,    # February
    3: 31,    # March
    4: 30,    # April
    5: 31,    # May
    6: 30,    # June
    7: 31,    # July
    8: 31,    # August
    9: 30,    # September
    10: 31,   # October
    11: 30,   # November
    12: 31    # December
}

# Ask the user for the month number
month = int(input("Enter the month number (1-12): "))

# Check if the month number is valid
if 1 <= month <= 12:
    print(f"There are {month_days[month]} days in month {month}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
