def odds_ratio(a, b, c, d, wash_factors):
    """
    a = lambda x: x['hookworm'] > 0
    b = lambda x: x['Q66'] == 1
    c = lambda x: x['hookworm'] == 0
    d = lambda x: x['Q66'] == 2
    """

    seriesObj = wash_factors.apply(a, axis=1)
    seriesObj_2 = wash_factors.apply(b, axis=1)
    both = len(seriesObj[seriesObj == True].index) + len(seriesObj_2[seriesObj_2 == True].index)

    seriesObj = wash_factors.apply(c, axis=1)
    seriesObj_2 = wash_factors.apply(d, axis=1)
    none = len(seriesObj[seriesObj == True].index) + len(seriesObj_2[seriesObj_2 == True].index)

    seriesObj = wash_factors.apply(c, axis=1)
    seriesObj_2 = wash_factors.apply(d, axis=1)
    some_1 = len(seriesObj[seriesObj == True].index) + len(seriesObj_2[seriesObj_2 == True].index)

    seriesObj = wash_factors.apply(a, axis=1)
    seriesObj_2 = wash_factors.apply(d, axis=1)
    some_2 = len(seriesObj[seriesObj == True].index) + len(seriesObj_2[seriesObj_2 == True].index)
    OR = (both*none)/(some_1*some_2)
    CI_upper = np.exp(np.log(OR) + 1.96*np.sqrt(1/both + 1/none + 1/some_1 + 1/some_2))
    CI_lower = np.exp(np.log(OR) - 1.96*np.sqrt(1/both + 1/none + 1/some_1 + 1/some_2))

    print('OR: {}, 95% CI: {} to {}'.format(round(OR, 2), round(CI_lower, 2), round(CI_upper, 2)))


    # Odds Ratio configuration
    # a = lambda x: x['hookworm'] > 0
    # b = lambda x: x['Q66'] == 1
    # c = lambda x: x['hookworm'] == 0
    # d = lambda x: x['Q66'] == 2
    # parasites = ['hookworm', 'STHPrev', 'Smansoni', 'ascaris', 'trichuris']