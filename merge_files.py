import pandas as pd
import numpy as np
import os

f_path = "processed_files"

AoA_df = pd.read_csv(os.path.join(f_path, 'AoA.csv'))
brm_df = pd.read_csv(os.path.join(f_path, 'BRM.csv'))
babiness_df = pd.read_csv(os.path.join(f_path, 'Iconicity.csv'))
esm_df = pd.read_csv(os.path.join(f_path, 'ESM.csv'))

merge_df = pd.concat([AoA_df, brm_df, babiness_df, esm_df])
merge_df.to_csv(os.path.join(f_path, "merged.csv"),
                index = None,
                header=True)