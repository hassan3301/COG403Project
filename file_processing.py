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
AoA_df = AoA_df['Word'].str.lower()

brm_df = pd.read_csv('BRM.csv',
                     index_col=0,
                     header=0)
brm_df = brm_df.replace('', np.NaN)
brm_df = brm_df.loc[:,["Word",
                       "V.Mean.Sum", "V.SD.Sum", "V.Rat.Sum", 
                       "A.Mean.Sum", "A.SD.Sum", "A.Rat.Sum"]]
brm_df = brm_df['Word'].str.lower()

babiness_df = pd.read_csv('babiness.csv',
                          header=0)
babiness_df = babiness_df.replace('', np.NaN)
babiness_df = babiness_df.rename(columns={'word':'Word'})
babiness_df = babiness_df.loc[:,["Word", "task", "rating", "lexicalCategory",
                                 "phonemes", "totalMorphemes", "concreteness", "babyAVG"]]
babiness_df = babiness_df.groupby('Word', as_index=False).mean()
babiness_df = babiness_df['Word'].str.lower()

esm_df = pd.read_excel('ESM.xlsx')
esm_df = esm_df.replace('', np.NaN)
esm_df = esm_df.loc[:,["Word", "Bigram", 
                       "Conc.M", "Conc.SD",
                       "Unknown", "Total", "SUBTLEX"]]
esm_df = esm_df['Word'].str.lower()

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