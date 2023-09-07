#BMI CALCULATOR
def bmi_calculaor():
    '''Finds your Body Mass Index and its interpretation. Allows user to choose Kg or Lbs'''
    system = input("What system will you use for mesurements?\nEnter: 'IMPERIAL' for (inches and pounds) or 'METRIC' for (Kilograms and meters).\nEntered: ").lower()
    if system == 'imperial':
        weight = float(input('Please enter your weight in pounds(lbs): '))
        height = float(input('Please enter your height in inches: '))
        BMI = round(((weight/(height**2)) * 703), 2)
    elif system == 'metric': 
        weight = float(input('Please enter your weight in Kilograms(kg): '))
        height = float(input('Please enter your height in Centimeters(cm): '))
        BMI = round((weight/(height**2)),2)
    if BMI <= 18.4:
        return print(f'Your BMI is {BMI}, you are underweight. Suggestion: Eat more protien while working out')
    if BMI >= 18.5 and BMI <= 24.9:
        return print(f'Your BMI is {BMI}, you are normal. Suggestion: If you are weak, then workout and eat more protien.\nIf you are healthy just continue doing what you are doing while making sure you get your micro and macro nutrients daily.')
    if BMI >= 25.0 and BMI <=39.9:
        return print(f'Your BMI is {BMI}, you are overweight. Suggestion: If you are bulking and are seeing strength gains then try to reduce fats and carbs by a little but maintain proper protien intake and incorporate some cardio.\nIf you are not working out (then start) or cannot due to injury, greatly reduce your calories by eating less.\nHowever, continue eating your daily protien requirement and make sure you get your micronutrients(vitamins and minerals)\n'
                     'NOTE: You WILL start feeling hungry all the time. DO NOT EAT, get used to that feeling and embrace it.')
    if BMI >= 40:
        return print(f'Your BMI is {BMI}, you are obese. Suggestion: start body building, incorporate 1-2 days a week of rigurous cardio.\nThings you can do standing or walking(talking on the phone, reading a book, etc..)do them while walking or standing.'
                     '\nIf you want to do a drastic weightloss, gradually remove fats and carbs altogether, while maintaing proper protein intake from lean sources(whey protien isolate powder only is a great option) and take a multivitmin sourced from whole foods and sufficient calcium through supplementation.\n'
                     'If you want to do a gradual weightloss, measure how much you eat and gradully reduce food intake by small amounts, while ensuring sufficient protien intake from lean sources and micronutrients from supplementation.\nThen within 1-2 weeks see if you are losing weight(measure early morning), if you are then continue eating and working out as much as you are.\n'
                     'If you are not losing weight then sufficiently increase activity and further reduce how much you eat some more. and repeat the measuring process.\n'
                     'NOTE: You WILL start feeling hungry all the time. DO NOT EAT, get used to that feeling and embrace it. Feeling hungry is what comes trying to lose weight.')

bmi_calculaor()

