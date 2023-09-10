# X marks the spot
# write code that would put an x in side the specified place
#example :
# Which world do you want to pu the treasure in? enter as: column row
# Entered: 31
#result:
# row1 = ["🌎", "🌎", "X"]
# row2 = ["🌎", "🌎", "🌎"]
# row3 = ["🌎", "🌎", "🌎"]
def treasure_mapper():
    row1 = ["🌎", "🌎", "🌎"]
    row2 = ["🌎", "🌎", "🌎"]
    row3 = ["🌎", "🌎", "🌎"]
    treasure_map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    marker = input('Which world do you want to pu the treasure in? enter as: column\\row\nEntered: ')
    exact_location = list(marker)
    if int(exact_location[0]) == 3:
        exact_location[0] = 2
    if int(exact_location[1]) == 3:    
        exact_location[1] = 2
    if int(exact_location[0]) == 1: 
        exact_location[0] = 0
    if int(exact_location[1]) == 1:
        exact_location[1] = 0
    treasure_map[int(exact_location[1])][int(exact_location[0])] = 'X'

    print(f"{row1}\n{row2}\n{row3}")

        
    

treasure_mapper()