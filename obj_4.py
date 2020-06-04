# Study of 0% prevalence schools

no_mansoni = all_data_noSHA[all_data_noSHA['Smansoni'] == 0]
has_mansoni = all_data_noSHA[all_data_noSHA['Smansoni'] != 0]
distribution_comparison(no_mansoni['temp_ann'], has_mansoni['temp_ann'], no_mansoni['prec_ann'], has_mansoni['prec_ann'], 'S.Mansoni')

no_hookworm = all_data_noSHA[all_data_noSHA['hookworm'] == 0]
has_hookworm = all_data_noSHA[all_data_noSHA['hookworm'] != 0]
distribution_comparison(no_hookworm['temp_ann'], has_hookworm['temp_ann'], no_hookworm['prec_ann'], has_hookworm['prec_ann'], 'Hookworms')

no_ascaris = all_data_noSHA[all_data_noSHA['ascaris'] == 0]
has_ascaris = all_data_noSHA[all_data_noSHA['ascaris'] != 0]
distribution_comparison(no_ascaris['temp_ann'], has_ascaris['temp_ann'], no_ascaris['prec_ann'], has_ascaris['prec_ann'], 'Ascaris')

no_trichuris = all_data_noSHA[all_data_noSHA['trichuris'] == 0]
has_trichuris = all_data_noSHA[all_data_noSHA['trichuris'] != 0]
distribution_comparison(no_trichuris['temp_ann'], has_trichuris['temp_ann'], no_trichuris['prec_ann'], has_trichuris['prec_ann'], 'Trichuris')

no_other = all_data_noSHA[all_data_noSHA['other_eggs'] == 0]
has_other = all_data_noSHA[all_data_noSHA['other_eggs'] != 0]
distribution_comparison(no_other['temp_ann'], has_other['temp_ann'], no_other['prec_ann'], has_other['prec_ann'], 'Other STHs')



