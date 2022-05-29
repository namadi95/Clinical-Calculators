def hasbled(htn, renaldys, liverdys, stroke, bleed, labileinr, age, rxbleed, etoh):
    if htn == 'yes':  # htn is uncontrolled, >160 mmHg systolic
        add_htn = 1
    elif htn == 'no':
        add_htn = 0

    if renaldys == 'yes':  # renal dysfunction = chronic dialysis, transplant, or SCr >200 mmol
        add_renaldys = 1
    elif renaldys == 'no':
        add_renaldys = 0

    if liverdys == 'yes':  # liver_dysfunction = chronic hepatic disease, bilirubin 2-3x ULN, or AST/ALT/Alk Phos 3x ULN (ULN = upper limit of normal)
        add_liverdys = 1
    elif liverdys == 'no':
        add_liverdys = 0

    if stroke == 'yes':
        add_stroke = 1
    elif stroke == 'no':
        add_stroke = 0

    if bleed == 'yes':  # bleeding tendency = anemia, history of bleed
        add_bleed = 1
    elif stroke == 'no':
        add_bleed = 0

    if labileinr == 'yes':  # if on warfarin, TTR < 60%) TTR = time to therapeutic range
        add_labileinr = 1
    elif stroke == 'no':
        add_labileinr = 0

    if age == 'yes':  # age > 65
        add_age = 1
    elif age == 'no':
        add_age = 0

    if rxbleed == 'yes':  # drugs that promote bleeding = NSAIDs or antiplatelets
        add_rxbleed = 1
    elif rxbleed == 'no':
        add_rxbleed = 0

    if etoh == 'yes':
        add_etoh = 1
    elif etoh == 'no':
        add_etoh = 0

    print('Your HAS-BLED Score is ' + str(
        add_htn + add_renaldys + add_liverdys + add_stroke + add_bleed + add_labileinr + add_age + add_rxbleed + add_etoh))


hasbled('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
