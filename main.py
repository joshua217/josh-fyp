import pandas as pd
import numpy as np
import os

from compare import compare
from configs import DATA_PATH, SCH_FILE_NAME, KK_FILE_NAME, WSH_FILE_NAME, ELE_FILE_NAME

from elevation_getter import get_elevations
from parasite_aggregator import aggregate_parasites
from read_input_data import read_input_data

if __name__ == "__main__":

    sch, kk, wsh = read_input_data(
        DATA_PATH, SCH_FILE_NAME, KK_FILE_NAME, WSH_FILE_NAME
    )
    # get_elevations(sch, api_key_path)
    elev = pd.read_csv(os.path.join(DATA_PATH, ELE_FILE_NAME), dtype={'SchoolCode': str})
    kk_grouped, sch_grouped = aggregate_parasites(kk, sch)

    sch_kk_merged = pd.merge(
        elev,
        kk_grouped,
        how="left",
        left_on=["Woreda", "SchoolCode"],
        right_on=["WoredaCode", "SchoolCode"],
        suffixes=("_sch", "_kk"),
        indicator=False,
        validate=None,
    )

    compare(sch_kk_merged['SmansoniPrev'], sch_kk_merged["elevation"], "SmansoniPrev", "Elevation")
    compare(sch_kk_merged['HookwormPrev'], sch_kk_merged["elevation"], "HookwormPrev", "Elevation")
    compare(sch_kk_merged['AscarisPrev'], sch_kk_merged["elevation"], "AscarisPrev", "Elevation")
    compare(sch_kk_merged['TrichurisPrev'], sch_kk_merged["elevation"], "TrichurisPrev", "Elevation")


