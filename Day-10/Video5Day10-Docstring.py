# Docstring
# Ex:
"""
    This is a docstring
"""



def format_name(f_name, l_name):
    """
    Take a first and last name and format it to 
    return the title case version of the name
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return (f_name + " " + l_name).title()

print(format_name(input("What is your first name? "), input( "What is your last name? ")))
