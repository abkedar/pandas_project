import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    #ipl_df1 = pd.DataFrame(ipl_df['match_code'])
    ipl_df2 = ipl_df[ipl_df['match_code'] == match_code]
    return (ipl_df2)
print get_match_specific_df(392204)
