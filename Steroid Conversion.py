doseeq_hydrocortisone = 20
doseeq_cortisone = 25
doseeq_prednisone = 5
doseeq_prednisolone = 5
doseeq_methylprednisolone = 4
doseeq_triamcinolone = 4
doseeq_dexamethasone = 0.75
doseeq_betamethasone = 0.6


def steroidconv(drug_from, dose_from, drug_to):
# From Hydrocortisone
    if drug_from == 'hydrocortisone' and drug_to == 'cortisone':
        final_conv = (doseeq_cortisone * dose_from) / doseeq_hydrocortisone
        print(str(final_conv) + ' mg of cortisone')

    if drug_from == 'hydrocortisone' and drug_to == 'prednisone':
        final_conv = (doseeq_prednisone * dose_from) / doseeq_hydrocortisone
        print(str(final_conv) + ' mg of prednisone')

    if drug_from == 'hydrocortisone' and drug_to == 'prednisolone':
        final_conv = (doseeq_prednisolone * dose_from) / doseeq_hydrocortisone
        print(str(final_conv) + ' mg of prednisolone')

    if drug_from == 'hydrocortisone' and drug_to == 'methylprednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_hydrocortisone
        print(str(final_conv) + ' mg of methylprednisolone')

    if drug_from == 'hydrocortisone' and drug_to == 'triamcinolone':
        final_conv = (doseeq_triamcinolone * dose_from) / doseeq_hydrocortisone
        print(str(final_conv) + ' mg of triamcinolone')

    if drug_from == 'hydrocortisone' and drug_to == 'dexamethasone':
        final_conv = (doseeq_dexamethasone * dose_from) / doseeq_hydrocortisone
        print(str(final_conv) + ' mg of dexamethasone')

    if drug_from == 'hydrocortisone' and drug_to == 'betamethasone':
        final_conv = (doseeq_betamethasone * dose_from) / doseeq_hydrocortisone
        print(str(final_conv) + ' mg of betamethasone')

# From Cortisone
    if drug_from == 'cortisone' and drug_to == 'hydrocortisone':
        final_conv = (doseeq_hydrocortisone * dose_from) / doseeq_cortisone
        print(str(final_conv) + ' mg of hydrocortisone')

    if drug_from == 'cortisone' and drug_to == 'prednisone':
        final_conv = (doseeq_prednisone * dose_from) / doseeq_cortisone
        print(str(final_conv) + ' mg of prednisone')

    if drug_from == 'cortisone' and drug_to == 'prednisolone':
        final_conv = (doseeq_prednisolone * dose_from) / doseeq_cortisone
        print(str(final_conv) + ' mg of prednisolone')

    if drug_from == 'cortisone' and drug_to == 'methylprednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_cortisone
        print(str(final_conv) + ' mg of methylprednisolone')

    if drug_from == 'cortisone' and drug_to == 'triamcinolone':
        final_conv = (doseeq_triamcinolone * dose_from) / doseeq_cortisone
        print(str(final_conv) + ' mg of triamcinolone')

    if drug_from == 'cortisone' and drug_to == 'dexamethasone':
        final_conv = (doseeq_dexamethasone * dose_from) / doseeq_cortisone
        print(str(final_conv) + ' mg of dexamethasone')

    if drug_from == 'cortisone' and drug_to == 'betamethasone':
        final_conv = (doseeq_betamethasone * dose_from) / doseeq_cortisone
        print(str(final_conv) + ' mg of betamethasone')

# From Prednisone
    if drug_from == 'prednisone' and drug_to == 'hydrocortisone':
        final_conv = (doseeq_hydrocortisone * dose_from) / doseeq_prednisone
        print(str(final_conv) + ' mg of hydrocortisone')

    if drug_from == 'prednisone' and drug_to == 'cortisone':
        final_conv = (doseeq_cortisone * dose_from) / doseeq_prednisone
        print(str(final_conv) + ' mg of cortisone')

    if drug_from == 'prednisone' and drug_to == 'prednisolone':
        final_conv = (doseeq_prednisolone * dose_from) / doseeq_prednisone
        print(str(final_conv) + ' mg of prednisolone')

    if drug_from == 'prednisone' and drug_to == 'methylprednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_prednisone
        print(str(final_conv) + ' mg of methylprednisolone')

    if drug_from == 'prednisone' and drug_to == 'triamcinolone':
        final_conv = (doseeq_triamcinolone * dose_from) / doseeq_prednisone
        print(str(final_conv) + ' mg of triamcinolone')

    if drug_from == 'prednisone' and drug_to == 'dexamethasone':
        final_conv = (doseeq_dexamethasone * dose_from) / doseeq_prednisone
        print(str(final_conv) + ' mg of dexamethasone')

    if drug_from == 'prednisone' and drug_to == 'betamethasone':
        final_conv = (doseeq_betamethasone * dose_from) / doseeq_prednisone
        print(str(final_conv) + ' mg of betamethasone')

# From Prednisolone
    if drug_from == 'prednisolone' and drug_to == 'hydrocortisone':
        final_conv = (doseeq_hydrocortisone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of hydrocortisone')

    if drug_from == 'prednisolone' and drug_to == 'cortisone':
        final_conv = (doseeq_cortisone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of cortisone')

    if drug_from == 'prednisolone' and drug_to == 'prednisone':
        final_conv = (doseeq_prednisone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of prednisone')

    if drug_from == 'prednisolone' and drug_to == 'methylprednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of methylprednisolone')

    if drug_from == 'prednisolone' and drug_to == 'triamcinolone':
        final_conv = (doseeq_triamcinolone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of triamcinolone')

    if drug_from == 'prednisolone' and drug_to == 'dexamethasone':
        final_conv = (doseeq_dexamethasone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of dexamethasone')

    if drug_from == 'prednisolone' and drug_to == 'betamethasone':
        final_conv = (doseeq_betamethasone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of betamethasone')

# From Methylprednisolone
    if drug_from == 'methylprednisolone' and drug_to == 'hydrocortisone':
        final_conv = (doseeq_hydrocortisone * dose_from) / doseeq_methylprednisolone
        print(str(final_conv) + ' mg of hydrocortisone')

    if drug_from == 'methylprednisolone' and drug_to == 'cortisone':
        final_conv = (doseeq_cortisone * dose_from) / doseeq_methylprednisolone
        print(str(final_conv) + ' mg of cortisone')

    if drug_from == 'methylprednisolone' and drug_to == 'prednisone':
        final_conv = (doseeq_prednisone * dose_from) / doseeq_methylprednisolone
        print(str(final_conv) + ' mg of prednisone')

    if drug_from == 'methylprednisolone' and drug_to == 'prednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_prednisolone
        print(str(final_conv) + ' mg of prednisolone')

    if drug_from == 'methylprednisolone' and drug_to == 'triamcinolone':
        final_conv = (doseeq_triamcinolone * dose_from) / doseeq_methylprednisolone
        print(str(final_conv) + ' mg of triamcinolone')

    if drug_from == 'methylprednisolone' and drug_to == 'dexamethasone':
        final_conv = (doseeq_dexamethasone * dose_from) / doseeq_methylprednisolone
        print(str(final_conv) + ' mg of dexamethasone')

    if drug_from == 'methylprednisolone' and drug_to == 'betamethasone':
        final_conv = (doseeq_betamethasone * dose_from) / doseeq_methylprednisolone
        print(str(final_conv) + ' mg of betamethasone')

# From Triamcinolone
    if drug_from == 'triamcinolone' and drug_to == 'hydrocortisone':
        final_conv = (doseeq_hydrocortisone * dose_from) / doseeq_triamcinolone
        print(str(final_conv) + ' mg of hydrocortisone')

    if drug_from == 'triamcinolone' and drug_to == 'cortisone':
        final_conv = (doseeq_cortisone * dose_from) / doseeq_triamcinolone
        print(str(final_conv) + ' mg of cortisone')

    if drug_from == 'triamcinolone' and drug_to == 'prednisone':
        final_conv = (doseeq_prednisone * dose_from) / doseeq_triamcinolone
        print(str(final_conv) + ' mg of prednisone')

    if drug_from == 'triamcinolone' and drug_to == 'methylprednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_triamcinolone
        print(str(final_conv) + ' mg of methylprednisolone')

    if drug_from == 'triamcinolone' and drug_to == 'prednisolone':
        final_conv = (doseeq_prednisolone * dose_from) / doseeq_triamcinolone
        print(str(final_conv) + ' mg of prednisolone')

    if drug_from == 'triamcinolone' and drug_to == 'dexamethasone':
        final_conv = (doseeq_dexamethasone * dose_from) / doseeq_triamcinolone
        print(str(final_conv) + ' mg of dexamethasone')

    if drug_from == 'triamcinolone' and drug_to == 'betamethasone':
        final_conv = (doseeq_betamethasone * dose_from) / doseeq_triamcinolone
        print(str(final_conv) + ' mg of betamethasone')

# From Dexamethasone
    if drug_from == 'dexamethasone' and drug_to == 'hydrocortisone':
        final_conv = (doseeq_hydrocortisone * dose_from) / doseeq_dexamethasone
        print(str(final_conv) + ' mg of hydrocortisone')

    if drug_from == 'dexamethasone' and drug_to == 'cortisone':
        final_conv = (doseeq_cortisone * dose_from) / doseeq_dexamethasone
        print(str(final_conv) + ' mg of cortisone')

    if drug_from == 'dexamethasone' and drug_to == 'prednisone':
        final_conv = (doseeq_prednisone * dose_from) / doseeq_dexamethasone
        print(str(final_conv) + ' mg of prednisone')

    if drug_from == 'dexamethasone' and drug_to == 'methylprednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_dexamethasone
        print(str(final_conv) + ' mg of methylprednisolone')

    if drug_from == 'dexamethasone' and drug_to == 'triamcinolone':
        final_conv = (doseeq_triamcinolone * dose_from) / doseeq_dexamethasone
        print(str(final_conv) + ' mg of triamcinolone')

    if drug_from == 'dexamethasone' and drug_to == 'prednisolone':
        final_conv = (doseeq_prednisolone * dose_from) / doseeq_dexamethasone
        print(str(final_conv) + ' mg of prednisolone')

    if drug_from == 'dexamethasone' and drug_to == 'betamethasone':
        final_conv = (doseeq_betamethasone * dose_from) / doseeq_dexamethasone
        print(str(final_conv) + ' mg of betamethasone')

# From Betamethasone
    if drug_from == 'betamethasone' and drug_to == 'hydrocortisone':
        final_conv = (doseeq_hydrocortisone * dose_from) / doseeq_betamethasone
        print(str(final_conv) + ' mg of hydrocortisone')

    if drug_from == 'betamethasone' and drug_to == 'cortisone':
        final_conv = (doseeq_cortisone * dose_from) / doseeq_betamethasone
        print(str(final_conv) + ' mg of cortisone')

    if drug_from == 'betamethasone' and drug_to == 'prednisone':
        final_conv = (doseeq_prednisone * dose_from) / doseeq_betamethasone
        print(str(final_conv) + ' mg of prednisone')

    if drug_from == 'betamethasone' and drug_to == 'methylprednisolone':
        final_conv = (doseeq_methylprednisolone * dose_from) / doseeq_betamethasone
        print(str(final_conv) + ' mg of methylprednisolone')

    if drug_from == 'betamethasone' and drug_to == 'triamcinolone':
        final_conv = (doseeq_triamcinolone * dose_from) / doseeq_betamethasone
        print(str(final_conv) + ' mg of triamcinolone')

    if drug_from == 'betamethasone' and drug_to == 'dexamethasone':
        final_conv = (doseeq_dexamethasone * dose_from) / doseeq_betamethasone
        print(str(final_conv) + ' mg of dexamethasone')

    if drug_from == 'betamethasone' and drug_to == 'prednisolone':
        final_conv = (doseeq_prednisolone * dose_from) / doseeq_betamethasone
        print(str(final_conv) + ' mg of prednisolone')

steroidconv('betamethasone', 40, 'dexamethasone')
