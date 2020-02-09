import pandas as pd

from configs import KK_FILE_PATH

if __name__ == "__main__":
    # individual = pd.read_excel(r"C:\dev\data\josh-fyp\inputs\national_mapping_data_josh\Disease\Individual_3_7_14_anon.xlsx")
    kk = pd.read_excel(
        KK_FILE_PATH,
        sheet_name="Data",
        # dtype={"WoredaCode": str, "SchoolCode": str},
    )
    wash = pd.read_excel(
        r"C:\dev\data\josh-fyp\inputs\national_mapping_data_josh\WASH-cleaned\WASHData.xlsx"
    )

    kk_grouped = (
        kk.groupby(by=["WoredaCode", "SchoolCode"]).mean().reset_index(drop=False)
    )

    kk_wash_merged = pd.merge(
        kk_grouped,
        wash,
        how="left",
        left_on=["WoredaCode", "SchoolCode"],
        right_on=["WOREDA", "SCHOOL_ID"],
        suffixes=("_kk", "_wash"),
        indicator=False,
        validate=None,
    )

    kk_wash_merged.dropna(subset=["Q1"], inplace=True)
    kk_wash_merged["SmansoniPrev"].hist(bins=100)

    print(kk_wash_merged)
