# Functions with Multiple return value

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return (f_name + " " + l_name).title()

print(format_name(input("What is your first name? "), input( "What is your last name? ")))
