def chadsvasc(age, sex, chf, htn, stroke, cvd, dm):
    if age <= 64:
        add_age = 0
    if 65 <= age <= 74:
        add_age = 1
    if age >= 75:
        add_age = 2

    if sex == 'female':
        add_sex = 1
    elif sex == 'male':
        add_sex = 0

    if chf == 'yes':
        add_chf = 1
    elif chf == 'no':
        add_chf = 0

    if htn == 'yes':
        add_htn = 1
    elif htn == 'no':
        add_htn = 0

    if stroke == 'yes':
        add_stroke = 2
    elif stroke == 'no':
        add_stroke = 0

    if cvd == 'yes':
        add_cvd = 1
    elif cvd == 'no':
        add_cvd = 0

    if dm == 'yes':
        add_dm = 1
    elif dm == 'no':
        add_dm = 0

    print('Your CHA2DS2VASc Score is ' + str(add_age + add_sex + add_chf + add_htn + add_stroke + add_cvd + add_dm))


chadsvasc(64, 'female', 'yes', 'no', 'yes', 'no', 'yes')
