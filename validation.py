def check_for_empty_field(string):
    """ Validation function to check if a field is empty (returns True or False) """
    if string == "":
        return False
    else:
        return True

def check_input_length(input,min,max):
    """ Validation function to check the length of an input field (returns True or False) """
    if (( len(input) > min) and ( len(input) < max)):
        return True
    else:
        return False