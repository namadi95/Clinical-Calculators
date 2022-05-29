age = int(input('Age: '))
weight_kg = float(input('Weight (kg): '))
weight_lb = weight_kg * 2.2  # if needed
height_in = int(input('Height (in): '))
height_cm = height_in / 2.54  # if needed
SCr = float(input('SCr (mg/dL): '))
sex = input('male or female? ')
sex_multiplier = 0.85

if sex == 'female':
    female_ibw = 45.5 + (2.3 * (height_in - 60))
else:
    male_ibw = 50 + (2.3 * (height_in - 60))


def crcl():
    result = ((140 - age) * weight_kg) / (72 * SCr)

    if sex == 'female' and (weight_kg / female_ibw) * 100 >= 120:
        female_adjbw = female_ibw + (0.4 * (weight_kg - female_ibw))
        female_crcl = int(((140 - age) * female_adjbw) / (72 * SCr) * sex_multiplier)
        print('Creatinine clearance is ' + str(female_crcl) + ' mL/min using adjusted body weight.')

    elif sex == 'male' and (weight_kg / male_ibw) * 100 >= 120:
        male_adjbw = male_ibw + (0.4 * (weight_kg - male_ibw))
        male_crcl = int(((140 - age) * male_adjbw) / (72 * SCr))
        print('Creatinine clearance is ' + str(male_crcl) + ' mL/min using adjusted body weight.')

    if sex == 'female' and (weight_kg / female_ibw) * 100 <= 100:
        female_crcl = int(result * sex_multiplier)
        print('Creatinine clearance is ' + str(female_crcl) + ' mL/min using actual body weight.')

    elif sex == 'male' and (weight_kg / male_ibw) * 100 <= 100:
        male_crcl = int(result)
        print('Creatinine clearance is ' + str(male_crcl) + ' mL/min using actual body weight.')

    if sex == 'female' and 100 <= (weight_kg / female_ibw) * 100 <= 120:
        female_crcl = int(((140 - age) * female_ibw) / (72 * SCr) * sex_multiplier)
        print('Creatinine clearance is ' + str(female_crcl) + ' mL/min using ideal body weight.')

    elif sex == 'male' and 100 <= (weight_kg / male_ibw) * 100 <= 120:
        male_crcl = int(((140 - age) * male_ibw) / (72 * SCr))
        print('Creatinine clearance is ' + str(male_crcl) + ' mL/min using ideal body weight.')


crcl()
