import os
os.system('clear')
while True:
    print('Welcome to CALCULATOR.\n')
    calc_list = input('Enter problem as 0000 action 0000: ').split(' ')
    first = calc_list[0]
    action = calc_list[1]
    second = calc_list[2]
    calculation = []
    while True:
        if action == '+':
            quot = float(first) + float(second)
            print(f"{first} {action} {second} = {quot}")
            calc_list.clear()
            calculation.clear()
        if action == '*':
            quot = float(first) * float(second)
            print(f"{first} {action} {second} = {quot}")
            calc_list.clear()
            calculation.clear()
        if action == '-':
            quot = float(first) - float(second)
            print(f"{first} {action} {second} = {quot}")
            calc_list.clear()
            calculation.clear()
        if action == '/':
            quot = float(first) / float(second)
            print(f"{first} {action} {second} = {quot}")
            calc_list.clear()
            calculation.clear()
        calculation.append(quot)
        print('To restart calculation type \'r\'')
        print(f"Enter additional as: {quot} action 0000\n")
        q = list(input(f'{quot} '))
        if q == 'r':
            break
        calculation.append(q[0])
        calculation.append(q[2])
        first = calculation[0]
        action = calculation[1]
        second = calculation[2]
        continue


    