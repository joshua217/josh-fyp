import pandas as pd
import requests
import math
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
import csv

from configs import ELE_FILE_PATH, SCH_FILE_PATH, KK_FILE_PATH
# Not imported: GAM_FILE_PATH, INS_FILE_PATH, WASH_FILE_PATH

# Read Data
sch = pd.read_excel(SCH_FILE_PATH)
kk = pd.read_excel(KK_FILE_PATH, sheet_name="Data")

# Get Elevation Data from Google API
def get_elevations():
    coordinates = list(zip(sch["Lat"].to_list(), sch["Long"].to_list()))
    elevations = list()

    for lat, long in tqdm(coordinates):
        if math.isnan(lat) or math.isnan(long):
            elevations.append(None)  # np.nan
            continue

        elev = requests.get(
            "https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&key=API_KEY_HERE".format(
                lat, long
            )
        ).json()
        elevations.append(elev["results"][0]["elevation"])

    with open(r"C:\dev\data\josh-fyp\inputs\national_mapping_data_josh\elevation\elevations.csv", "a") as csvfile:
        for elev in elevations:
            print(elev, file=csvfile)

get_elevations()


# Read in Elevation Data - Going to move this bit into get_elevations()
elev = pd.read_csv(ELE_FILE_PATH, names=['Elevations'])
elev = elev.replace("None", np.nan)
elev = elev.dropna()
elev["Elevations"] = elev["Elevations"].astype("float64")

# Groupby
kk_grouped = kk.groupby(by=["WoredaCode", "SchoolCode"]).mean().reset_index(drop=False)
sch_grouped = sch.groupby(by=["Woreda", "SchoolCode"])

# Add Elevations and merge sch and kk
sch_elev_merged = sch
sch_elev_merged['Elevations'] = elev
sch_kk_merged = pd.merge(
    sch,
    kk_grouped,
    how="left",
    left_on=["Woreda", "SchoolCode"],
    right_on=["WoredaCode", "SchoolCode"],
    suffixes=("_sch", "_kk"),
    indicator=False,
    validate=None,
)

# Kendalls tau
dat1 = sch_kk_merged[['Elevations', 'SmansoniPrev']]
ans = dat1.corr(method='kendall').iloc[1]['Elevations']
# ans_spr = dat.corr(method='spearman')
print("Kendalls tau (Eleion/KK_Prevalence)")
print("SmansoniPrev:", ans)

dat2 = sch_kk_merged[['Elevations', 'HookwormPrev']]
ans = dat2.corr(method='kendall').iloc[1]['Elevations']
print("HookwormPrev:", ans)

dat3 = sch_kk_merged[['Elevations', 'AscarisPrev']]
ans = dat3.corr(method='kendall').iloc[1]['Elevations']
print("AscarisPrev:", ans)

dat4 = sch_kk_merged[['Elevations', 'TrichurisPrev']]
ans = dat4.corr(method='kendall').iloc[1]['Elevations']
print("TrichurisPrev:", ans)

dat5 = sch_kk_merged[['Elevations', 'STHPrev']]
ans = dat5.corr(method='kendall').iloc[1]['Elevations']
print("STHPrev:", ans)
