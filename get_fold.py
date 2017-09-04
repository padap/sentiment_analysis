import pandas as pd
from sklearn.utils import shuffle
import random
import numpy as np
import sys 

FIN = 'data/data_clear.csv'

def get_fold(N_fold = 10, K_fold = 1, seed = 42, df = None):
    random.seed(seed)
    np.random.seed(seed = seed)
    if df == None:
        df = pd.read_csv(FIN)
    random.seed(seed)
    df = df.iloc[random.sample(list(range(len(df))),len(df))]
    df.index = range(len(df))
    list_ind = {}
#     print('lbl\tnow\tzero')
    for lbl in [0,1,-1]:
        temp = list(df[df['label']==lbl].index)
        temp_temp = temp[K_fold::N_fold]
#         print(str(lbl)+'\t'+str(len(temp_temp))+'\t'+str(len(temp[0::N_fold])))
        if len(temp[0::N_fold]) != len(temp_temp):
#            sys.stderr.write('here')
            tmp_df = df[df['label']==lbl].index
            list_ind[lbl] = temp_temp+[tmp_df[random.randint(0,len(tmp_df)-1)]]
        else:
            list_ind[lbl] = temp_temp

    df_new = df.iloc[list(list_ind[0])+list(list_ind[1])+list(list_ind[-1])]
    return df_new

# temp = get_fold(N_fold=10,K_fold=9,seed=41,df = None)
# for lbl in temp['label'].unique():
#     print(str(lbl)+'\t'+str(len(temp[temp['label']==lbl])))
# temp