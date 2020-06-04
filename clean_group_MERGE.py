import pandas as pd
import numpy as np



def clean_group_MERGE(sch, kk, wsh, sha, elev):

    # read all in
    # kk and sha
    # Removing Schools with data from <25 students (sample size too small)
    kk['Count'] = 1
    kk_grouped_count = (
        kk.groupby(by=["WoredaCode", "SchoolCode"]).sum().reset_index(drop=False)
    )
    sample_big = kk_grouped_count[kk_grouped_count['Count'] >= 25][['WoredaCode', 'SchoolCode']]
    sample_small = kk_grouped_count[kk_grouped_count['Count'] < 25][['WoredaCode', 'SchoolCode']]
    kk_small = kk.merge(sample_small, how='inner', left_on=['WoredaCode', 'SchoolCode'], right_on=['WoredaCode', 'SchoolCode'])
    kk_big = kk.merge(sample_big, how='inner', left_on=['WoredaCode', 'SchoolCode'], right_on=['WoredaCode', 'SchoolCode']) # This is kk with the <25 students sample size schools removed
    kk = kk_big

    # Merge with sha for sha data, and drop the reallyy unnecessary columns
    kk_sha_merged = kk.merge(sha, how='inner', left_on=['ID_1'], right_on=['ID_1'], suffixes=('_kk', '_sha'),
                             indicator=False, validate=None)
    # Drop
    parasites = kk_sha_merged.drop(
        columns=['URI_kk', 'SUBMISSION_DATE_kk', 'other_kk', 'ID_2_kk', 'Region_kk', 'Zone', 'Woreda_kk', 'KK_Urine_kk',
                 'WoredaSchoolCode', 'Microscopist_kk', 'slide_kk', 'Count', 'URI_sha', 'SUBMISSION_DATE_sha',
                 'ID_2_sha', 'KK_Urine_sha', 'Microscopist_sha', 'slide_sha', 'S.mansoni', 'hookworm_sha',
                 'ascaris_sha', 'trichuris_sha', 'other_sha', 'other_eggs_sha', 'urine_date', 'PrimaryFirst',
                 'SLIDE_NO', 'Woreda_sha', 'Region_sha'])
    # Data types for groupby
    parasites['SchoolCode'] = parasites['SchoolCode'].astype(float)
    parasites['Smansoni'] = parasites['Smansoni'][parasites['Smansoni'] != ' '].fillna(0).astype(int)
    parasites['Smansoni'] = parasites['Smansoni'].astype(float)
    parasites['hookworm_kk'] = parasites['hookworm_kk'][parasites['hookworm_kk'] != ' '].fillna(0).astype(int)
    parasites['hookworm_kk'] = parasites['hookworm_kk'].astype(float)
    parasites['ascaris_kk'] = parasites['ascaris_kk'][parasites['ascaris_kk'] != ' '].fillna(0).astype(int)
    parasites['ascaris_kk'] = parasites['ascaris_kk'].astype(float)
    parasites['trichuris_kk'] = parasites['trichuris_kk'][parasites['trichuris_kk'] != ' '].fillna(0).astype(int)
    parasites['trichuris_kk'] = parasites['trichuris_kk'].astype(float)
    parasites['other_eggs_kk'] = parasites['other_eggs_kk'][parasites['other_eggs_kk'] != ' '].fillna(0).astype(int)
    parasites['other_eggs_kk'] = parasites['other_eggs_kk'].astype(float)

    # Groupby
    parasites_grouped = (parasites.groupby(by=['WoredaCode', 'SchoolCode']).mean().reset_index(drop=False))

    # Sch
    # Drop NaN on sch['Lat', 'Long']

    elev['SchoolCode'] = elev['SchoolCode'].astype(float)
    sch_elev_merged = pd.merge(sch, elev, how='inner', left_on=["Woreda", "SchoolCode"],
                               right_on=['Woreda', 'SchoolCode'], indicator=False, validate=None)
    sch_elev_merged = sch_elev_merged.rename(columns={'Lat_x': 'Lat', 'Long_x': 'Long'})
    sch_elev_merged = sch_elev_merged.drop(columns=['Lat_y', 'Long_y'])
    sch = sch_elev_merged.copy()

    # No duplicate schools found - sch.duplicated.value_counts()

    # Merge schools and parasite data
    sch_parasites = parasites_grouped.merge(sch, how='inner', left_on=['WoredaCode', 'SchoolCode'], right_on=['Woreda', 'SchoolCode'],
                            suffixes=('_parasites', '_sch'),
                            indicator=False, validate=None)
    sch_parasites['other_eggs_kk'] = sch_parasites['other_eggs_kk'].fillna(0)

    # merge with WASH data - look into why so many schools are lost here...
    all_data = sch_parasites.merge(wsh, how='inner', left_on=['WoredaCode', 'SchoolCode'],
                                   right_on=['WOREDA', 'SCHOOL_ID'],
                                   suffixes=('_paraSch', '_wsh'),
                                   indicator=False, validate=None)

    """ALL THE ABOVE BUT WITHOUT S.Haematobium Data"""
    # Without S.haem
    # Drop
    parasites_noSHA = kk.drop(
        columns=['URI', 'SUBMISSION_DATE', 'ID_2', 'Region', 'Zone', 'Woreda', 'KK_Urine', 'WoredaSchoolCode', 'Microscopist', 'slide', 'Count', 'other', 'WoredaCodeNum'])

    # Data types for groupby
    parasites_noSHA['SchoolCode'] = parasites_noSHA['SchoolCode'].astype(float)
    parasites_noSHA['Smansoni'] = parasites_noSHA['Smansoni'][parasites_noSHA['Smansoni'] != ' '].fillna(0).astype(int)
    parasites_noSHA['Smansoni'] = parasites_noSHA['Smansoni'].astype(float)
    parasites_noSHA['hookworm'] = parasites_noSHA['hookworm'][parasites_noSHA['hookworm'] != ' '].fillna(0).astype(int)
    parasites_noSHA['hookworm'] = parasites_noSHA['hookworm'].astype(float)
    parasites_noSHA['ascaris'] = parasites_noSHA['ascaris'][parasites_noSHA['ascaris'] != ' '].fillna(0).astype(int)
    parasites_noSHA['ascaris_kk'] = parasites_noSHA['ascaris'].astype(float)
    parasites_noSHA['trichuris'] = parasites_noSHA['trichuris'][parasites_noSHA['trichuris'] != ' '].fillna(0).astype(int)
    parasites_noSHA['trichuris'] = parasites_noSHA['trichuris'].astype(float)
    parasites_noSHA['other_eggs'] = parasites_noSHA['other_eggs'][parasites_noSHA['other_eggs'] != ' '].fillna(0).astype(int)
    parasites_noSHA['other_eggs'] = parasites_noSHA['other_eggs'].astype(float)

    # Groupby
    parasites_grouped_noSHA = (parasites_noSHA.groupby(by=['WoredaCode', 'SchoolCode']).mean().reset_index(drop=False))

    # Sch
    # Drop NaN on sch['Lat', 'Long']
    sch = sch.dropna(subset=['Lat', 'Long'])
    # No duplicate schools found - sch.duplicated.value_counts()

    # Merge schools and parasite data
    sch_parasites_noSHA = parasites_grouped_noSHA.merge(sch, how='inner', left_on=['WoredaCode', 'SchoolCode'],
                                            right_on=['Woreda', 'SchoolCode'],
                                            suffixes=('_parasites', '_sch'),
                                            indicator=False, validate=None)
    sch_parasites_noSHA['other_eggs'] = sch_parasites_noSHA['other_eggs'].fillna(0)

    # merge with WASH data
    all_data_noSHA = sch_parasites_noSHA.merge(wsh, how='inner', left_on=['WoredaCode', 'SchoolCode'],
                                   right_on=['WOREDA', 'SCHOOL_ID'],
                                   suffixes=('_paraSch', '_wsh'),
                                   indicator=False, validate=None)

    # New Columns
    # Latrine Privacy
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
    kk_wsh_merged = all_data_noSHA.copy()
    for i in cols:
        kk_wsh_merged[i].fillna(0, inplace=True)

    kk_wsh_merged['doors/toilet'] = (kk_wsh_merged['Q65_3_1'] + kk_wsh_merged['Q65_3_2'] + kk_wsh_merged['Q65_3_3'] +
                                     kk_wsh_merged['Q65_3_4'] + kk_wsh_merged['Q65_3_5'] + kk_wsh_merged['Q65_3_6']) / (
                                            kk_wsh_merged['Q65_2_1'] + kk_wsh_merged['Q65_2_2'] + kk_wsh_merged[
                                        'Q65_2_3'] + kk_wsh_merged['Q65_2_4'] + kk_wsh_merged['Q65_2_5'] +
                                            kk_wsh_merged['Q65_2_6'])
    all_data_noSHA['doors/toilet'] = kk_wsh_merged['doors/toilet']

    # Sharing of Toilets
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
    all_data_noSHA['num_toilets'] = all_data_noSHA.apply(
        lambda row: toilet_num(row['Q65_1_1'], row['Q65_1_2'], row['Q65_1_3'], row['Q65_1_4'], row['Q65_1_5'],
                               row['Q65_1_6']), axis=1)
    all_data_noSHA['sharing_score'] = all_data_noSHA.apply(
        lambda row: toilet_share(row['Q65_1_1'], row['Q65_1_2'], row['Q65_1_3'], row['Q65_1_4'], row['Q65_1_5'],
                                 row['Q65_1_6']), axis=1)
    all_data_noSHA['sharing_composite'] = all_data_noSHA['num_toilets'] * all_data_noSHA['sharing_score']

    def odour_agg(a, b, c, d, e, f):
        all = [a, b, c, d, e, f]
        # drop_zero = list(filter((0).__ne__, all))
        num = len(all) - all.count(0)
        if num == 0:
            score = 0
        elif num != 0:
            score = (a + b + c + d + e + f) / num
        return score

    all_data_noSHA['Q65_14_1'] = all_data_noSHA['Q65_14_1'].fillna(0)
    all_data_noSHA['Q65_14_2'] = all_data_noSHA['Q65_14_2'].fillna(0)
    all_data_noSHA['Q65_14_3'] = all_data_noSHA['Q65_14_3'].fillna(0)
    all_data_noSHA['Q65_14_4'] = all_data_noSHA['Q65_14_4'].fillna(0)
    all_data_noSHA['Q65_14_5'] = all_data_noSHA['Q65_14_5'].fillna(0)
    all_data_noSHA['Q65_14_6'] = all_data_noSHA['Q65_14_6'].fillna(0)
    all_data_noSHA['odour_score'] = all_data_noSHA.apply(
        lambda row: odour_agg(row['Q65_14_1'], row['Q65_14_2'], row['Q65_14_3'], row['Q65_14_4'], row['Q65_14_5'],
                              row['Q65_14_6']), axis=1)

    return all_data_noSHA, all_data

# Old Stuff - delete after push

# # # Merge KK and SHA for full disease data
# # kk_sha_merged = pd.merge(kk, sha, how="inner", left_on="ID_1", right_on="ID_1", suffixes=('_kk', '_sha'),
# #                          indicator=False, validate=None)
# # kk_sha_merged[['SchoolCode']] = kk_sha_merged[['SchoolCode']].astype(int)
# #
# # # Drop NaN on sch['Lat', 'Long']
# # sch = sch.dropna(subset=['Lat', 'Long'])
# #
# # # Merge sch and WASH data
# # sch_wsh_merged = pd.merge(sch, wsh, how="left", left_on=["Woreda", "SchoolCode"], right_on=["WOREDA", "SCHOOL_ID"],
# #     suffixes=("_sch", "_wsh"), indicator=False, validate=None,)
# #
# # disease_grouped = (
# #     kk_sha_merged.groupby(by=["WoredaCode", "SchoolCode"]).mean().reset_index(drop=False)
# # )
# # disease_grouped[['SchoolCode']] = disease_grouped[['SchoolCode']].astype(int)
# # data = pd.merge(disease_grouped, sch_wsh_merged, how="inner", left_on=["WoredaCode", "SchoolCode"], right_on=["Woreda", "SchoolCode"], suffixes=("_disease", "_WASH"), indicator=False, validate=None)
#
# # kk data types
# kk['Smansoni'] = kk['Smansoni'][kk['Smansoni'] != ' '].fillna(0).astype(int)
# kk['hookworm'] = kk['hookworm'][kk['hookworm'] != ' '].fillna(0).astype(int)
# kk['ascaris'] = kk['ascaris'][kk['ascaris'] != ' '].fillna(0).astype(int)
# kk['trichuris'] = kk['trichuris'][kk['trichuris'] != ' '].fillna(0).astype(int)
# kk['other_eggs'] = kk['other_eggs'][kk['other_eggs'] != ' '].fillna(0).astype(int)
#
# # kk_grouped, sch_grouped = aggregate_parasites(kk, sch)
# kk_grouped = (
#     kk.groupby(by=["WoredaCode", "SchoolCode"]).mean().reset_index(drop=False)
# )
# sch_grouped = (sch.groupby(by=['Woreda', 'SchoolCode']).mean().reset_index(drop=False))
#
# kk_grouped[['SchoolCode']] = kk_grouped[['SchoolCode']].astype(int)
# sha['s.haematobium'] = sha['s.haematobium'].fillna(0)
#
# kk_sha_merged = pd.merge(kk, sha, how="inner", left_on="ID_1", right_on="ID_1", suffixes=('_kk', '_sha'),
#                          indicator=False, validate=None)
# sha_grouped = (kk_sha_merged.groupby(by=["WoredaCode", "SchoolCode"]).mean().reset_index(drop=False))
# # kk_sha_grouped = (kk_sha_merged.groupby(by=["WoredaCodeNum", "SchoolCode"]).mean().reset_index(drop=False))
#
# sch_kk_merged = pd.merge(
#     sch_grouped,
#     kk_grouped,
#     how="inner",
#     left_on=["Woreda", "SchoolCode"],
#     right_on=["WoredaCode", "SchoolCode"],
#     suffixes=("_sch", "_kk"),
#     indicator=False,
#     validate=None,
# )
# sch_kk_merged[['SchoolCode']] = sch_kk_merged[['SchoolCode']].astype(str)
# sch_grouped[['Woreda']] = sch_grouped[['Woreda']].astype(str)
# sha_grouped[['WoredaCode']] = sha_grouped[['WoredaCode']].astype(str)
# sch_grouped[['SchoolCode']] = sch_grouped[['SchoolCode']].astype(str)
# sha_grouped[['SchoolCode']] = sha_grouped[['SchoolCode']].astype(str)
#
# sch_sha_merged = pd.merge(
#     sch_grouped,
#     sha_grouped,
#     how="inner",
#     left_on=["Woreda", "SchoolCode"],
#     right_on=["WoredaCode", "SchoolCode"],
#     suffixes=("_sch", "_sha"),
#     indicator=False,
#     validate=None,
# )
# sch_kk_merged = pd.merge(
#     sch_kk_merged,
#     elev,
#     how="inner",
#     left_on=["Woreda", "SchoolCode"],
#     right_on=["Woreda", "SchoolCode"],
#     suffixes=("", "_elev"),
#     indicator=False,
#     validate=None,
# )
# ind_gam_merged = pd.merge(
#     ind,
#     gam,
#     how="left",
#     left_on=["ID Number (1)", "ID Number (2)"],
#     right_on=["ID Number (1)", "ID Number (2)"],
#     suffixes=("_ind", "_gam"),
#     indicator=False,
#     validate=None,
# )
#
# sch_wsh_merged = pd.merge(
#     sch,
#     wsh,
#     how="left",
#     left_on=["Woreda", "SchoolCode"],
#     right_on=["WOREDA", "SCHOOL_ID"],
#     suffixes=("_sch", "_wsh"),
#     indicator=False,
#     validate=None,
# )
#
# # kk_grouped, sch_grouped = aggregate_parasites(kk, sch)
# kk_grouped['WoredaCode'] = kk_grouped['WoredaCode'].astype('int64')
# kk_grouped['SchoolCode'] = kk_grouped['SchoolCode'].astype('int64')
# wsh['SCHOOL_ID'] = wsh['SCHOOL_ID'].astype('int64')
#
# kk_wsh_merged = pd.merge(
#     kk_grouped,
#     wsh,
#     how="inner",
#     left_on=["WoredaCode", "SchoolCode"],
#     right_on=["WOREDA", "SCHOOL_ID"],
#     suffixes=("_sch", "_wsh"),
#     indicator=False,
#     validate=None,
# )