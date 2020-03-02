def aggregate_parasites(kk, sch):
    kk_grouped = (
        kk.groupby(by=["WoredaCode", "SchoolCode"]).mean().reset_index(drop=False)
    )
    sch_grouped = sch.groupby(by=["Woreda", "SchoolCode"])
    return kk_grouped, sch_grouped