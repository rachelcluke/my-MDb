#This file contains additional validation functions 
from datetime import datetime, date, timedelta

def check_for_empty_field(string):
    """Validation function to check if a field is empty (returns True or False)"""
    if string == "":
        return False
    else:
        return True

def check_input_length(input,min,max):
    """Validation function to check the length of an input field (returns True or False)"""
    if (( len(input) > min) and ( len(input) < max)):
        return True
    else:
        return False

def check_date_format(date_input):
    """Validation function to check if entry is a date"""
    try:
        test = bool(datetime.strptime(date_input, "%Y-%m-%d"))
        result = "true"
    except ValueError:
        result = "false"

    if result == "true" :
        return True
    else:
        return False

def check_date_entry(date_input):
    """Validation function to check that the date entered is not in the future and not more than 100 years ago"""
    today = datetime.date.today()
    cutoff_date = today - timedelta(years=100)
    if (date_input <= today) and (date_input >= cutoff_date ):
        return True
    else:
        return False