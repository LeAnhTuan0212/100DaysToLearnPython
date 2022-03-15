def is_Leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return True
    # else:
    #     return False
            
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    if is_Leap(year) and month == 2:
        return 29
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 120]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)        