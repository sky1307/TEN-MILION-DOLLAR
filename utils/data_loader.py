import sys 
sys.path.append('..')

import numpy as np
import pandas as pd
from utils.ssa import SSA 
from utils.reprocess_daily import extract_data, ed_extract_data, roll_data from

def get_input_data(input_file, default_n, sigma_list):
    data = pd.read_csv(input_file, header=0)
    