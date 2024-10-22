"""This file contains additional validation functions."""
from datetime import datetime, date, timedelta


def check_for_empty_field(string):
    """Validate form field.

    This checks if a field is empty.

    Args:
        string (str): Text content of field.

    Returns:
        Boolean value: True or False.
    """
    if string == "":
        return False
    else:
        return True


def check_input_length(input, min, max):
    """Validate form field.

    This checks if the length of an input fits within a range.

    Args:
        input (str): Text content of field.
        min (int): Minimum length number.
        max (int): Maximum length number.

    Returns:
        Boolean value: True or False.
    """
    if ((len(input) >= min) and (len(input) <= max)):
        return True
    else:
        return False


def check_date_format(date_input):
    """Validate date field.

    This checks if a date is valid.

    Args:
        date_input (date): Date.

    Returns:
        Boolean value: True or False.
    """
    try:
        test = bool(datetime.strptime(date_input, "%Y-%m-%d"))
        result = "true"
    except ValueError:
        result = "false"

    if result == "true":
        return True
    else:
        return False


def check_date_entry(date_input):
    """Validate date is in range.

    This checks if a date is in the set range.

    Args:
        date_input (date): Date.

    Returns:
        Boolean value: True or False.
    """
    formatted_date_input = datetime.strptime(date_input, "%Y-%m-%d").date()
    today = date.today()
    cutoff_date = today - timedelta(days=(365*100))
    if (formatted_date_input <= today) and (formatted_date_input >= cutoff_date):
        return True
    else:
        return False
