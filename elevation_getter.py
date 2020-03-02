import os

import numpy as np
import pandas as pd
import requests
from tqdm import tqdm

from configs import DATA_PATH

api_key_path = os.path.join(DATA_PATH, r"api_key\api_key.txt")
tqdm.pandas()


def get_elevations(sch, api_key_path):
    """
    This function gets elevations for the schools
    :param sch: df of schools
    :param api_key_path: path to txt file containing api key
    :return: none, outputs elevations csv
    """

    with open(api_key_path) as file:
        api_key = file.read()

    elevations = sch[["Woreda", "SchoolCode", "Lat", "Long"]]

    def f(x):
        try:
            elevation = requests.get(
                (
                    "https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&key="
                    + api_key
                ).format(x["Lat"], x["Long"])
            ).json()["results"][0]["elevation"]
        except:
            elevation = np.nan
        return elevation

    elevations["elevation"] = elevations.progress_apply(f, axis=1)

    elevations.to_csv(os.path.join(DATA_PATH, "work\elevations.csv"))


if __name__ == "__main__":
    from configs import DATA_PATH, SCH_FILE_NAME

    sch = pd.read_excel(os.path.join(DATA_PATH, SCH_FILE_NAME))
    get_elevations(sch, api_key_path)

