import pandas as pd
import numpy as np
import os
from scipy import stats
import importlib
from compare import compare # kendalls tau comparison (histogram)
from configs import (
    DATA_PATH,
    SCH_FILE_NAME,
    KK_FILE_NAME,
    WSH_FILE_NAME,
    ELE_FILE_NAME,
    GAM_FILE_NAME,
    SHA_FILE_NAME,
    IND_FILE_NAME,
)
import statistics
from elevation_getter import get_elevations
from read_input_data import read_input_data
from mapping import prev_mapping
from shapely.geometry import Point, Polygon, linestring
import geopandas as gpd
from clean_group_MERGE import clean_group_MERGE
from latlon_utils import get_climate
import geopandas as gpd


from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import tree
from sklearn.utils import resample

import statsmodels.api as sm
import statsmodels.formula.api as smf

if __name__ == "__main__":
    sch, kk, wsh, gam, sha, ind = read_input_data(
        DATA_PATH,
        SCH_FILE_NAME,
        KK_FILE_NAME,
        WSH_FILE_NAME,
        GAM_FILE_NAME,
        SHA_FILE_NAME,
        IND_FILE_NAME,
    )

    # get_elevations(sch, api_key_path)
    elev = pd.read_csv(
        os.path.join(DATA_PATH, ELE_FILE_NAME), dtype={"SchoolCode": str}
    )
    # Get temperatures - should save this to csv
    sch = sch.dropna(subset=['Lat', 'Long'])
    sch['temp_ann'] = sch.apply(lambda row: get_climate(row['Lat'], row['Long'])['tavg', 'ann'],
                                                      axis=1)
    sch['prec_ann'] = sch.apply(lambda row: get_climate(row['Lat'], row['Long'])['prec', 'ann'],
                                                      axis=1)

    all_data_noSHA, all_data = clean_group_MERGE(sch, kk, wsh, sha, elev)
    # Mapping file
    sch_geo = all_data_noSHA[['Long', 'Lat']]
    geometry = [Point(xy) for xy in zip(sch_geo['Long'], sch_geo['Lat'])]
    crs = {'init': 'epsg:4326'}
    geothiopia = gpd.GeoDataFrame(all_data_noSHA, crs=crs, geometry=geometry)
    # RUN
    woreda_path = r"C:\dev\data\josh-fyp\inputs\ETH_admin_SHP\ETH.shp"
    wereda_path = r"C:\dev\data\josh-fyp\inputs\Eth_GIS\eth_weredas.shp"
    ethiopia = gpd.read_file(woreda_path)
    ethiopia.crs = geothiopia.crs

    a = np.linspace(1, 1673, 1673)
    all_data_noSHA['unique'] = a
    schools = all_data_noSHA[['unique', 'geometry']]


    poly_code_1 = ethiopia[['ADM3', 'geometry']]
    schools = gpd.GeoDataFrame(schools, crs=crs)
    joined_1 = gpd.sjoin(poly_code_1, schools, how='inner', op='intersects')
    df = pd.DataFrame(joined_1)
    df['unique'].value_counts()
    all_data_geo = pd.merge(all_data_noSHA, df, how='inner', left_on='unique', right_on='unique',
    suffixes = ('_all', ''), indicator = False, validate = None)
    all_data_geo_grouped = (all_data_geo.groupby(by=['ADM3']).mean().reset_index(drop=False))
    mappable = all_data_geo_grouped[['elevation', 'temp_ann', 'prec_ann', 'Smansoni', 'hookworm', 'trichuris', 'ascaris', 'other_eggs', 'SmansoniPrev', 'AscarisPrev', 'TrichurisPrev', 'STHPrev', 'HookwormPrev', 'ADM3']]
    mappable_merged = pd.merge(mappable, poly_code_1, how='left', left_on='ADM3', right_on='ADM3', suffixes = ('', '_compare'), indicator = False, validate = None)
    dropped = mappable_merged.drop_duplicates(subset=['ADM3'])
    dropped['ones'] = 1

    poly = pd.DataFrame(poly_code_1)
    MAP = pd.merge(poly, dropped, how='left', left_on=['ADM3'], right_on=['ADM3'], suffixes=('', '_dropped'), indicator = False, validate = None)
    geo_map = gpd.GeoDataFrame(MAP)
    # Matching plottable Woreda ID to all_data



    # LR model
    logis_regre = all_data_noSHA.copy()
    para = Smansoni # hookworm ascaris trichuris other_eggs
    test = decision_tree(para, logis_regre, 0.33)




    # WASH and parasites
    i = ('Smansoni', 'hookworm', 'ascaris', 'trichuris')
    for j in i:
        compare(kk_wsh_merged['doors/toilet'], kk_wsh_merged[j], 'Doors per Toilet', j)

    # Prevalence mapping
    map_data = sch_kk_merged[['Lat', 'Long', 'SmansoniPrev']]

    prev_mapping(sch_kk_merged[['Lat', 'Long', 'SmansoniPrev']], 'SmansoniPrev', 'Smansoni Prev')
    prev_mapping(sch_kk_merged[['Lat', 'Long', 'HookwormPrev']], 'HookwormPrev', 'HookwormPrev')
    prev_mapping(sch_kk_merged[['Lat', 'Long', 'AscarisPrev']], 'AscarisPrev', 'AscarisPrev ')
    prev_mapping(sch_kk_merged[['Lat', 'Long', 'TrichurisPrev']], 'TrichurisPrev', 'TrichurisPrev ')
    prev_mapping(sch_kk_merged[['Lat', 'Long', 'STHPrev']], 'STHPrev', 'STHPrev ')

    # Geo Distance Calculations
    sch_geo = map_data[['Long', 'Lat']]
    geometry = [Point(xy) for xy in zip(sch_geo['Long'], sch_geo['Lat'])]
    rivers = gpd.read_file(r"D:\Downloads\eth_rivers\eth_rivers.shp")
    rivers.crs = {'init': 'epsg:32637'}
    rivers = rivers.to_crs('epsg:4326')

    res =
    for point in geometry:
        distances = [point.distance(line) for line in rivers.geometry]
        distance = min(distances)

        for line in rivers.geometry:
            if point.distance(line) == distance:
                our_line = line
                break

        res.append((point, distance, our_line))

    res_df = pd.DataFrame(res, columns=['geometry', 'Dist', 'Line'])
    df2 = res_df[res_df['Dist'] <= 10]

    # proximity to river
    sch_dist = sch_kk_merged.join(res_df)
    sch_dist = sch_dist[sch_dist['Dist'] < 100]
    sch_dist[['SchoolCode']] = sch_dist[['SchoolCode']].astype(int)

    # Elevation and prevalence
    compare(sch_kk_merged["SmansoniPrev"], sch_kk_merged["elevation"], "SmansoniPrev", "Elevation",)
    compare(sch_kk_merged["HookwormPrev"], sch_kk_merged["elevation"], "HookwormPrev", "Elevation",)
    compare(sch_kk_merged["AscarisPrev"], sch_kk_merged["elevation"], "AscarisPrev", "Elevation",)
    compare(sch_kk_merged["TrichurisPrev"], sch_kk_merged["elevation"], "TrichurisPrev", "Elevation",)
    compare(ind_gam_merged["Age"], ind_gam_merged["S. mansoni eggs"], "Age", "S.Mansoni eggs",)

    intensities = ('Smansoni', 'hookworm', 'ascaris', 'trichuris', 'other_eggs')
    for i in intensities:
        a = i + 'Intensity (EPG)'
        compare(basin_dist[i], basin_dist['Dist'], a, 'Dist to basins')
        for i in parasites:
        compare(basin_dist[i], basin_dist['Dist'], i, 'Dist to river')

    # CLIMATE
    sch_kk_merged = sch_kk_merged.dropna(subset=['Lat', 'Long'])
    for i in range(2000):
        print(get_climate(sch_kk_merged['Lat'][i], sch_kk_merged['Long'][i])['tavg', 'mam'])
    d = get_climate(32, 8)['tavg'].mean()

    sch_kk_merged['prec_ann'] = ""


    temp_ann = get_climate(sch_kk_merged['Lat'][i], sch_kk_merged['Long'][i])['tavg', 'ann']
    temp_rain = get_climate(sch_kk_merged['Lat'][i], sch_kk_merged['Long'][i])['tavg', 'mam']
    temp_dry = get_climate(sch_kk_merged['Lat'][i], sch_kk_merged['Long'][i])['tavg', 'mam']
    prec_ann = get_climate(sch_kk_merged['Lat'][i], sch_kk_merged['Long'][i])['prec', 'ann']
    prec_rain = get_climate(sch_kk_merged['Lat'][i], sch_kk_merged['Long'][i])['prec', 'mam']
    prec_dry = get_climate(sch_kk_merged['Lat'][i], sch_kk_merged['Long'][i])['prec', 'mam']

    sch_kk_merged['temp_ann'] = sch_kk_merged.apply(lambda row: get_climate(row['Lat'], row['Long'])['tavg', 'ann'],
                                                    axis=1)

    sch_kk_merged['temp_ann'] = sch_kk_merged.apply(lambda row: get_climate(row['Lat'], row['Long'])['tavg', 'ann'],
                                                    axis=1)
    sch_kk_merged['prec_ann'] = sch_kk_merged.apply(lambda row: get_climate(row['Lat'], row['Long'])['prec', 'ann'],
                                                    axis=1)
    sch_kk_merged.to_csv(os.path.join(DATA_PATH, "work\sch_kk_climate.csv"))

    # STH coinfection
    coinfection = kk_sha_merged[
        (kk_sha_merged['hookworm_kk'] > 0) & (kk_sha_merged['ascaris_kk'] > 0) & (kk_sha_merged['trichuris_kk'] > 0)]

    # Distance to rivers check. (Google maps)
    river10_hookworm = sch_dist.nlargest(10, ['hookworm'])
    geothiopia = gpd.GeoDataFrame(river10_hookworm, crs=crs)
    fig, ax = plt.subplots(figsize=(10, 10))
    rivers.plot(ax=ax)
    geothiopia.plot(ax=ax, markersize=5, color='red')

    sch_dist[['SchoolCode']] = sch_dist[['SchoolCode']].astype(int)
    river_source = sch_dist.merge(kk_wsh_merged, how='inner', left_on=["Woreda", "SchoolCode"],
                                  right_on=["WoredaCode", "SchoolCode"])
    only_river = river_source[river_source['Q2'] == 1]


    # Logistic Regression
    # No decimals
    LR_df = all_data_noSHA.copy()
    LR_df = LR_df[['hookworm', 'Q36', 'Q37', 'Q40', 'Q41', 'Q42']]
    LR_df['Q36'] = LR_df['Q36'].replace([2, 3, 4, 5, 6], 0)
    LR_df['Q37'] = LR_df['Q37'].replace([2, 3, 4], 0)

    # With decimals
    mask = LR_df.hookworm > 0
    col = 'hookworm'
    LR_df.loc[mask, col] = 1
    mask = LR_df.Q40 > 0
    col = 'Q40'
    LR_df.loc[mask, col] = 1
    LR_df['Q40'] = LR_df['Q40'].fillna(0)
    mask = LR_df.Q41 > 0
    col = 'Q41'
    LR_df.loc[mask, col] = 1
    mask = LR_df.Q42 > 0
    col = 'Q42'
    LR_df.loc[mask, col] = 1
    LR_df['Q36'] = LR_df['Q36'].fillna(0)
    LR_df['Q37'] = LR_df['Q37'].fillna(0)
    LR_df['Q40'] = LR_df['Q40'].fillna(0)
    LR_df['Q41'] = LR_df['Q41'].fillna(0)
    LR_df['Q42'] = LR_df['Q42'].fillna(0)

    # Model
    X = LR_df[['Q36', 'Q37', 'Q40', 'Q41', 'Q42']]
    y = LR_df['hookworm']
    model = sm.Logit(y, X)
    model = model.fit()
    model.summary()

    np.exp(outputs)

    from sklearn import preprocessing
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    import seaborn as sns

    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    logit = sm.Logit(y, X)
    X = X.dropna()


    # Survey
    wsh_count = wsh.drop(['ENUMERATOR_NAME', 'ENUMERATOR_ID', 'DATE_OF_SURVEY', 'Unnamed: 253',
                          "Status (1=fine, 2=smartphone and WASH match but not with schoolsformapping (basically fine), 3=WASH code correct but absent from smartphone database, 4=WASH code correct but corresponds to different school in smartphone database, 5-WASH code is wrong (schoolsformapping and smartphone agree, WASH is different), 6 - WASH code is wrong (different name in schools for mapping, absent from smartphone database), 7=WASH code is wrong (missing from schoolsformapping and smartphone databases), 8=mistakes in both databases (names don't match up between either), 9=WASH code wrong (different name in schools for mapping, absent from smartphone database), 2=needs checking, 3=no idea, 4=fine but no disease data)",
                          'NOTES', 'Added on 01102014?', 'School and woreda code changed on 011014?',
                          'Changed after comparison with smartphone, school ID databases 01102014',
                          'Previous woreda code (before 01102014)', 'Previous school code (before 01102014)',
                          'School ID - WASH', 'Proposed codes:'], axis=1)
    for c in wsh_count.columns:
        print("---- %s ---" % c)
        print(wsh_count[c].value_counts())

    # Proxy for socio-economic factors
    guards_dry = kk_wsh_merged[kk_wsh_merged['Q12_O'] == ('HIRED LABOURERS' or "SCHOOL GURADS")]
    guards_rain = kk_wsh_merged[kk_wsh_merged['Q12_O'] == ('HIRED LABOURERS' or "SCHOOL GURADS")]
    guards = pd.concat([guards_dry, guards_rain])
    # verified as same 6 schools
    # clipboard = guards.drop(columns=['ID_1', 'ID_2','KK_Urine', 'schoolid', 'WOREDA', 'SCHOOL_ID', 'ENUMERATOR_NAME', 'ENUMERATOR_ID', 'DATE_OF_SURVEY', 'Q1', 'Q2', 'Q2_O', 'Q3', 'Q3_O', 'Q4', 'Q4_O', 'Q5', 'Q5_O', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q12_O', 'Q13', 'Q13_O', 'Q14', 'Q15', 'Q16_1', 'Q16_2', 'Q16_3', 'Q16_4', 'Q16_5', 'Q16_6', 'Q16_7', 'Q16_8', 'Q16_O', 'Q17_1', 'Q17_2', 'Q17_3', 'Q17_4', 'Q17_5', 'Q17_6', 'Q17_7', 'Q17_8', 'Q17_O', 'Q18', 'Q18_O', 'Q19', 'Q19_O', 'Q20', 'Q20_O', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q25_O', 'Q26', 'Q27_1', 'Q27_2', 'Q27_3', 'Q27_4', 'Q27_5', 'Q27_6', 'Q27_7', 'Q27_8', 'Q27_O', 'Q28_1', 'Q28_2', 'Q28_3', 'Q28_4', 'Q28_5', 'Q28_6', 'Q28_7', 'Q28_8', 'Q28_O', 'Q29', 'Q29_O', 'Q30', 'Q31_1', 'Q31_2', 'Q31_3', 'Q31_4', 'Q31_5', 'Q31_6', 'Q31_7', 'Q31_8', 'Q31_O', 'Q32', 'Q32_O', 'Q33', 'Q33_O', 'Q34', 'Q34_O', 'Q35', 'Q35_O', 'Q36', 'Q36_AMT', 'Q36_O', 'Q37', 'Q37_O', 'Q38', 'Q38_O', 'Q39', 'Q39_O', 'Q40', 'Q41', 'Q42', 'Q43', 'Q44', 'Q45_1_1', 'Q45_2_1', 'Q45_3_1', 'Q45_4_1', 'Q45_1_2', 'Q45_2_2', 'Q45_3_2', 'Q45_4_2', 'Q45_1_3', 'Q45_2_3', 'Q45_3_3', 'Q45_4_3', 'Q45_1_4', 'Q45_2_4', 'Q45_3_4', 'Q45_4_4', 'Q45_1_5', 'Q45_2_5', 'Q45_3_5', 'Q45_4_5', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50', 'Q51', 'Q52', 'Q53', 'Q54', 'Q55', 'Q56', 'Q57', 'Q58', 'Q59', 'Q60', 'Q61', 'Q62', 'Q63', 'Q63_O', 'Q64', 'Q65_1_1', 'Q65_1_2', 'Q65_1_3', 'Q65_1_4', 'Q65_1_5', 'Q65_1_6', 'Q65_2_1', 'Q65_2_2', 'Q65_2_3', 'Q65_2_4', 'Q65_2_5', 'Q65_2_6', 'Q65_3_1', 'Q65_3_2', 'Q65_3_3', 'Q65_3_4', 'Q65_3_5', 'Q65_3_6', 'Q65_4_1', 'Q65_4_2', 'Q65_4_3', 'Q65_4_4', 'Q65_4_5', 'Q65_4_6', 'Q65_5_1', 'Q65_5_2', 'Q65_5_3', 'Q65_5_4', 'Q65_5_5', 'Q65_5_6', 'Q65_6_1', 'Q65_6_2', 'Q65_6_3', 'Q65_6_4', 'Q65_6_5', 'Q65_6_6', 'Q65_7_1', 'Q65_7_2', 'Q65_7_3', 'Q65_7_4', 'Q65_7_5', 'Q65_7_6', 'Q65_8_1', 'Q65_8_2', 'Q65_8_3', 'Q65_8_4', 'Q65_8_5', 'Q65_8_6', 'Q65_9_1', 'Q65_9_2', 'Q65_9_3', 'Q65_9_4', 'Q65_9_5', 'Q65_9_6', 'Q65_10_1', 'Q65_10_2', 'Q65_10_3', 'Q65_10_4', 'Q65_10_5', 'Q65_10_6', 'Q65_11_1', 'Q65_11_2', 'Q65_11_3', 'Q65_11_4', 'Q65_11_5', 'Q65_11_6', 'Q65_12_1', 'Q65_12_2', 'Q65_12_3', 'Q65_12_4', 'Q65_12_5', 'Q65_12_6', 'Q65_13_1', 'Q65_13_2', 'Q65_13_3', 'Q65_13_4', 'Q65_13_5', 'Q65_13_6', 'Q65_14_1', 'Q65_14_2', 'Q65_14_3', 'Q65_14_4', 'Q65_14_5', 'Q65_14_6', 'Q65_15_1', 'Q65_15_2', 'Q65_15_3', 'Q65_15_4', 'Q65_15_5', 'Q65_15_6', 'Q65_16_1', 'Q65_16_2', 'Q65_16_3', 'Q65_16_4', 'Q65_16_5', 'Q65_16_6', 'Q65_17_1', 'Q65_17_2', 'Q65_17_3', 'Q65_17_4', 'Q65_17_5', 'Q65_17_6', 'Q66', 'Unnamed: 253', "Status (1=fine, 2=smartphone and WASH match but not with schoolsformapping (basically fine), 3=WASH code correct but absent from smartphone database, 4=WASH code correct but corresponds to different school in smartphone database, 5-WASH code is wrong (schoolsformapping and smartphone agree, WASH is different), 6 - WASH code is wrong (different name in schools for mapping, absent from smartphone database), 7=WASH code is wrong (missing from schoolsformapping and smartphone databases), 8=mistakes in both databases (names don't match up between either), 9=WASH code wrong (different name in schools for mapping, absent from smartphone database), 2=needs checking, 3=no idea, 4=fine but no disease data)", 'NOTES', 'Added on 01102014?', 'School and woreda code changed on 011014?', 'Changed after comparison with smartphone, school ID databases 01102014', 'Previous woreda code (before 01102014)', 'Previous school code (before 01102014)', 'School ID - WASH', 'Proposed codes:'])
    # clipboard.to_clipboard(sep='\t')

    # Rainy/Dry Season Value
    plt.hist(kk_wsh_merged['Q2'], bins=6, color='#BCF56C')
    plt.title('Which type of source is mainly used in the dry season? 1,847 schools')
    plt.annotate('Surface Water', (1.25, 250))
    plt.annotate('Borehole/Protected Dug Well', (2.1, 50))
    plt.annotate('Standpipe', (3.35, 90))
    plt.annotate('Rainwater Collection', (4.20, 90))
    plt.annotate('Protected Spring', (5.25, 50))
    plt.annotate('Unprotected Dug Well', (6.14 , 20))

    compare(kk_wsh_merged['Q2'], kk_wsh_merged['Q3'], 'Dry Season', 'Rainy Season')

    samesies = kk_wsh_merged[kk_wsh_merged['Q2'] == kk_wsh_merged['Q3']]
    different = kk_wsh_merged[kk_wsh_merged['Q2'] != kk_wsh_merged['Q3']]

    # Another possible proxy for socio-economic status Q63 on Hired cleaners
    hired_cleaners = kk_wsh_merged[kk_wsh_merged['Q63'] == 2]

    # Functional Doors per Toilet
    # Fill NaN
    cols = (
    'Q65_3_1', 'Q65_3_2', 'Q65_3_3', 'Q65_3_4', 'Q65_3_5', 'Q65_3_6', 'Q65_2_1', 'Q65_2_2', 'Q65_2_3', 'Q65_2_4',
    'Q65_2_5', 'Q65_2_6', 'Q65_4_1', 'Q65_4_2', 'Q65_4_3', 'Q65_4_4', 'Q65_4_5', 'Q65_4_6', 'Q65_5_1', 'Q65_5_2', 'Q65_5_3', 'Q65_5_4', 'Q65_5_5', 'Q65_5_6', 'Q65_6_1', 'Q65_6_2', 'Q65_6_3', 'Q65_6_4', 'Q65_6_5', 'Q65_6_6', 'Q65_7_1', 'Q65_7_2', 'Q65_7_3', 'Q65_7_4', 'Q65_7_5', 'Q65_7_6', 'Q65_8_1', 'Q65_8_2', 'Q65_8_3', 'Q65_8_4', 'Q65_8_5', 'Q65_8_6', 'Q65_9_1', 'Q65_9_2', 'Q65_9_3', 'Q65_9_4', 'Q65_9_5', 'Q65_9_6', 'Q65_10_1', 'Q65_10_2', 'Q65_10_3', 'Q65_10_4', 'Q65_10_5', 'Q65_10_6', 'Q65_11_1', 'Q65_11_2', 'Q65_11_3', 'Q65_11_4', 'Q65_11_5', 'Q65_11_6', 'Q65_12_1', 'Q65_12_2', 'Q65_12_3', 'Q65_12_4', 'Q65_12_5', 'Q65_12_6', 'Q65_13_1', 'Q65_13_2', 'Q65_13_3', 'Q65_13_4', 'Q65_13_5', 'Q65_13_6', 'Q65_14_1', 'Q65_14_2', 'Q65_14_3', 'Q65_14_4', 'Q65_14_5', 'Q65_14_6', 'Q65_15_1', 'Q65_15_2', 'Q65_15_3', 'Q65_15_4', 'Q65_15_5', 'Q65_15_6', 'Q65_16_1', 'Q65_16_2', 'Q65_16_3', 'Q65_16_4', 'Q65_16_5', 'Q65_16_6', 'Q65_17_1', 'Q65_17_2', 'Q65_17_3', 'Q65_17_4', 'Q65_17_5', 'Q65_17_6')

    for i in cols:
        kk_wsh_merged[i].fillna(0, inplace=True)

    kk_wsh_merged['doors/toilet'] = (kk_wsh_merged['Q65_3_1'] + kk_wsh_merged['Q65_3_2'] + kk_wsh_merged['Q65_3_3'] +
                                     kk_wsh_merged['Q65_3_4'] + kk_wsh_merged['Q65_3_5'] + kk_wsh_merged['Q65_3_6']) / (
                                                kk_wsh_merged['Q65_2_1'] + kk_wsh_merged['Q65_2_2'] + kk_wsh_merged[
                                            'Q65_2_3'] + kk_wsh_merged['Q65_2_4'] + kk_wsh_merged['Q65_2_5'] +
                                                kk_wsh_merged['Q65_2_6'])

    strange = kk_wsh_merged[kk_wsh_merged['doors/toilet'] > 1]
    doors_toilet = kk_wsh_merged[kk_wsh_merged['doors/toilet'] < 5]

    # Blocks Used
    kk_wsh_merged['blocks used'] = (kk_wsh_merged['Q65_1_1'] > 0).astype(int) + (kk_wsh_merged['Q65_1_2'] > 0).astype(
        int) + (kk_wsh_merged['Q65_1_3'] > 0).astype(int) + (kk_wsh_merged['Q65_1_4'] > 0).astype(int) + (
                                               kk_wsh_merged['Q65_1_5'] > 0).astype(int) + (
                                               kk_wsh_merged['Q65_1_6'] > 0).astype(int)
    hist0plot(kk_wsh_merged['blocks used'], 6, 'Number of Latrine Blocks used per school', 0.3, '#BCF56C', 1)

    # Homogeneity of latrine blocks within schools
    for row in kk_wsh_merged.iterrows():
        a = np.array([kk_wsh_merged['Q65_4_1'][row], kk_wsh_merged['Q65_4_2'][row], kk_wsh_merged['Q65_4_3'][row],
                      kk_wsh_merged['Q65_4_4'][row], kk_wsh_merged['Q65_4_5'][row], kk_wsh_merged['Q65_4_6'][row]])
        trim_0 = np.trim_zeros(a)
        sim_score = len(np.unique(trim_0))/len(trim_0)


    def similarity_count_Q65_4(row):
        unique = len(np.unique(np.trim_zeros(np.array(
            [row['Q65_4_1'], row['Q65_4_2'], row['Q65_4_3'], row['Q65_4_4'], row['Q65_4_5'], row['Q65_4_6']]))))
        length = (len(
            np.trim_zeros(np.array(
                [row['Q65_4_1'], row['Q65_4_2'], row['Q65_4_3'], row['Q65_4_4'], row['Q65_4_5'], row['Q65_4_6']]))))
        if length > 0:
            ans = unique/length
        elif length == 0:
            ans = 0
        return ans

    def similarity_count_Q65_14(row):
        unique = len(np.unique(np.trim_zeros(np.array(
            [row['Q65_14_1'], row['Q65_14_2'], row['Q65_14_3'], row['Q65_14_4'], row['Q65_14_5'], row['Q65_14_6']]))))
        length = (len(
            np.trim_zeros(np.array(
                [row['Q65_14_1'], row['Q65_14_2'], row['Q65_14_3'], row['Q65_14_4'], row['Q65_14_5'], row['Q65_14_6']]))))
        if length > 0:
            ans = unique/length
        elif length == 0:
            ans = 0
        return ans
    def median_odour(row):
        a = np.trim_zeros(np.array([row['Q65_14_1'], row['Q65_14_2'], row['Q65_14_3'], row['Q65_14_4'], row['Q65_14_5'], row['Q65_14_6']]), trim='bf')
        if len(a) != 0:
            ans = statistics.median(a)
        elif len(a) == 0:
            ans = 0
        return ans


    logis_regre['sim_Q65'] = logis_regre.apply(similarity_count_Q65_4, axis=1)
    logis_regre['sim_odour'] = logis_regre.apply(similarity_count_Q65_14, axis=1)
    logis_regre['median_odour'] = logis_regre.apply(median_odour, axis=1)




# console run
#
#
# import pandas as pd
# import numpy as np
# import os
# from scipy import stats
# import importlib
# from compare import compare
# from configs import (
#     DATA_PATH,
#     SCH_FILE_NAME,
#     KK_FILE_NAME,
#     WSH_FILE_NAME,
#     ELE_FILE_NAME,
#     GAM_FILE_NAME,
#     SHA_FILE_NAME,
#     IND_FILE_NAME,
# )
# from elevation_getter import get_elevations
# from read_input_data import read_input_data
# from mapping import prev_mapping
# # from nlp import classify, sample_analyze_sentiment
# from shapely.geometry import Point, Polygon, linestring
# import geopandas as gpd
# from clean_group_MERGE import clean_group_MERGE
# from latlon_utils import get_climate
#
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\dev\data\josh-fyp\api_key\FGP_NLP_josh-fyp-294bc4b423e6.json"
# sch, kk, wsh, gam, sha, ind = read_input_data(
#     DATA_PATH,
#     SCH_FILE_NAME,
#     KK_FILE_NAME,
#     WSH_FILE_NAME,
#     GAM_FILE_NAME,
#     SHA_FILE_NAME,
#     IND_FILE_NAME,
# )
#
# # get_elevations(sch, api_key_path)
# elev = pd.read_csv(
#     os.path.join(DATA_PATH, ELE_FILE_NAME), dtype={"SchoolCode": str}
# )
#
# kk_sha_merged, sch_kk_merged, sch_sha_merged, ind_gam_merged, sch_wsh_merged, kk_wsh_merged, sha_grouped = clean_group_MERGE(sch,
#                                                                                                                 kk,
#                                                                                                                 wsh,
#                                                                                                                 gam,
#                                                                                                                 sha,
#                                                                                                                 ind,
#                                                                                                                 elev)
# # Prevalence mapping
# map_data = sch_kk_merged[['Lat', 'Long', 'SmansoniPrev']]
#
# # Geo calculations
# sch_geo = map_data[['Long', 'Lat']]
# geometry = [Point(xy) for xy in zip(sch_geo['Long'], sch_geo['Lat'])]
# rivers = gpd.read_file(r"D:\Downloads\eth_rivers\eth_rivers.shp")
# rivers.crs = {'init': 'epsg:32637'}
# rivers = rivers.to_crs('epsg:4326')
#
# res = []
# for point in geometry:
#     distances = [point.distance(line) for line in rivers.geometry]
#     distance = min(distances)
#
#     for line in rivers.geometry:
#         if point.distance(line) == distance:
#             our_line = line
#             break
#
#     res.append((point, distance, our_line))
#
# res_df = pd.DataFrame(res, columns=['geometry', 'Dist', 'Line'])
# df2 = res_df[res_df['Dist'] <= 10]
#
# # proximity to river
# sch_dist = sch_kk_merged.join(res_df)
# sch_dist = sch_dist[sch_dist['Dist'] < 100]
#
#
# # CLIMATE
# sch_kk_climate = sch_kk_merged.dropna(subset=['Lat', 'Long'])
# # for i in range(2000):
# #     print(get_climate(sch_kk_climate['Lat'][i], sch_kk_merged['Long'][i])['tavg', 'mam'])
# # d = get_climate(32, 8)['tavg'].mean()
#
#
# sch_kk_climate['temp_ann'] = sch_kk_climate.apply(lambda row: get_climate(row['Lat'], row['Long'])['tavg', 'ann'],
#                                                 axis=1)
# sch_kk_climate['prec_ann'] = sch_kk_climate.apply(lambda row: get_climate(row['Lat'], row['Long'])['prec', 'ann'],
#                                                 axis=1)

np.array([kk_wsh_merged['Q65_4_1'][row], kk_wsh_merged['Q65_4_2'][row], kk_wsh_merged['Q65_4_3'][row], kk_wsh_merged['Q65_4_4'][row], kk_wsh_merged['Q65_4_5'][row], kk_wsh_merged['Q65_4_6'][row]])