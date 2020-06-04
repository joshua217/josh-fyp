from scipy import stats
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.ticker import FormatStrFormatter
from numpy.polynomial.polynomial import polyfit
import numpy as np





# for i in parasites:
#     compare(sch_dist[i], sch_dist['Dist'], i, 'Dist to river')

def compare(x, y, x_name, y_name, save_1, tick_1, tick_loc, tick_label):
    """
    Compare computes kendalls tau and p-value, outputs graph
    :param x:
    :param y:
    :param x_name:
    :param y_name:
    :return:
    """
    plt.figure()
    tau, p = stats.kendalltau(x, y, nan_policy='omit')
    ori_p = p
    if p < 0.05:
        p = "p < 0.05"
    elif p>= 0.05:
        p = round(p, 3)
    plt.scatter(x, y, c='blue', alpha=0.3)
    # b, m = polyfit(x, y, 1)
    # plt.plot(x, b+m*x, '-')
    plt.xlabel(x_name)
    plt.ylabel(y_name)

    n = len(x)
    r = tau

    alpha = 0.05
    z_one = 1 - (alpha / 2)
    z_r = 0.5 * (np.log((1 + r)/(1 - r)))
    z_upper = z_r + (z_one*(np.sqrt(0.437/n)))
    z_lower = z_r - (z_one * (np.sqrt(0.437 / n)))
    CI_upper = (np.exp(2*z_upper)-1)/(np.exp(2*z_upper)+1)
    CI_lower = (np.exp(2 * z_lower) - 1) / (np.exp(2 * z_lower) + 1)
    print('p', p, 'CI:', CI_lower, CI_upper)

    plt.suptitle(r"x: {}, y: {}     No.sch: {}".format(x_name, y_name, n))
    plt.title("Kendall's tau: {}, p-value: {}, 95% CI:[{} to {}]".format(round(r, 3), p, round(CI_lower, 3), round(CI_upper, 3)))
    if tick_1 == 1:
        plt.xticks(tick_loc, tick_label)
    r_tau = round(tau, 5)
    r_p = p

    if save_1 == 1:
        plt.savefig(r"C:\dev\data\josh-fyp\outputs\Obj_1\toilet_privacy\{}_against_{}.png".format(x_name, y_name))


def hist0plot(x, bins, title, alpha, color, save_1, tick_loc, tick_label, x_label, y_label, tick_1):
    """ General Histogram plotting"""
    plt.figure(figsize=(15,15))
    plt.hist(x, bins=bins, alpha=alpha, color=color)
    plt.suptitle(title)
    plt.show()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    num_sch = len(x)
    Annotate = 'No. of schools: {}'.format(num_sch)
    plt.title(Annotate)
    if tick_1 == 1:
        plt.xticks(tick_loc, tick_label)
    if save_1 == 1:
        plt.savefig(r"C:\dev\data\josh-fyp\outputs\Mapping\proximity_tau\{}.png".format(title))
    # hist0plot(all_data_noSHA['Q1'], 3, 'Water Sources within school compound', 0.5, '#BCF56C', 0, [1.333, 2, 2.666], ['Yes, always used', 'Yes, only used in RAINY season', 'No, water always brought in'])

def mwu_compare(x, y):
    mann_u, p = stats.mannwhitneyu(x, y)
    plt.figure(figsize=(10, 10))

    print(mann_u, 'P-value:', p)

def prev_check(df):
    a = df[df['SmansoniPrev'] == 0]
    mansoni = 1 - (len(a)/len(df))
    print('Smansoni % Prev:', mansoni)
    a = df[df['HookwormPrev'] == 0]
    mansoni = 1 - (len(a)/len(df))
    print('Hookworm % Prev:', mansoni)
    a = df[df['AscarisPrev'] == 0]
    mansoni = 1 - (len(a)/len(df))
    print('Ascaris % Prev:', mansoni)
    a = df[df['TrichurisPrev'] == 0]
    mansoni = 1 - (len(a)/len(df))
    print('Trichuris % Prev:', mansoni)
    a = df[df['STHPrev'] == 0]
    mansoni = 1 - (len(a)/len(df))
    print('Other STH % Prev:', mansoni)


# Saving
def csv_me(df, name_csv):
    df.to_csv(r"C:\dev\data\josh-fyp\work\{}".format(name_csv))


def distribution_comparison(temp_0, temp_1, prec_0, prec_1, para):
    ks, p = stats.ks_2samp(temp_0, temp_1)
    mwu, p_mwu = stats.mannwhitneyu(temp_0, temp_1)
    fig, (axa, axb) = plt.subplots(2, 1, figsize=(10, 10))
    plt.suptitle('Distribution Comparison of {}'.format(para))
    plt.title('0% Prev Schools: {}      Non-0% Prev Schools: {}'.format(len(temp_0), len(temp_1)))
    axa.hist(temp_0, 100, alpha=0.3, color='blue', label='0% Prevalence')
    axa.hist(temp_1, 100, alpha=0.3, color='red', label='Non-0 Prevalence')
    axa.set_xlabel('Annual Mean Temperature Distribution')
    axa.set_ylabel('Number of Schools')
    mwu = round(mwu, 3)
    p_mwu = round(p_mwu, 3)
    ks = round(ks, 3)
    p = round(p, 3)
    if p < 0.01:
        p = '< 0.05'
    if p_mwu < 0.05:
        p_mwu = '< 0.05'
    axa.annotate('MannUWhitney: {} p:{}'.format(mwu, p_mwu), xy=(0.15, 0.85), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
    axa.annotate('K-S: {} p:{}'.format(ks, p), xy=(0.15, 0.825), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
    axa.legend()

    ks, p = stats.ks_2samp(prec_0, prec_1)
    mwu, p_mwu = stats.mannwhitneyu(prec_0, prec_1)
    axb.hist(prec_0, 100, alpha=0.3, color='blue', label='0% Prevalence')
    axb.hist(prec_1, 100, alpha=0.3, color='red',label='Non-0 Prevalence')
    axb.set_xlabel('Annual Mean Precipitation Distribution')
    axb.set_ylabel('Number of Schools')
    mwu = round(mwu, 3)
    p_mwu = round(p_mwu, 3)
    ks = round(ks, 3)
    p = round(p, 3)
    if p < 0.01:
        p = '< 0.05'
    if p_mwu < 0.05:
        p_mwu = '< 0.05'
    axb.annotate('MannUWhitney: {} p:{}'.format(mwu, p_mwu), xy=(0.15, 0.45),
                 xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12,
                 color='#555555')
    axb.annotate('K-S: {} p:{}'.format(ks, p), xy=(0.15, 0.425), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
    axb.legend()


