# INDIVIDUAL WASH FACTORS
wsh['SCHOOL_ID'] = wsh['SCHOOL_ID'].astype(str)
wash_factors = pd.merge(wsh, sch_kk_merged, how="inner", left_on=["WOREDA", "SCHOOL_ID"],
                        right_on=["WoredaCode", "SchoolCode"], suffixes=("_wsh", ""), indicator=False,
                        validate=None, )
open_shit = wash_factors[wash_factors['Q66'] == 1]
always_used = wash_factors[wash_factors['Q1'] == 1]
rainy_used = wash_factors[wash_factors['Q1'] == 2]
never_used = wash_factors[wash_factors['Q1'] == 3]
fig, axs = plt.subplots(6, 2)
axs[0, 0].hist(always_used['STHPrev'], 100)
axs[0, 0].set_title('always_used STHPrev')
axs[0, 1].hist(never_used['STHPrev'], 100)
axs[0, 1].set_title('never_used STHPrev')