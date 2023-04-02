import pandas as pd
import numpy as np
import os

f_path = "processed_files"

AoA_df = pd.read_csv(os.path.join(f_path, 'AoA.csv'))
brm_df = pd.read_csv(os.path.join(f_path, 'BRM.csv'))
iconicity_df = pd.read_csv(os.path.join(f_path, 'Iconicity.csv'))
esm_df = pd.read_csv(os.path.join(f_path, 'ESM.csv'))

merge_df = pd.merge(AoA_df, brm_df, on='Word', how='outer')
merge_df = pd.merge(merge_df, iconicity_df, on='Word', how='outer')
merge_df = pd.merge(merge_df, esm_df, on='Word', how='outer')

mergen_df = pd.merge(AoA_df, brm_df, on='Word', how='outer')
mergen_df = pd.merge(mergen_df, esm_df, on='Word', how='outer')

mergen_df = mergen_df.dropna()

merge_df = merge_df.dropna()

merge_df.to_csv(os.path.join(f_path, "merged_with_iconicity.csv"),
                index = None,
                header=True)

merge_df = merge_df.loc[:, ~merge_df.columns.isin(['Word type', 'pos_new', 'Unknown',
                                                   'V.SD.Sum', 'V.Rat.Sum', 'A.SD.Sum', 'A.Rat.Sum', 'Conc.SD',
                                                   'freq_eng', 'Total'])]
# merge_df = merge_df.set_index('Word', drop=True)
merge_df = merge_df.drop_duplicates(subset=['Word'], keep='first')
merge_df.to_csv(os.path.join(f_path, "merged_withoutstring.csv"),
                index = None,
                header=True)

mergen_df.to_csv(os.path.join(f_path, "merged.csv"),
                 index = None,
                 header=True)


