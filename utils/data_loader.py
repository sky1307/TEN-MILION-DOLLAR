import sys 
sys.path.append('..')

import numpy as np
import pandas as pd
from utils.ssa import SSA 
# from utils.reprocess_daily import extract_data, ed_extract_data, roll_data

def get_input_data(input_file, default_n, sigma_lst):
    data = pd.read_csv(input_file, header=0)
    H = data['High'].to_list()
    L = data['Low'].to_list()

    lst_H_ssa = SSA(H, default_n)
    lst_L_ssa = SSA(L, default_n)

    H_ssa = lst_H_ssa.reconstruct(sigma_lst)
    L_ssa = lst_L_ssa.reconstruct(sigma_lst)

    data['H_ssa'] = H_ssa
    data['L_ssa'] = L_ssa

    result = data[['High', 'Low', 'H_ssa', 'L_ssa']]
    return result
if __name__ == "__main__":
    res = get_input_data('../data/data1000d_BTCUSDT.csv', 20, [1, 2, 3])
    res.to_csv('../data/modified_data.csv', index=False)
    print(res.head())