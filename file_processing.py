import pandas as pd
import numpy as np
import os

f_path = "processed_files"

AoA_df = pd.read_csv('AoA.csv', 
                     header=0, 
                     skiprows=list(range(0, 3)), 
                     usecols=list(range(0, 10)))
AoA_df = AoA_df.replace('.', np.NaN)
AoA_df = AoA_df.replace('#N/A', np.NaN)

brm_df = pd.read_csv('BRM.csv',
                     index_col=0,
                     header=0)
brm_df = brm_df.replace('', np.NaN)

babiness_df = pd.read_csv('babiness.csv',
                          header=0)
babiness_df = babiness_df.replace('', np.NaN)

esm_df = pd.read_excel('ESM.xlsx')
esm_df = esm_df.replace('', np.NaN)

AoA_df.to_csv(os.path.join(f_path, "AoA.csv"),
              index = None,
              header=True)
brm_df.to_csv(os.path.join(f_path, "BRM.csv"),
              index = None,
              header=True)
babiness_df.to_csv(os.path.join(f_path, "Iconicity.csv"),
                   index = None,
                   header=True)
esm_df.to_csv(os.path.join(f_path, "ESM.csv"), 
              index = None,
              header=True)