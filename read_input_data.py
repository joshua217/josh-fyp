# from configs import DATA_PATH, SCH_FILE_NAME, KK_FILE_NAME, WSH_FILE_NAME
import pandas as pd
import os

def read_input_data(data_path, sch_file_name, kk_file_name, wsh_file_name):
    """
    Reads Input Data
    :return: sch, kk, wsh
    """
    sch = pd.read_excel(os.path.join(data_path, sch_file_name))
    kk = pd.read_excel(os.path.join(data_path, kk_file_name), sheet_name="Data", dtype={'SchoolCode': str})
    wsh = pd.read_excel(os.path.join(data_path, wsh_file_name))
    return sch, kk, wsh
