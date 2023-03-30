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
AoA_df = AoA_df.rename(columns={'WORD':'Word'})
AoA_df = AoA_df.loc[:,["Word", "Word type", "new AoA", "Frequency"]]
AoA_df['Word'] = AoA_df['Word'].str.lower()

brm_df = pd.read_csv('BRM.csv',
                     index_col=0,
                     header=0)
brm_df = brm_df.replace('', np.NaN)
brm_df = brm_df.loc[:,["Word",
                       "V.Mean.Sum", "V.SD.Sum", "V.Rat.Sum", 
                       "A.Mean.Sum", "A.SD.Sum", "A.Rat.Sum"]]
brm_df['Word'] = brm_df['Word'].str.lower()

# Iconicity ratings for 3001 English words were collected by Perry et al. (2015) and Winter et al. (2017a). 

iconicity_df = pd.read_csv('new_iconicity.csv',
                           header=0)
iconicity_df = iconicity_df.replace('', np.NaN)
iconicity_df = iconicity_df.rename(columns={'word':'Word'})
iconicity_df = iconicity_df.loc[:,["Word", "pos_new", "icon_eng", "freq_eng",]]
# iconicity_df = iconicity_df.groupby('Word', as_index=False).mean()
iconicity_df['Word'] = iconicity_df['Word'].str.lower()

esm_df = pd.read_excel('ESM.xlsx')
esm_df = esm_df.replace('', np.NaN)
esm_df = esm_df.loc[:,["Word", "Bigram", 
                       "Conc.M", "Conc.SD",
                       "Unknown", "Total", "SUBTLEX"]]
esm_df['Word'] = esm_df['Word'].str.lower()

AoA_df.to_csv(os.path.join(f_path, "AoA.csv"),
              index = None,
              header=True)
brm_df.to_csv(os.path.join(f_path, "BRM.csv"),
              index = None,
              header=True)
iconicity_df.to_csv(os.path.join(f_path, "Iconicity.csv"),
                    index = None,
                    header=True)
esm_df.to_csv(os.path.join(f_path, "ESM.csv"), 
              index = None,
              header=True)