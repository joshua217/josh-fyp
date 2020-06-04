# ALL WASH FACTORS CORRELATIONS?

# Similarity Score -
cols = ['Q65_4_1', 'Q65_4_2', 'Q65_4_3', 'Q65_4_4', 'Q65_4_5', 'Q65_4_6']

for col in cols:
    wsh[col] = wsh[col].fillna(0)
    wsh[col] = wsh[col].replace([3, 5, 7], 5)
    wsh[col] = wsh[col].replace([2, 6, 8], 2)
    wsh[col] = wsh[col].replace([1, 4], 1)

def homo_latrine(a, b, c, d, e, f):
    all = [a, b, c, d, e, f]
    drop_zero = np.trim_zeros(all, 'b')
    unique_toilets = np.unique(drop_zero)
    homo_score = 1
    if len(unique_toilets) > 1:
        homo_score = 1/len(unique_toilets)

    return homo_score

wsh['homo_latrine'] = wsh.apply(lambda row: homo_latrine(row['Q65_4_1'], row['Q65_4_2'], row['Q65_4_3'], row['Q65_4_4'], row['Q65_4_5'], row['Q65_4_6']), axis=1)

cols = ['Q65_6_1', 'Q65_6_2', 'Q65_6_3', 'Q65_6_4', 'Q65_6_5', 'Q65_6_6']
wsh['homo_floors'] = wsh.apply(lambda row: homo_latrine(row['Q65_6_1'], row['Q65_6_2'], row['Q65_6_3'], row['Q65_6_4'], row['Q65_6_5'], row['Q65_6_6']), axis=1)

cols = ['Q65_7_1', 'Q65_7_2', 'Q65_7_3', 'Q65_7_4', 'Q65_7_5', 'Q65_7_6']
wsh['homo_walls'] = wsh.apply(lambda row: homo_latrine(row['Q65_6_1'], row['Q65_6_2'], row['Q65_6_3'], row['Q65_6_4'], row['Q65_6_5'], row['Q65_6_6']), axis=1)

# Homogeneity of Roofs
cols = ['Q65_8_1', 'Q65_8_2', 'Q65_8_3', 'Q65_8_4', 'Q65_8_5', 'Q65_8_6']
wsh['homo_roof'] = wsh.apply(lambda row: homo_latrine(row['Q65_6_1'], row['Q65_6_2'], row['Q65_6_3'], row['Q65_6_4'], row['Q65_6_5'], row['Q65_6_6']), axis=1)

# Predict Open defecation based on WASH factors.
Y.Q66 = Y.Q66 - 1


# Rainy Dry SPlit
all_data_noSHA['source_change_dry_rain'] = all_data_noSHA['Q2'] - all_data_noSHA['Q3']
compare = all_data_noSHA[['Q1',  'Q2', 'Q3', 'source_change_dry_rain']]
no_change = compare[compare.source_change_dry_rain == 0]
one = all_data_noSHA[all_data_noSHA.Q1 == 3]
change = compare[compare.source_change_dry_rain != 0]
change = change[change.Q1 == 3]


site_rainwater = all_data_noSHA[all_data_noSHA.Q29 == 4]
# Could plot PRECIPITATION FOR ABOVE ^^^

# Schools with no change removed
# Change to adequacy scores



