def BMI(units, weight, height):
    if units == 'imperial':
        result_imperial = round(((weight / (height * height)) * 703), 1)
        if result_imperial < 18.5:
            print('BMI is ' + str(result_imperial) + ' and underweight.')

        if 18.5 <= result_imperial <= 24.9:
            print('BMI is ' + str(result_imperial) + ' and normal weight.')

        if 25 <= result_imperial <= 29.9:
            print('BMI is ' + str(result_imperial) + ' and overweight.')

        if 30 <= result_imperial <= 34.9:
            print('BMI is ' + str(result_imperial) + ' and class 1 obese.')

        if 35 <= result_imperial <= 39.9:
            print('BMI is ' + str(result_imperial) + ' and class 2 obese.')

        if result_imperial > 40:
            print('BMI is ' + str(result_imperial) + ' and class 3 obese.')

    if units == 'metric':
        result_metric = round((weight / (height * height)), 1)
        if result_metric < 18.5:
            print('BMI is ' + str(result_metric) + ' and underweight.')

        if 18.5 <= result_metric <= 24.9:
            print('BMI is ' + str(result_metric) + ' and normal weight.')

        if 25 <= result_metric <= 29.9:
            print('BMI is ' + str(result_metric) + ' and overweight.')

        if 30 <= result_metric <= 34.9:
            print('BMI is ' + str(result_metric) + ' and class 1 obese.')

        if 35 <= result_metric <= 39.9:
            print('BMI is ' + str(result_metric) + ' and class 2 obese.')

        if result_metric > 40:
            print('BMI is ' + str(result_metric) + ' and class 3 obese.')


BMI('metric', 80, 1.73)
