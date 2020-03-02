from scipy import stats
from matplotlib import pyplot as plt

def compare(x, y, x_name, y_name):
    plt.figure()
    tau, p = stats.kendalltau(x, y, nan_policy='omit')
    plt.scatter(x, y)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title("x:{}, y:{}\ntau: {}, p: {}".format(x_name, y_name, tau, p))


    plt.savefig(r"C:\dev\data\josh-fyp\outputs\{}_against_{}.png".format(x_name, y_name))
    # return

