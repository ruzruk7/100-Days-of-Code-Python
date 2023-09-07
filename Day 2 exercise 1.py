def leap_year_finder():
    year = int(input("Please enter the year to check: "))
    is_leap = 0
    if year % 4 == 0:
        is_leap += 1
    else:
        is_leap -= 1
    if year % 100 == 0:
        is_leap -= 1
    else:
        is_leap += 1
    if year % 400 == 0:
        is_leap += 1
    else:
        is_leap -= 1
    
    if is_leap > 0:
        return print(f'{year} is a Leap year.')
    else:
        return print(f'{year} is not a Leap year')
    

leap_year_finder()

