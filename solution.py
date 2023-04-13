import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 561049466

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    p_comb = (x_success + y_success) / (x_cnt + y_cnt)
    p_val = 1 - norm.cdf((y_success / y_cnt - x_success / x_cnt) / np.sqrt(p_comb * (1 - p_comb) * (1 / x_cnt + 1 / y_cnt)))
    return p_val < 0.07
