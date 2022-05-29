def corrected_ca(measured_ca, normal_alb, measured_alb):
    ca_result = round(measured_ca + 0.8 * (normal_alb - measured_alb), 1)
    ca_mmol = round((measured_ca + 0.8 * (normal_alb - measured_alb)) * 0.2495, 2)
    print('Corrected calcium is ' + str(ca_result) + ' mg/dL ' + 'or ' + str(ca_mmol) + ' mmol/L')


corrected_ca(10.4, 4, 1.8)
