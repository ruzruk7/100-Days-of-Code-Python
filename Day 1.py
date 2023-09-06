def tip_calculater():
    '''Calculate how much each indivdual should pay based on any percentage given'''
    bill = float(input("Welcome to Tip Calculator\nWhat was the Total bill? "))
    percent_tip = (int((input("What percentage tip would you like to give? ")))/100)
    split_quantitiy = int(input("How many people to split the bill? "))
    if total >= 1:
        total = bill * percent_tip
        total += bill    
    else:
        total = bill
    pay_per_person = round((total / split_quantitiy), 2)
    
    return print(f"Each person should pay: {pay_per_person}")

tip_calculater()
