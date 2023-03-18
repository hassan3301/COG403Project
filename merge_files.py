import pandas as pd
import numpy as np
import os

f_path = "processed_files"

AoA_df = pd.read_csv(os.path.join(f_path, 'AoA.csv'))
brm_df = pd.read_csv(os.path.join(f_path, 'BRM.csv'))
babiness_df = pd.read_csv(os.path.join(f_path, 'Iconicity.csv'))
esm_df = pd.read_csv(os.path.join(f_path, 'ESM.csv'))

