# Comparison of Intensities with WASH Factors

# Which Parasite
i = 'ascaris'
has_parasite = all_data_noSHA[all_data_noSHA[i] > 0].copy()

# Q2
has_parasite['Q2'] = has_parasite['Q2'].replace([4, 6, 7], 1)
has_parasite['Q2'] = has_parasite['Q2'].replace([3, 5], 2)
compare(has_parasite['Q2'], has_parasite[i], 'Water source (1: Unsafe 2: Safer)', 'School Mean {} Intensity'.format(i), 0)

# Q3
has_parasite['Q3'] = has_parasite['Q3'].replace([4, 6, 7], 1)
has_parasite['Q3'] = has_parasite['Q3'].replace([3, 5], 2)
compare(has_parasite['Q3'], has_parasite[i], 'Rainy Season Water source (1: Unsafe 2: Safer)', 'School Mean {} Intensity'.format(i), 0)

# In School Water Source always used
# Q29
always_used = all_data_noSHA[all_data_noSHA['Q1'] == 1].copy()
hist0plot(always_used['Q29'], 7, 'Type of Water Source (In-sch always used)', 0.5, '#1CE692', 1, [1.4285, 2.2855, 3.1425, 3.9995, 4.8565, 5.7136, 6.5705], ['Surface Water', 'Borehole/Protected DW', 'Standpipe', 'Rainwater', 'Protected Spring', 'Unprotected DW', 'Piped Water'], '', 'Number of Schools', 1)

# Each parasite
mansoni = always_used[always_used['Smansoni'] != 0].copy()
hist0plot(mansoni['Q29'], 7, 'With Mansoni: Type of Water Source (In-sch always used)', 0.5, '#1CE692', 1, [1.4285, 2.2855, 3.1425, 3.9995, 4.8565, 5.7136, 6.5705], ['Surface Water', 'Borehole/Protected DW', 'Standpipe', 'Rainwater', 'Protected Spring', 'Unprotected DW', 'Piped Water'], '', 'Number of Schools', 1)

no_mansoni = always_used[always_used['Smansoni'] != 0].copy()
hist0plot(no_mansoni['Q29'], 7, 'NO Mansoni: Type of Water Source (In-sch always used)', 0.5, '#1CE692', 1, [1.4285, 2.2855, 3.1425, 3.9995, 4.8565, 5.7136, 6.5705], ['Surface Water', 'Borehole/Protected DW', 'Standpipe', 'Rainwater', 'Protected Spring', 'Unprotected DW', 'Piped Water'], '', 'Number of Schools', 1)

# Is water treated
compare(all_data_noSHA['Q32'], all_data_noSHA['Smansoni'], 'Treat Drinking Water (Dry Season)', 'S.Mansoni Intensity', 0, 1, [1, 2, 3, 4, 5, 6, 7, 8], ['No - never drank', 'No - drink untreated', 'Yes - boiling', 'Yes - chlorine/Bishangari', 'Yes - Moringa', 'Yes - ceramic/biosand', 'Yes - SODIS', 'Yes - cloth straining'])
compare(all_data_noSHA['Q33'], all_data_noSHA['Smansoni'], 'Treat Drinking Water (Dry Season)', 'S.Mansoni Intensity', 0, 1, [1, 2, 3, 4, 5, 6, 7, 8], ['No - never drank', 'No - drink untreated', 'Yes - boiling', 'Yes - chlorine/Bishangari', 'Yes - Moringa', 'Yes - ceramic/biosand', 'Yes - SODIS', 'Yes - cloth straining'])
compare(all_data_noSHA['Q34'], all_data_noSHA['Smansoni'], 'Treat Drinking Water (Dry Season)', 'S.Mansoni Intensity', 0, 0, [1, 2, 3, 4, 5, 6, 7, 8], ['No - never drank', 'No - drink untreated', 'Yes - boiling', 'Yes - chlorine/Bishangari', 'Yes - Moringa', 'Yes - ceramic/biosand', 'Yes - SODIS', 'Yes - cloth straining'])
compare(all_data_noSHA['Q35'], all_data_noSHA['Smansoni'], 'Treat Drinking Water (Dry Season)', 'S.Mansoni Intensity', 0, 0, [1, 2, 3, 4, 5, 6, 7, 8], ['No - never drank', 'No - drink untreated', 'Yes - boiling', 'Yes - chlorine/Bishangari', 'Yes - Moringa', 'Yes - ceramic/biosand', 'Yes - SODIS', 'Yes - cloth straining'])

# Open defecation
compare(all_data_noSHA['Q66'], all_data_noSHA['hookworm'], '', 'Hookworm Intensity [EPG]', 0, 1, [1, 2], ['Yes ', 'No'])
compare(all_data_noSHA['Q66'], all_data_noSHA['ascaris'], '', 'Ascaris Intensity [EPG]', 0, 1, [1, 2], ['Yes ', 'No'])
compare(all_data_noSHA['Q66'], all_data_noSHA['trichuris'], '', 'Trichuris Intensity [EPG]', 0, 1, [1, 2], ['Yes ', 'No'])
compare(all_data_noSHA['Q66'], all_data_noSHA['other_eggs'], '', 'Other STHs Intensity [EPG]', 0, 1, [1, 2], ['Yes ', 'No'])
compare(all_data_noSHA['Q66'], all_data_noSHA['Smansoni'], '', 'Smansoni Intensity [EPG]', 0, 1, [1, 2], ['Yes ', 'No'])




# Doors per toilet
cols = (
'Q65_3_1', 'Q65_3_2', 'Q65_3_3', 'Q65_3_4', 'Q65_3_5', 'Q65_3_6', 'Q65_2_1', 'Q65_2_2', 'Q65_2_3', 'Q65_2_4',
'Q65_2_5', 'Q65_2_6', 'Q65_4_1', 'Q65_4_2', 'Q65_4_3', 'Q65_4_4', 'Q65_4_5', 'Q65_4_6', 'Q65_5_1', 'Q65_5_2', 'Q65_5_3', 'Q65_5_4', 'Q65_5_5', 'Q65_5_6', 'Q65_6_1', 'Q65_6_2', 'Q65_6_3', 'Q65_6_4', 'Q65_6_5', 'Q65_6_6', 'Q65_7_1', 'Q65_7_2', 'Q65_7_3', 'Q65_7_4', 'Q65_7_5', 'Q65_7_6', 'Q65_8_1', 'Q65_8_2', 'Q65_8_3', 'Q65_8_4', 'Q65_8_5', 'Q65_8_6', 'Q65_9_1', 'Q65_9_2', 'Q65_9_3', 'Q65_9_4', 'Q65_9_5', 'Q65_9_6', 'Q65_10_1', 'Q65_10_2', 'Q65_10_3', 'Q65_10_4', 'Q65_10_5', 'Q65_10_6', 'Q65_11_1', 'Q65_11_2', 'Q65_11_3', 'Q65_11_4', 'Q65_11_5', 'Q65_11_6', 'Q65_12_1', 'Q65_12_2', 'Q65_12_3', 'Q65_12_4', 'Q65_12_5', 'Q65_12_6', 'Q65_13_1', 'Q65_13_2', 'Q65_13_3', 'Q65_13_4', 'Q65_13_5', 'Q65_13_6', 'Q65_14_1', 'Q65_14_2', 'Q65_14_3', 'Q65_14_4', 'Q65_14_5', 'Q65_14_6', 'Q65_15_1', 'Q65_15_2', 'Q65_15_3', 'Q65_15_4', 'Q65_15_5', 'Q65_15_6', 'Q65_16_1', 'Q65_16_2', 'Q65_16_3', 'Q65_16_4', 'Q65_16_5', 'Q65_16_6', 'Q65_17_1', 'Q65_17_2', 'Q65_17_3', 'Q65_17_4', 'Q65_17_5', 'Q65_17_6')
kk_wsh_merged = all_data_noSHA.copy()
for i in cols:
    kk_wsh_merged[i].fillna(0, inplace=True)

kk_wsh_merged['doors/toilet'] = (kk_wsh_merged['Q65_3_1'] + kk_wsh_merged['Q65_3_2'] + kk_wsh_merged['Q65_3_3'] +
                                 kk_wsh_merged['Q65_3_4'] + kk_wsh_merged['Q65_3_5'] + kk_wsh_merged['Q65_3_6']) / (
                                            kk_wsh_merged['Q65_2_1'] + kk_wsh_merged['Q65_2_2'] + kk_wsh_merged[
                                        'Q65_2_3'] + kk_wsh_merged['Q65_2_4'] + kk_wsh_merged['Q65_2_5'] +
                                            kk_wsh_merged['Q65_2_6'])

compare(doors_toilet['doors/toilet'], doors_toilet['hookworm'], 'Privacy doors per toilet', 'S.Mansoni Intensity', 0, 0, [1, 2, 3], ['a', 'a', 'a'])
compare(doors_toilet['doors/toilet'], doors_toilet['hookworm'], 'Privacy doors per toilet', 'Hookworm Intensity', 0, 0, [1, 2, 3], ['a', 'a', 'a'])
compare(doors_toilet['doors/toilet'], doors_toilet['Smansoni'], 'Privacy doors per toilet', 'S.Mansoni Intensity', 0, 0, [1, 2, 3], ['a', 'a', 'a'])
compare(doors_toilet['doors/toilet'], doors_toilet['ascaris'], 'Privacy doors per toilet', 'Ascaris Intensity', 0, 0, [1, 2, 3], ['a', 'a', 'a'])
compare(doors_toilet['doors/toilet'], doors_toilet['trichuris'], 'Privacy doors per toilet', 'Trichuris Intensity', 0, 0, [1, 2, 3], ['a', 'a', 'a'])

# Sharing of toilets
def toilet_num(a, b, c, d, e, f):
    all = [a, b, c, d, e, f]
    # drop_zero = list(filter((0).__ne__, all))
    num_toilets = len(all) - all.count(0)
    return num_toilets
def toilet_share(a, b, c, d, e, f):
    all = [a, b, c, d, e, f]
    drop_zero = list(filter((0).__ne__, all))
    unique_toilets = np.unique(drop_zero)
    sharing_score = len(unique_toilets) / len(drop_zero)
    return sharing_score

all_data_noSHA['Q65_1_1'] = all_data_noSHA['Q65_1_1'].fillna(0)
all_data_noSHA['Q65_1_2'] = all_data_noSHA['Q65_1_2'].fillna(0)
all_data_noSHA['Q65_1_3'] = all_data_noSHA['Q65_1_3'].fillna(0)
all_data_noSHA['Q65_1_4'] = all_data_noSHA['Q65_1_4'].fillna(0)
all_data_noSHA['Q65_1_5'] = all_data_noSHA['Q65_1_5'].fillna(0)
all_data_noSHA['Q65_1_6'] = all_data_noSHA['Q65_1_6'].fillna(0)
all_data_noSHA['num_toilets'] = all_data_noSHA.apply(lambda row: toilet_num(row['Q65_1_1'], row['Q65_1_2'], row['Q65_1_3'], row['Q65_1_4'], row['Q65_1_5'], row['Q65_1_6']), axis=1)
all_data_noSHA['sharing_score'] = all_data_noSHA.apply(lambda row: toilet_share(row['Q65_1_1'], row['Q65_1_2'], row['Q65_1_3'], row['Q65_1_4'], row['Q65_1_5'], row['Q65_1_6']), axis=1)
all_data_noSHA['sharing_composite'] = all_data_noSHA['num_toilets'] * all_data_noSHA['sharing_score']

compare(all_data_noSHA['sharing_composite'], all_data_noSHA['hookworm'], 'Composite Shared Toilet Score', 'Hookworm Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_composite'], all_data_noSHA['Smansoni'], 'Composite Shared Toilet Score', 'Smansoni Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_composite'], all_data_noSHA['ascaris'], 'Composite Shared Toilet Score', 'Ascaris Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_composite'], all_data_noSHA['trichuris'], 'Composite Shared Toilet Score', 'Trichuris Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_composite'], all_data_noSHA['other_eggs'], 'Composite Shared Toilet Score', 'Other STHs Intensity', 0, 0, [1, 2], ['a'])

compare(all_data_noSHA['num_toilets'], all_data_noSHA['hookworm'], 'Number of Toilets', 'Hookworm Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['num_toilets'], all_data_noSHA['Smansoni'], 'Number of Toilets', 'Smansoni Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['num_toilets'], all_data_noSHA['ascaris'], 'Number of Toilets', 'Ascaris Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['num_toilets'], all_data_noSHA['trichuris'], 'Number of Toilets', 'Trichuris Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['num_toilets'], all_data_noSHA['other_eggs'], 'Number of Toilets', 'Other STHs Intensity', 0, 0, [1, 2], ['a'])

compare(all_data_noSHA['sharing_score'], all_data_noSHA['hookworm'], 'Sharing Score', 'Hookworm Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_score'], all_data_noSHA['Smansoni'], 'Sharing Score', 'Smansoni Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_score'], all_data_noSHA['ascaris'], 'Sharing Score', 'Ascaris Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_score'], all_data_noSHA['trichuris'], 'Sharing Score', 'Trichuris Intensity', 0, 0, [1, 2], ['a'])
compare(all_data_noSHA['sharing_score'], all_data_noSHA['other_eggs'], 'Sharing Score', 'Other STHs Intensity', 0, 0, [1, 2], ['a'])

# Floor as a Factor
all_data_noSHA['Q65_1_1'] = all_data_noSHA['Q65_1_1'].fillna(0)
all_data_noSHA['Q65_1_2'] = all_data_noSHA['Q65_1_2'].fillna(0)
all_data_noSHA['Q65_1_3'] = all_data_noSHA['Q65_1_3'].fillna(0)
all_data_noSHA['Q65_1_4'] = all_data_noSHA['Q65_1_4'].fillna(0)
all_data_noSHA['Q65_1_5'] = all_data_noSHA['Q65_1_5'].fillna(0)
all_data_noSHA['Q65_1_6'] = all_data_noSHA['Q65_1_6'].fillna(0)
all_data_noSHA['num_toilets'] = all_data_noSHA.apply(lambda row: toilet_num(row['Q65_1_1'], row['Q65_1_2'], row['Q65_1_3'], row['Q65_1_4'], row['Q65_1_5'], row['Q65_1_6']), axis=1)
all_data_noSHA['sharing_score'] = all_data_noSHA.apply(lambda row: row['Q65_1_1'])

# Odour as a Factor
def odour_agg(a, b, c, d, e, f):
    all = [a, b, c, d, e, f]
    # drop_zero = list(filter((0).__ne__, all))
    num = len(all) - all.count(0)
    if num == 0:
        score = 0
    elif num != 0:
        score = (a + b + c + d + e + f)/num
    return score

all_data_noSHA['Q65_14_1'] = all_data_noSHA['Q65_14_1'].fillna(0)
all_data_noSHA['Q65_14_2'] = all_data_noSHA['Q65_14_2'].fillna(0)
all_data_noSHA['Q65_14_3'] = all_data_noSHA['Q65_14_3'].fillna(0)
all_data_noSHA['Q65_14_4'] = all_data_noSHA['Q65_14_4'].fillna(0)
all_data_noSHA['Q65_14_5'] = all_data_noSHA['Q65_14_5'].fillna(0)
all_data_noSHA['Q65_14_6'] = all_data_noSHA['Q65_14_6'].fillna(0)
all_data_noSHA['odour_score'] = all_data_noSHA.apply(lambda row: odour_agg(row['Q65_14_1'], row['Q65_14_2'], row['Q65_14_3'], row['Q65_14_4'], row['Q65_14_5'], row['Q65_14_6']), axis=1)


""" CREATE DUMMY COLUMNS FOR LOGISTIC REGRESSION AND DECISION TREE"""

# Create dummy columns
def dummy_column(logis_regre):
    logis_regre['Q1_source_n_y'] = 0  # Schools with no water source = 0, with source = 1
    mask = logis_regre.Q1 != 3
    col = 'Q1_source_n_y'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q1_always_used'] = 0  # School where water source always used = 1, else 0
    mask = logis_regre.Q1 == 1
    col = ['Q1_always_used']
    logis_regre.loc[mask, col] = 1

    logis_regre['Q1_rainy_used'] = 0  # School where source is used during rainy season = 1, else 0
    mask = logis_regre.Q1 == 2
    col = 'Q1_rainy_used'
    logis_regre.loc[mask, col] = 1

    logis_regre['dry_surface'] = 0  # Where dry season source is surface water, 1, else 0
    mask = logis_regre.Q2 == 1
    col = 'dry_surface'
    logis_regre.loc[mask, col] = 1

    logis_regre['dry_protectDW'] = 0  # Where dry season source is protected Dug Well, 1, else 0
    mask = logis_regre.Q2 == 2
    col = 'dry_protectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['dry_standpipe'] = 0  # Where dry season source is standpipe, 1, else 0
    mask = logis_regre.Q2 == 3
    col = 'dry_standpipe'
    logis_regre.loc[mask, col] = 1

    logis_regre['dry_rainwater'] = 0  # Where dry season source is rainwater, 1, else 0
    mask = logis_regre.Q2 == 4
    col = 'dry_rainwater'
    logis_regre.loc[mask, col] = 1

    logis_regre['dry_protectedspring'] = 0  # Where dry season source is protected spring, 1, else 0
    mask = logis_regre.Q2 == 5
    col = 'dry_protectedspring'
    logis_regre.loc[mask, col] = 1

    logis_regre['dry_unprotectDW'] = 0  # Where dry season source is unprotected dug well, 1, else 0
    mask = logis_regre.Q2 == 6
    col = 'dry_unprotectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['rainy_surface'] = 0  # Where rainy season source is surface water, 1, else 0
    mask = logis_regre.Q2 == 1
    col = 'rainy_surface'
    logis_regre.loc[mask, col] = 1

    logis_regre['rainy_protectDW'] = 0  # Where rainy season source is protected Dug Well, 1, else 0
    mask = logis_regre.Q2 == 2
    col = 'rainy_protectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['rainy_standpipe'] = 0  # Where rainy season source is standpipe, 1, else 0
    mask = logis_regre.Q2 == 3
    col = 'rainy_standpipe'
    logis_regre.loc[mask, col] = 1

    logis_regre['rainy_rainwater'] = 0  # Where rainy season source is rainwater, 1, else 0
    mask = logis_regre.Q2 == 4
    col = 'rainy_rainwater'
    logis_regre.loc[mask, col] = 1

    logis_regre['rainy_protectedspring'] = 0  # Where rainy season source is protected spring, 1, else 0
    mask = logis_regre.Q2 == 5
    col = 'rainy_protectedspring'
    logis_regre.loc[mask, col] = 1

    logis_regre['rainy_unprotectDW'] = 0  # Where rainy season source is unprotected dug well, 1, else 0
    mask = logis_regre.Q2 == 6
    col = 'rainy_unprotectDW'
    logis_regre.loc[mask, col] = 1

    # End of Q3
    # Q18 - Water Source only used during rainy
    logis_regre['Q18_dry_surface'] = 0  # Q18/19 Where dry season source is surface water, 1, else 0
    mask = logis_regre.Q18 == 1
    col = 'Q18_dry_surface'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_dry_protectDW'] = 0  # Q18/19 Where dry season source is protected Dug Well, 1, else 0
    mask = logis_regre.Q18 == 2
    col = 'Q18_dry_protectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_dry_standpipe'] = 0  # Q18/19 Where dry season source is standpipe, 1, else 0
    mask = logis_regre.Q18 == 3
    col = 'Q18_dry_standpipe'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_dry_rainwater'] = 0  # Q18/19 Where dry season source is rainwater, 1, else 0
    mask = logis_regre.Q18 == 4
    col = 'Q18_dry_rainwater'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_dry_protectedspring'] = 0  # Q18/19 Where dry season source is protected spring, 1, else 0
    mask = logis_regre.Q18 == 5
    col = 'Q18_dry_protectedspring'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_dry_unprotectDW'] = 0  # Q18/19 Where dry season source is unprotected dug well, 1, else 0
    mask = logis_regre.Q18 == 6
    col = 'Q18_dry_unprotectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_dry_piped'] = 0  # Q18/19 Where dry season source is piped water, 1, else 0
    mask = logis_regre.Q18 == 7
    col = 'Q18_dry_piped'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_rainy_surface'] = 0  # Q18/19 Where rainy season source is surface water, 1, else 0
    mask = logis_regre.Q19 == 1
    col = 'Q18_rainy_surface'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_rainy_protectDW'] = 0  # Q18/19 Where rainy season source is protected Dug Well, 1, else 0
    mask = logis_regre.Q19 == 2
    col = 'Q18_rainy_protectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_rainy_standpipe'] = 0  # Q18/19 Where rainy season source is standpipe, 1, else 0
    mask = logis_regre.Q19 == 3
    col = 'Q18_rainy_standpipe'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_rainy_rainwater'] = 0  # Q18/19 Where rainy season source is rainwater, 1, else 0
    mask = logis_regre.Q19 == 4
    col = 'Q18_rainy_rainwater'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_rainy_protectedspring'] = 0  # Q18/19 Where rainy season source is protected spring, 1, else 0
    mask = logis_regre.Q19 == 5
    col = 'Q18_rainy_protectedspring'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_rainy_unprotectDW'] = 0  # Q18/19 Where rainy season source is unprotected dug well, 1, else 0
    mask = logis_regre.Q19 == 6
    col = 'rainy_unprotectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['Q18_rainy_piped'] = 0  # Q18/19 Where rainy season source is piped water, 1, else 0
    mask = logis_regre.Q19 == 7
    col = 'Q18_dry_piped'
    logis_regre.loc[mask, col] = 1
    # End of Q18/19
    # Start of Q29
    # ALL-YEAR SOURCE
    logis_regre['all_year_surface'] = 0  # Q29 where all-year source is surface water, 1, else 0
    mask = logis_regre.Q29 == 1
    col = 'all_year_surface'
    logis_regre.loc[mask, col] = 1

    logis_regre['all_year_protectDW'] = 0  # Q29 where all-year source is protected Dug Well, 1, else 0
    mask = logis_regre.Q29 == 2
    col = 'all_year_protectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['all_year_standpipe'] = 0  # Q29 where all-year source is standpipe, 1, else 0
    mask = logis_regre.Q29 == 3
    col = 'all_year_standpipe'
    logis_regre.loc[mask, col] = 1

    logis_regre['all_year_rainwater'] = 0  # Q29 where all-year source is rainwater, 1, else 0
    mask = logis_regre.Q29 == 4
    col = 'all_year_rainwater'
    logis_regre.loc[mask, col] = 1

    logis_regre['all_year_protectedspring'] = 0  # Q29 where all-year source is protected spring, 1, else 0
    mask = logis_regre.Q29 == 5
    col = 'all_year_protectedspring'
    logis_regre.loc[mask, col] = 1

    logis_regre['all_year_unprotectDW'] = 0  # Q29 where all-year source is unprotected dug well, 1, else 0
    mask = logis_regre.Q29 == 6
    col = 'all_year_unprotectDW'
    logis_regre.loc[mask, col] = 1

    logis_regre['all_year_piped'] = 0  # Q29 where all-year source is piped water, 1, else 0
    mask = logis_regre.Q29 == 7
    col = 'Q18_dry_piped'
    logis_regre.loc[mask, col] = 1
    # End of all-year water source
    # Start of WATER TREATMENT
    # Dry season water treatment
    logis_regre['treat_dry_neverdrank'] = 0  # Q32 water is never drank = 1, else 0
    mask = logis_regre.Q32 == 1
    col = 'treat_dry_neverdrank'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_nevertreat'] = 0  # Q32 water is never treated = 1, else 0
    mask = logis_regre.Q32 == 2
    col = 'treat_dry_nevertreat'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_boiled'] = 0  # Q32 water is boiled = 1, else 0
    mask = logis_regre.Q32 == 3
    col = 'treat_dry_boiled'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_chlorine'] = 0  # Q32 water is bishangari/wuha agar/PUR/bleach/chlorine = 1, else 0
    mask = logis_regre.Q32 == 4
    col = 'treat_dry_chlorine'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_moringa'] = 0  # Q32 water is treated moringa seeds = 1, else 0
    mask = logis_regre.Q32 == 5
    col = 'treat_dry_moringa'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_biosand'] = 0  # Q32 water is biosand/ceramic/candle treated = 1, else 0
    mask = logis_regre.Q32 == 6
    col = 'treat_dry_biosand'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_sodis'] = 0  # Q32 water is SODIS treated = 1, else 0
    mask = logis_regre.Q32 == 7
    col = 'treat_dry_sodis'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_cloth'] = 0  # Q32 water is cloth treated = 1, else 0
    mask = logis_regre.Q32 == 8
    col = 'treat_dry_cloth'
    logis_regre.loc[mask, col] = 1
    # Onto rainy season
    # Rainy season water treatment
    logis_regre['treat_rainy_neverdrank'] = 0  # rain Q32 water is never drank = 1, else 0
    mask = logis_regre.Q33 == 1
    col = 'treat_rainy_neverdrank'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_rainy_nevertreat'] = 0  # rain Q32 water is never treated = 1, else 0
    mask = logis_regre.Q33 == 2
    col = 'treat_rainy_nevertreat'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_rainy_boiled'] = 0  # rain Q32 water is boiled = 1, else 0
    mask = logis_regre.Q33 == 3
    col = 'treat_rainy_boiled'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_rainy_chlorine'] = 0  # rain Q32 water is bishangari/wuha agar/PUR/bleach/chlorine = 1, else 0
    mask = logis_regre.Q33 == 4
    col = 'treat_rainy_chlorine'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_rainy_moringa'] = 0  # rain Q32 water is treated moringa seeds = 1, else 0
    mask = logis_regre.Q33 == 5
    col = 'treat_rainy_moringa'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_rainy_biosand'] = 0  # rain Q32 water is biosand/ceramic/candle treated = 1, else 0
    mask = logis_regre.Q33 == 6
    col = 'treat_rainy_biosand'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_rainy_sodis'] = 0  # rain Q32 water is SODIS treated = 1, else 0
    mask = logis_regre.Q33 == 7
    col = 'treat_rainy_sodis'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_rainy_cloth'] = 0  # rain Q32 water is cloth treated = 1, else 0
    mask = logis_regre.Q33 == 8
    col = 'treat_rainy_cloth'
    logis_regre.loc[mask, col] = 1
    # End of Rainy season water treatment
    # Onto Question 34 - NON-DRINKING WATER Q34
    # DRY SEASON
    logis_regre['treat_dry_xdrink_nevertreat'] = 0  # NON-DRINKING WATER Q34 is never treated = 1, else 0
    mask = logis_regre.Q34 == 1
    col = 'treat_dry_xdrink_nevertreat'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_xdrink_boiled'] = 0  # NON-DRINKING WATER Q34 is boiled = 1, else 0
    mask = logis_regre.Q34 == 2
    col = 'treat_dry_xdrink_boiled'
    logis_regre.loc[mask, col] = 1

    logis_regre[
        'treat_dry_xdrink_chlorine'] = 0  # NON-DRINKING WATER Q34 is bishangari/wuha agar/PUR/bleach/chlorine = 1, else 0
    mask = logis_regre.Q34 == 3
    col = 'treat_dry_xdrink_chlorine'
    logis_regre.loc[mask, col] = 1

    logis_regre['treat_dry_xdrink_moringa'] = 0  # NON-DRINKING WATER Q34 is treated moringa seeds = 1, else 0
    mask = logis_regre.Q34 == 4
    col = 'treat_dry_xdrink_moringa'
    logis_regre.loc[mask, col] = 1

    col = 'treat_dry_xdrink_biosand'  # NON-DRINKING WATER Q34 is biosand/ceramic/candle treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q34 == 5
    logis_regre.loc[mask, col] = 1

    col = 'treat_dry_xdrink_sodis'  # NON-DRINKING WATER Q34 is SODIS treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q34 == 6
    logis_regre.loc[mask, col] = 1

    col = 'treat_dry_xdrink_cloth'  # NON-DRINKING WATER Q34 is cloth treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q34 == 7
    logis_regre.loc[mask, col] = 1
    # ONTO RAINY SEASON
    col = 'treat_rainy_xdrink_not_treat'  # NON-DRINKING WATER Q35 is not treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q35 == 1
    logis_regre.loc[mask, col] = 1

    col = 'treat_rainy_xdrink_boiled'  # NON-DRINKING WATER Q35 is boiled treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q35 == 2
    logis_regre.loc[mask, col] = 1

    col = 'treat_rainy_xdrink_chlorine'  # NON-DRINKING WATER Q35 is chlorine treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q35 == 3
    logis_regre.loc[mask, col] = 1

    col = 'treat_rainy_xdrink_moringa'  # NON-DRINKING WATER Q35 is moringa treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q35 == 4
    logis_regre.loc[mask, col] = 1

    col = 'treat_rainy_xdrink_biosand'  # NON-DRINKING WATER Q35 is biosand/ceramic/candle treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q35 == 5
    logis_regre.loc[mask, col] = 1

    col = 'treat_rainy_xdrink_sodis'  # NON-DRINKING WATER Q35 is sodis treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q35 == 6
    logis_regre.loc[mask, col] = 1

    col = 'treat_rainy_xdrink_cloth'  # NON-DRINKING WATER Q35 is cloth treated = 1, else 0
    logis_regre[col] = 0
    mask = logis_regre.Q35 == 7
    logis_regre.loc[mask, col] = 1
    # End of water treatment methods
    # Does School PAY FOR SANITATION
    col = 'pays_sanitation'  # 1 if some sort of sanitation paymeny, 0 means school NEVER PAYS for any sanitation
    logis_regre[col] = 0
    mask = logis_regre.Q36 != 1
    logis_regre.loc[mask, col] = 1
    # School pay for water provision?
    col = 'pays_provision'  # 1 if there is a weekly/monthly/yearly fee, 0 if no REGULAR fee
    logis_regre[col] = 0
    mask = logis_regre.Q37 != 1
    logis_regre.loc[mask, col] = 1

    # Number of blocks
    logis_regre['block_1'] = 0
    mask = logis_regre.Q65_2_1 > 0
    logis_regre.loc[mask, 'block_1'] = 1

    logis_regre['block_2'] = 0
    mask = logis_regre.Q65_2_2 > 0
    logis_regre.loc[mask, 'block_2'] = 1

    logis_regre['block_3'] = 0
    mask = logis_regre.Q65_2_3 > 0
    logis_regre.loc[mask, 'block_3'] = 1

    logis_regre['block_4'] = 0
    mask = logis_regre.Q65_2_4 > 0
    logis_regre.loc[mask, 'block_4'] = 1

    logis_regre['block_5'] = 0
    mask = logis_regre.Q65_2_5 > 0
    logis_regre.loc[mask, 'block_5'] = 1

    logis_regre['block_6'] = 0
    mask = logis_regre.Q65_2_6 > 0
    logis_regre.loc[mask, 'block_6'] = 1

    # Number of blocks
    logis_regre['block_count'] = (
                logis_regre.Q65_2_1 + logis_regre.Q65_2_2 + logis_regre.Q65_2_3 + logis_regre.Q65_2_4 + logis_regre.Q65_2_5 + logis_regre.Q65_2_6)

    # Privacy Doors per Toilet
    cols = (
        'Q65_3_1', 'Q65_3_2', 'Q65_3_3', 'Q65_3_4', 'Q65_3_5', 'Q65_3_6', 'Q65_2_1', 'Q65_2_2', 'Q65_2_3', 'Q65_2_4',
        'Q65_2_5', 'Q65_2_6', 'Q65_4_1', 'Q65_4_2', 'Q65_4_3', 'Q65_4_4', 'Q65_4_5', 'Q65_4_6', 'Q65_5_1', 'Q65_5_2',
        'Q65_5_3', 'Q65_5_4', 'Q65_5_5', 'Q65_5_6', 'Q65_6_1', 'Q65_6_2', 'Q65_6_3', 'Q65_6_4', 'Q65_6_5', 'Q65_6_6',
        'Q65_7_1', 'Q65_7_2', 'Q65_7_3', 'Q65_7_4', 'Q65_7_5', 'Q65_7_6', 'Q65_8_1', 'Q65_8_2', 'Q65_8_3', 'Q65_8_4',
        'Q65_8_5', 'Q65_8_6', 'Q65_9_1', 'Q65_9_2', 'Q65_9_3', 'Q65_9_4', 'Q65_9_5', 'Q65_9_6', 'Q65_10_1', 'Q65_10_2',
        'Q65_10_3', 'Q65_10_4', 'Q65_10_5', 'Q65_10_6', 'Q65_11_1', 'Q65_11_2', 'Q65_11_3', 'Q65_11_4', 'Q65_11_5',
        'Q65_11_6', 'Q65_12_1', 'Q65_12_2', 'Q65_12_3', 'Q65_12_4', 'Q65_12_5', 'Q65_12_6', 'Q65_13_1', 'Q65_13_2',
        'Q65_13_3', 'Q65_13_4', 'Q65_13_5', 'Q65_13_6', 'Q65_14_1', 'Q65_14_2', 'Q65_14_3', 'Q65_14_4', 'Q65_14_5',
        'Q65_14_6', 'Q65_15_1', 'Q65_15_2', 'Q65_15_3', 'Q65_15_4', 'Q65_15_5', 'Q65_15_6', 'Q65_16_1', 'Q65_16_2',
        'Q65_16_3', 'Q65_16_4', 'Q65_16_5', 'Q65_16_6', 'Q65_17_1', 'Q65_17_2', 'Q65_17_3', 'Q65_17_4', 'Q65_17_5',
        'Q65_17_6')

    for i in cols:
        logis_regre[i].fillna(0, inplace=True)
    # toilet floor and odour
    logis_regre['odour_score'] = ((logis_regre['Q65_14_1'] + logis_regre['Q65_14_2'] + logis_regre['Q65_14_3'] +
                                   logis_regre['Q65_14_4'] + logis_regre['Q65_14_5'] + logis_regre[
                                       'Q65_14_6']) / logis_regre.block_count)
    # Structural COndition score
    logis_regre['floor_struc_score'] = ((logis_regre['Q65_6_1'] + logis_regre['Q65_6_2'] + logis_regre['Q65_6_3'] +
                                         logis_regre['Q65_6_4'] + logis_regre['Q65_6_5'] + logis_regre[
                                             'Q65_6_6']) / logis_regre.block_count)

    # Wall Privacy score
    logis_regre['wall_priv_score'] = ((logis_regre['Q65_7_1'] + logis_regre['Q65_7_2'] + logis_regre['Q65_7_3'] +
                                       logis_regre['Q65_7_4'] + logis_regre['Q65_7_5'] + logis_regre[
                                           'Q65_7_6']) / logis_regre.block_count)

    # Roof Structural COndition score
    logis_regre['roof_struc_score'] = ((logis_regre['Q65_8_1'] + logis_regre['Q65_8_2'] + logis_regre['Q65_8_3'] +
                                        logis_regre['Q65_8_4'] + logis_regre['Q65_8_5'] + logis_regre[
                                            'Q65_8_6']) / logis_regre.block_count)

    # Floor Cleanliness score
    logis_regre['floor_clean_score'] = ((logis_regre['Q65_10_1'] + logis_regre['Q65_10_2'] + logis_regre['Q65_10_3'] +
                                         logis_regre['Q65_10_4'] + logis_regre['Q65_10_5'] + logis_regre[
                                             'Q65_10_6']) / logis_regre.block_count)

    # Flies score
    logis_regre['flies_score'] = ((logis_regre['Q65_12_1'] + logis_regre['Q65_12_2'] + logis_regre['Q65_12_3'] +
                                   logis_regre['Q65_12_4'] + logis_regre['Q65_12_5'] + logis_regre[
                                       'Q65_12_6']) / logis_regre.block_count)

    # Structural COndition score
    logis_regre['floor_struc_score'] = ((logis_regre['Q65_6_1'] + logis_regre['Q65_6_2'] + logis_regre['Q65_6_3'] +
                                         logis_regre['Q65_6_4'] + logis_regre['Q65_6_5'] + logis_regre[
                                             'Q65_6_6']) / logis_regre.block_count)

    logis_regre['doors/toilet'] = ((logis_regre['Q65_3_1'] + logis_regre['Q65_3_2'] + logis_regre['Q65_3_3'] +
                                    logis_regre['Q65_3_4'] + logis_regre['Q65_3_5'] + logis_regre['Q65_3_6']) / (
                                           logis_regre['Q65_2_1'] + logis_regre['Q65_2_2'] + logis_regre[
                                       'Q65_2_3'] + logis_regre['Q65_2_4'] + logis_regre['Q65_2_5'] +
                                           logis_regre['Q65_2_6']))
    # Set ratio > 1 to median
    med = logis_regre['doors/toilet'].median()
    col = 'doors/toilet'
    mask = logis_regre['doors/toilet'] > 1
    logis_regre.loc[mask, col] = med

    Y = logis_regre[
        ['Smansoni', 'hookworm', 'ascaris', 'trichuris', 'other_eggs', 'SmansoniPrev', 'HookwormPrev', 'AscarisPrev',
         'TrichurisPrev', 'STHPrev', 'Q66']].copy()
    mask = Y.Smansoni > 0
    Y.loc[mask, 'Smansoni'] = 1
    mask = Y.hookworm > 0
    Y.loc[mask, 'hookworm'] = 1
    mask = Y.ascaris > 0
    Y.loc[mask, 'ascaris'] = 1
    mask = Y.trichuris > 0
    Y.loc[mask, 'trichuris'] = 1
    mask = Y.other_eggs > 0
    Y.loc[mask, 'other_eggs'] = 1
    X = logis_regre.drop(
        ['WoredaCode', 'SchoolCode', 'ID_1', 'Smansoni', 'hookworm', 'ascaris', 'trichuris', 'other_eggs',
         'SmansoniPrev', 'HookwormPrev', 'AscarisPrev', 'TrichurisPrev', 'STHPrev', 'ascaris_kk', 'No.', 'SubDate',
         'Long', 'Lat', 'Date', 'Team', 'Leader', 'Region', 'Zone', 'District', 'Woreda', 'Deworming', 'TwoMonths',
         'Lowest', 'Highest', 'Boys', 'Girls', 'Gr1Boys', 'Gr1Girls', 'Gr2Boys', 'Gr2Girls', 'Gr3Boys', 'Gr3Girls',
         'Gr4Boys', 'Gr4Girls', 'Gr5Boys', 'Gr5Girls', 'Gr6Boys', 'Gr6Girls', 'Gr7Boys', 'Gr7Girls', 'Gr8Boys',
         'Gr8Girls', 'Notes', 'SchoolCheck',
         'Unnamed: 0',
         'schoolid', 'WOREDA', 'SCHOOL_ID', 'ENUMERATOR_NAME', 'ENUMERATOR_ID', 'DATE_OF_SURVEY', 'Q1', 'Q2', 'Q2_O',
         'Q3', 'Q3_O', 'Q4', 'Q4_O', 'Q5', 'Q5_O', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q12_O', 'Q13', 'Q13_O',
         'Q14', 'Q15', 'Q16_1', 'Q16_2', 'Q16_3', 'Q16_4', 'Q16_5', 'Q16_6', 'Q16_7', 'Q16_8', 'Q16_O', 'Q17_1',
         'Q17_2', 'Q17_3', 'Q17_4', 'Q17_5', 'Q17_6', 'Q17_7', 'Q17_8', 'Q17_O', 'Q18', 'Q18_O', 'Q19', 'Q19_O', 'Q20',
         'Q20_O', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q25_O', 'Q26', 'Q27_1', 'Q27_2', 'Q27_3', 'Q27_4', 'Q27_5',
         'Q27_6', 'Q27_7', 'Q27_8', 'Q27_O', 'Q28_1', 'Q28_2', 'Q28_3', 'Q28_4', 'Q28_5', 'Q28_6', 'Q28_7', 'Q28_8',
         'Q28_O', 'Q29', 'Q29_O', 'Q30', 'Q31_1', 'Q31_2', 'Q31_3', 'Q31_4', 'Q31_5', 'Q31_6', 'Q31_7', 'Q31_8',
         'Q31_O', 'Q32', 'Q32_O', 'Q33', 'Q33_O', 'Q34', 'Q34_O', 'Q35', 'Q35_O', 'Q36', 'Q36_AMT', 'Q36_O', 'Q37',
         'Q37_O', 'Q38', 'Q38_O', 'Q39', 'Q39_O', 'Q40', 'Q41', 'Q42', 'Q43', 'Q44', 'Q45_1_1', 'Q45_2_1', 'Q45_3_1',
         'Q45_4_1', 'Q45_1_2', 'Q45_2_2', 'Q45_3_2', 'Q45_4_2', 'Q45_1_3', 'Q45_2_3', 'Q45_3_3', 'Q45_4_3', 'Q45_1_4',
         'Q45_2_4', 'Q45_3_4', 'Q45_4_4', 'Q45_1_5', 'Q45_2_5', 'Q45_3_5', 'Q45_4_5', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50',
         'Q51', 'Q52', 'Q53', 'Q54', 'Q55', 'Q56', 'Q57', 'Q58', 'Q59', 'Q60', 'Q61', 'Q62', 'Q63', 'Q63_O', 'Q64',
         'Q65_1_1', 'Q65_1_2', 'Q65_1_3', 'Q65_1_4', 'Q65_1_5', 'Q65_1_6', 'Q65_2_1', 'Q65_2_2', 'Q65_2_3', 'Q65_2_4',
         'Q65_2_5', 'Q65_2_6', 'Q65_3_1', 'Q65_3_2', 'Q65_3_3', 'Q65_3_4', 'Q65_3_5', 'Q65_3_6', 'Q65_4_1', 'Q65_4_2',
         'Q65_4_3', 'Q65_4_4', 'Q65_4_5', 'Q65_4_6', 'Q65_5_1', 'Q65_5_2', 'Q65_5_3', 'Q65_5_4', 'Q65_5_5', 'Q65_5_6',
         'Q65_6_1', 'Q65_6_2', 'Q65_6_3', 'Q65_6_4', 'Q65_6_5', 'Q65_6_6', 'Q65_7_1', 'Q65_7_2', 'Q65_7_3', 'Q65_7_4',
         'Q65_7_5', 'Q65_7_6', 'Q65_8_1', 'Q65_8_2', 'Q65_8_3', 'Q65_8_4', 'Q65_8_5', 'Q65_8_6', 'Q65_9_1', 'Q65_9_2',
         'Q65_9_3', 'Q65_9_4', 'Q65_9_5', 'Q65_9_6', 'Q65_10_1', 'Q65_10_2', 'Q65_10_3', 'Q65_10_4', 'Q65_10_5',
         'Q65_10_6', 'Q65_11_1', 'Q65_11_2', 'Q65_11_3', 'Q65_11_4', 'Q65_11_5', 'Q65_11_6', 'Q65_12_1', 'Q65_12_2',
         'Q65_12_3', 'Q65_12_4', 'Q65_12_5', 'Q65_12_6', 'Q65_13_1', 'Q65_13_2', 'Q65_13_3', 'Q65_13_4', 'Q65_13_5',
         'Q65_13_6', 'Q65_14_1', 'Q65_14_2', 'Q65_14_3', 'Q65_14_4', 'Q65_14_5', 'Q65_14_6', 'Q65_15_1', 'Q65_15_2',
         'Q65_15_3', 'Q65_15_4', 'Q65_15_5', 'Q65_15_6', 'Q65_16_1', 'Q65_16_2', 'Q65_16_3', 'Q65_16_4', 'Q65_16_5',
         'Q65_16_6', 'Q65_17_1', 'Q65_17_2', 'Q65_17_3', 'Q65_17_4', 'Q65_17_5', 'Q65_17_6', 'Unnamed: 253',
         "Status (1=fine, 2=smartphone and WASH match but not with schoolsformapping (basically fine), 3=WASH code correct but absent from smartphone database, 4=WASH code correct but corresponds to different school in smartphone database, 5-WASH code is wrong (schoolsformapping and smartphone agree, WASH is different), 6 - WASH code is wrong (different name in schools for mapping, absent from smartphone database), 7=WASH code is wrong (missing from schoolsformapping and smartphone databases), 8=mistakes in both databases (names don't match up between either), 9=WASH code wrong (different name in schools for mapping, absent from smartphone database), 2=needs checking, 3=no idea, 4=fine but no disease data)",
         'NOTES', 'Added on 01102014?', 'School and woreda code changed on 011014?',
         'Changed after comparison with smartphone, school ID databases 01102014',
         'Previous woreda code (before 01102014)', 'Previous school code (before 01102014)', 'School ID - WASH',
         'Proposed codes:'], axis=1)
    X['doors/toilet'] = X['doors/toilet'].fillna(0.7282005410219611)
    mean_elev = X['elevation'].mean()
    X['elevation'] = X['elevation'].fillna(mean_elev)
    return X, Y


# Run Logistic Regression
# Check na
# X.isnull().sum()
# Fill na with mean + elevation?

y = Y['Smansoni']
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn import metrics
# import seaborn as sn
# import matplotlib.pyplot as plt
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)

# Logistic Regression
model = sm.Logit(y, X)
model = model.fit()
model.summary()

# Decision tree
from sklearn import tree
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
para = 'Smansoni'
def decision_tree(para, df, split):
    logis_regre = df.copy()
    df_1 = logis_regre[logis_regre[para] == 0]
    df_2 = logis_regre[logis_regre[para] > 0]
    if len(df_1) > len(df_2):
        df_minority = df_2
        df_majority = df_1
    elif len(df_2) >= len(df_1):
        df_minority = df_1
        df_majority = df_2

    df_minority_upsampled = resample(df_minority,
                                 replace=True,     # sample with replacement
                                 n_samples=len(df_majority),    # to match majority class
                               random_state=123)

    df_upsampled = pd.concat([df_majority, df_minority_upsampled])
    print(df_upsampled[para].value_counts())
    X, Y = dummy_column(df_upsampled)
    y = Y[para]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1, random_state=42)
    clf = tree.DecisionTreeClassifier()
    print("Mean Accuracy", cross_val_score(clf, X_train, y_train, cv=5).mean())

    clf = clf.fit(X_train, y_train)
    print('Score on test dataset:',  clf.score(X_test, y_test))
    importance = clf.feature_importances_
    features = list(X.columns.values)
    features = np.asarray(features)
    importance_of_features = pd.DataFrame(data=features)
    importance_of_features['importance'] = importance
    print(importance_of_features)
    return importance_of_features

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
def random_forest(para, df, split):
    logis_regre = df.copy()
    df_1 = logis_regre[logis_regre[para] == 0]
    df_2 = logis_regre[logis_regre[para] > 0]
    if len(df_1) > len(df_2):
        df_minority = df_2
        df_majority = df_1
    elif len(df_2) >= len(df_1):
        df_minority = df_1
        df_majority = df_2

    df_minority_upsampled = resample(df_minority,
                                     replace=True,  # sample with replacement
                                     n_samples=len(df_majority),  # to match majority class
                                     random_state=123)

    df_upsampled = pd.concat([df_majority, df_minority_upsampled])
    print(df_upsampled[para].value_counts())
    X, Y = dummy_column(df_upsampled)
    y = Y[para]
    X = X[['block_count', 'floor_struc_score', 'wall_priv_score', 'roof_struc_score', 'floor_clean_score', 'flies_score', 'pays_sanitation', 'doors/toilet', 'num_toilets', 'sharing_score', 'sharing_composite', 'odour_score']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.333, random_state=42)
    clf = RandomForestClassifier(n_estimators=100)
    print("Mean Accuracy", cross_val_score(clf, X_train, y_train, cv=5).mean())

    clf = clf.fit(X_train, y_train)
    print('Score on test dataset:', clf.score(X_test, y_test))
    importance = clf.feature_importances_
    features = list(X.columns.values)
    features = np.asarray(features)
    importance_of_features = pd.DataFrame(data=features)
    importance_of_features['importance'] = importance
    print(importance_of_features)
    return importance_of_features



# Split schools by ecological factor and compare to WASH factors
elev_above = logis_regre[logis_regre['elevation'] > 1890.574941699205]
elev_below = logis_regre[logis_regre['elevation'] < 1890.574941699205]
prec_above = logis_regre[logis_regre['prec_ann'] > 96.94510858736801]
prec_below = logis_regre[logis_regre['prec_ann'] < 96.94510858736801]

# Water Source
y = elev_above['SmansoniPrev']
x = elev_above['Q1']
compare(x, y, 'School Water Source', 'S.Mansoni Prevalece', 0, 0, 0, 0)

y = elev_below['SmansoniPrev']
x = elev_below['Q1']
compare(x, y, 'School Water Source', 'S.Mansoni Prevalece', 0, 0, 0, 0)

y = prec_above['HookwormPrev']
x = prec_above['Q1']
compare(x, y, 'School Water Source', 'Hookworm Prevalence', 0, 0, 0, 0)

para = 'HookwormPrev'
y = prec_above[para]
x = prec_above['Q1']
compare(x, y, 'School Water Source', 'Hookworm ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q1']
compare(x, y, 'School Water Source', 'Hookworm Prevalence', 1, 0, 0, 0)

para = 'AscarisPrev'
y = prec_above[para]
x = prec_above['Q1']
compare(x, y, 'School Water Source', 'Ascaris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q1']
compare(x, y, 'School Water Source', 'Ascaris Prevalence', 1, 0, 0, 0)

para = 'TrichurisPrev'
y = prec_above[para]
x = prec_above['Q1']
compare(x, y, 'School Water Source', 'Trichuris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q1']
compare(x, y, 'School Water Source', 'Trichuris Prevalence', 1, 0, 0, 0)

# Type of Brought water source
# Q2
always_brought = logis_regre[logis_regre['Q1'] == 3]
always_brought['Q2'] = always_brought['Q2'].replace([1], 10)
always_brought['Q2'] = always_brought['Q2'].replace([2], 20)
always_brought['Q2'] = always_brought['Q2'].replace([3], 30)
always_brought['Q2'] = always_brought['Q2'].replace([4], 40)
always_brought['Q2'] = always_brought['Q2'].replace([5], 50)
always_brought['Q2'] = always_brought['Q2'].replace([6], 60)
always_brought['Q2'] = always_brought['Q2'].replace([7], 70)

always_brought['Q2'] = always_brought['Q2'].replace([10], 6)
always_brought['Q2'] = always_brought['Q2'].replace([20], 1)
always_brought['Q2'] = always_brought['Q2'].replace([30], 2)
always_brought['Q2'] = always_brought['Q2'].replace([40], 4)
always_brought['Q2'] = always_brought['Q2'].replace([50], 3)
always_brought['Q2'] = always_brought['Q2'].replace([60], 5)
always_brought['Q2'] = always_brought['Q2'].replace([70], 7)

prec_above = always_brought[always_brought['prec_ann'] > 96.94510858736801]
prec_below = always_brought[always_brought['prec_ann'] < 96.94510858736801]
para = 'TrichurisPrev'  # all
y = prec_above[para]
x = prec_above['Q2']
compare(x, y, 'School Water Source', 'Trichuris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q2']
compare(x, y, 'School Water Source', 'Trichuris Prevalence', 1, 0, 0, 0)

para = 'SmansoniPrev'  # all
y = prec_above[para]
x = prec_above['Q2']
compare(x, y, 'School Water Source', 'S.Mansoni ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q2']
compare(x, y, 'School Water Source', 'S.Mansoni Prevalence', 1, 0, 0, 0)

para = 'HookwormPrev'  # all
y = prec_above[para]
x = prec_above['Q2']
compare(x, y, 'School Water Source', 'Hookworm ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q2']
compare(x, y, 'School Water Source', 'Hookworm Prevalence', 1, 0, 0, 0)

para = 'AscarisPrev'  # all
y = prec_above[para]
x = prec_above['Q2']
compare(x, y, 'School Water Source', 'Ascaris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q2']
compare(x, y, 'School Water Source', 'Ascaris Prevalence', 1, 0, 0, 0)

para = 'STHPrev'  # all
y = prec_above[para]
x = prec_above['Q2']
compare(x, y, 'School Water Source', 'Other STHs ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below['Q2']
compare(x, y, 'School Water Source', 'Other STHs Prevalence', 1, 0, 0, 0)

# Q3
Q = 'Q3'
always_brought = logis_regre[logis_regre['Q1'] == 3]
always_brought[Q] = always_brought[Q].replace([1], 10)
always_brought[Q] = always_brought[Q].replace([2], 20)
always_brought[Q] = always_brought[Q].replace([3], 30)
always_brought[Q] = always_brought[Q].replace([4], 40)
always_brought[Q] = always_brought[Q].replace([5], 50)
always_brought[Q] = always_brought[Q].replace([6], 60)
always_brought[Q] = always_brought[Q].replace([7], 70)
# Rank by weighting and literature
always_brought[Q] = always_brought[Q].replace([10], 6)
always_brought[Q] = always_brought[Q].replace([20], 1)
always_brought[Q] = always_brought[Q].replace([30], 2)
always_brought[Q] = always_brought[Q].replace([40], 4)
always_brought[Q] = always_brought[Q].replace([50], 3)
always_brought[Q] = always_brought[Q].replace([60], 5)
always_brought[Q] = always_brought[Q].replace([70], 7)

prec_above = always_brought[always_brought['prec_ann'] > 96.94510858736801]
prec_below = always_brought[always_brought['prec_ann'] < 96.94510858736801]
para = 'TrichurisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Trichuris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Trichuris Prevalence', 1, 0, 0, 0)

para = 'SmansoniPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'S.Mansoni ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'S.Mansoni Prevalence', 1, 0, 0, 0)

para = 'HookwormPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Hookworm ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Hookworm Prevalence', 1, 0, 0, 0)

para = 'AscarisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Ascaris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Ascaris Prevalence', 1, 0, 0, 0)

para = 'STHPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Other STHs ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Other STHs Prevalence', 1, 0, 0, 0)

# Type of School Water Source
# Q29
Q = 'Q29'
always_brought = logis_regre[logis_regre['Q1'] == 1]
always_brought[Q] = always_brought[Q].replace([1], 10)
always_brought[Q] = always_brought[Q].replace([2], 20)
always_brought[Q] = always_brought[Q].replace([3], 30)
always_brought[Q] = always_brought[Q].replace([4], 40)
always_brought[Q] = always_brought[Q].replace([5], 50)
always_brought[Q] = always_brought[Q].replace([6], 60)
always_brought[Q] = always_brought[Q].replace([7], 70)
always_brought[Q] = always_brought[Q].replace([8], 80)
# Rank by weighting and literature
always_brought[Q] = always_brought[Q].replace([10], 7)
always_brought[Q] = always_brought[Q].replace([20], 2)
always_brought[Q] = always_brought[Q].replace([30], 3)
always_brought[Q] = always_brought[Q].replace([40], 5)
always_brought[Q] = always_brought[Q].replace([50], 4)
always_brought[Q] = always_brought[Q].replace([60], 6)
always_brought[Q] = always_brought[Q].replace([70], 1)
always_brought[Q] = always_brought[Q].replace([80], 8)

prec_above = always_brought[always_brought['prec_ann'] > 96.94510858736801]
prec_below = always_brought[always_brought['prec_ann'] < 96.94510858736801]
para = 'TrichurisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Trichuris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Trichuris Prevalence', 1, 0, 0, 0)

para = 'SmansoniPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'S.Mansoni ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'S.Mansoni Prevalence', 1, 0, 0, 0)

para = 'HookwormPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Hookworm ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Hookworm Prevalence', 1, 0, 0, 0)

para = 'AscarisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Ascaris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Ascaris Prevalence', 1, 0, 0, 0)

para = 'STHPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'School Water Source', 'Other STHs ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'School Water Source', 'Other STHs Prevalence', 1, 0, 0, 0)
# End
# Drinking Water Treatment - Dry
# Q32                                                                                                   # Q32
Q = 'Q32'
always_brought = logis_regre.copy()
always_brought = always_brought.dropna(subset=[Q])
always_brought[Q] = always_brought[Q].replace([1], 10)
always_brought[Q] = always_brought[Q].replace([2], 20)
always_brought[Q] = always_brought[Q].replace([3], 30)
always_brought[Q] = always_brought[Q].replace([4], 40)
always_brought[Q] = always_brought[Q].replace([5], 50)
always_brought[Q] = always_brought[Q].replace([6], 60)
always_brought[Q] = always_brought[Q].replace([7], 70)
always_brought[Q] = always_brought[Q].replace([8], 80)
always_brought[Q] = always_brought[Q].replace([9], 90)
# Rank by weighting and literature
always_brought[Q] = always_brought[Q].replace([10], 2)
always_brought[Q] = always_brought[Q].replace([20], 8)
always_brought[Q] = always_brought[Q].replace([30], 1)
always_brought[Q] = always_brought[Q].replace([40], 3)
always_brought[Q] = always_brought[Q].replace([50], 4)
always_brought[Q] = always_brought[Q].replace([60], 5)
always_brought[Q] = always_brought[Q].replace([70], 6)
always_brought[Q] = always_brought[Q].replace([80], 7)
always_brought[Q] = always_brought[Q].replace([90], 9)

prec_above = always_brought[always_brought['prec_ann'] > 96.94510858736801]
prec_below = always_brought[always_brought['prec_ann'] < 96.94510858736801]
para = 'TrichurisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Trichuris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Trichuris Prevalence', 1, 0, 0, 0)

para = 'SmansoniPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'S.Mansoni ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'S.Mansoni Prevalence', 1, 0, 0, 0)

para = 'HookwormPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Hookworm ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Hookworm Prevalence', 1, 0, 0, 0)

para = 'AscarisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Ascaris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Ascaris Prevalence', 1, 0, 0, 0)

para = 'STHPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Other STHs ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Drinking Water Treatment - Dry', 'Other STHs Prevalence', 1, 0, 0, 0)
# REPEATED FOR RAINY SEASON Q = Q33

# Odour
Q = 'odour_score'
always_brought = all_data_noSHA.copy()
always_brought = always_brought.dropna(subset=[Q])
always_brought = always_brought[always_brought[Q] != 0]
always_brought[Q] = always_brought[Q].replace([1], 10)
always_brought[Q] = always_brought[Q].replace([2], 20)
always_brought[Q] = always_brought[Q].replace([3], 30)
always_brought[Q] = always_brought[Q].replace([4], 40)
always_brought[Q] = always_brought[Q].replace([5], 50)
always_brought[Q] = always_brought[Q].replace([6], 60)
always_brought[Q] = always_brought[Q].replace([7], 70)
always_brought[Q] = always_brought[Q].replace([8], 80)
always_brought[Q] = always_brought[Q].replace([9], 90)
# Rank by weighting and literature
always_brought[Q] = always_brought[Q].replace([10], 2)
always_brought[Q] = always_brought[Q].replace([20], 8)
always_brought[Q] = always_brought[Q].replace([30], 1)
always_brought[Q] = always_brought[Q].replace([40], 3)
always_brought[Q] = always_brought[Q].replace([50], 4)
always_brought[Q] = always_brought[Q].replace([60], 5)
always_brought[Q] = always_brought[Q].replace([70], 6)
always_brought[Q] = always_brought[Q].replace([80], 7)
always_brought[Q] = always_brought[Q].replace([90], 9)

prec_above = always_brought[always_brought['prec_ann'] > 96.94510858736801]
prec_below = always_brought[always_brought['prec_ann'] < 96.94510858736801]
para = 'TrichurisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Toilet Odour Score', 'Trichuris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Toilet Odour Score', 'Trichuris Prevalence', 1, 0, 0, 0)

para = 'SmansoniPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Toilet Odour Score', 'S.Mansoni ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Toilet Odour Score', 'S.Mansoni Prevalence', 1, 0, 0, 0)

para = 'HookwormPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Toilet Odour Score', 'Hookworm ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Toilet Odour Score', 'Hookworm Prevalence', 1, 0, 0, 0)

para = 'AscarisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Toilet Odour Score', 'Ascaris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Toilet Odour Score', 'Ascaris Prevalence', 1, 0, 0, 0)

para = 'STHPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, 'Toilet Odour Score', 'Other STHs ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, 'Toilet Odour Score', 'Other STHs Prevalence', 1, 0, 0, 0)

# Latrine Privacy
cols = (
'Q65_3_1', 'Q65_3_2', 'Q65_3_3', 'Q65_3_4', 'Q65_3_5', 'Q65_3_6', 'Q65_2_1', 'Q65_2_2', 'Q65_2_3', 'Q65_2_4',
'Q65_2_5', 'Q65_2_6', 'Q65_4_1', 'Q65_4_2', 'Q65_4_3', 'Q65_4_4', 'Q65_4_5', 'Q65_4_6', 'Q65_5_1', 'Q65_5_2', 'Q65_5_3', 'Q65_5_4', 'Q65_5_5', 'Q65_5_6', 'Q65_6_1', 'Q65_6_2', 'Q65_6_3', 'Q65_6_4', 'Q65_6_5', 'Q65_6_6', 'Q65_7_1', 'Q65_7_2', 'Q65_7_3', 'Q65_7_4', 'Q65_7_5', 'Q65_7_6', 'Q65_8_1', 'Q65_8_2', 'Q65_8_3', 'Q65_8_4', 'Q65_8_5', 'Q65_8_6', 'Q65_9_1', 'Q65_9_2', 'Q65_9_3', 'Q65_9_4', 'Q65_9_5', 'Q65_9_6', 'Q65_10_1', 'Q65_10_2', 'Q65_10_3', 'Q65_10_4', 'Q65_10_5', 'Q65_10_6', 'Q65_11_1', 'Q65_11_2', 'Q65_11_3', 'Q65_11_4', 'Q65_11_5', 'Q65_11_6', 'Q65_12_1', 'Q65_12_2', 'Q65_12_3', 'Q65_12_4', 'Q65_12_5', 'Q65_12_6', 'Q65_13_1', 'Q65_13_2', 'Q65_13_3', 'Q65_13_4', 'Q65_13_5', 'Q65_13_6', 'Q65_14_1', 'Q65_14_2', 'Q65_14_3', 'Q65_14_4', 'Q65_14_5', 'Q65_14_6', 'Q65_15_1', 'Q65_15_2', 'Q65_15_3', 'Q65_15_4', 'Q65_15_5', 'Q65_15_6', 'Q65_16_1', 'Q65_16_2', 'Q65_16_3', 'Q65_16_4', 'Q65_16_5', 'Q65_16_6', 'Q65_17_1', 'Q65_17_2', 'Q65_17_3', 'Q65_17_4', 'Q65_17_5', 'Q65_17_6')
kk_wsh_merged = all_data_noSHA.copy()
for i in cols:
    kk_wsh_merged[i].fillna(0, inplace=True)

kk_wsh_merged['doors/toilet'] = (kk_wsh_merged['Q65_3_1'] + kk_wsh_merged['Q65_3_2'] + kk_wsh_merged['Q65_3_3'] +
                                 kk_wsh_merged['Q65_3_4'] + kk_wsh_merged['Q65_3_5'] + kk_wsh_merged['Q65_3_6']) / (
                                            kk_wsh_merged['Q65_2_1'] + kk_wsh_merged['Q65_2_2'] + kk_wsh_merged[
                                        'Q65_2_3'] + kk_wsh_merged['Q65_2_4'] + kk_wsh_merged['Q65_2_5'] +
                                            kk_wsh_merged['Q65_2_6'])

Q = 'doors/toilet'
always_brought = kk_wsh_merged[kk_wsh_merged['doors/toilet'] <= 1]

prec_above = always_brought[always_brought['prec_ann'] > 96.94510858736801]
prec_below = always_brought[always_brought['prec_ann'] < 96.94510858736801]
para = 'TrichurisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
x_name = 'Doors per Toilet'
compare(x, y, x_name, 'Trichuris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, x_name, 'Trichuris Prevalence', 1, 0, 0, 0)

para = 'SmansoniPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, x_name, 'S.Mansoni ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, x_name, 'S.Mansoni Prevalence', 1, 0, 0, 0)

para = 'HookwormPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, x_name, 'Hookworm ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, x_name, 'Hookworm Prevalence', 1, 0, 0, 0)

para = 'AscarisPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, x_name, 'Ascaris ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, x_name, 'Ascaris Prevalence', 1, 0, 0, 0)

para = 'STHPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, x_name, 'Other STHs ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, x_name, 'Other STHs Prevalence', 1, 0, 0, 0)
# 0-prev test
always_brought = kk_wsh_merged[kk_wsh_merged['doors/toilet'] <= 1]
always_brought = always_brought[always_brought['HookwormPrev'] > 0]
prec_above = always_brought[always_brought['prec_ann'] > 96.94510858736801]
prec_below = always_brought[always_brought['prec_ann'] < 96.94510858736801]

para = 'HookwormPrev'  # all
y = prec_above[para]
x = prec_above[Q]
compare(x, y, x_name, 'Hookworm non-0 ABOVE', 1, 0, 0, 0)
y = prec_below[para]
x = prec_below[Q]
compare(x, y, x_name, 'Hookworm non-0 Prevalence', 1, 0, 0, 0)

#


