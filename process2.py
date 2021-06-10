import pickle
import pandas
import shutil
import os


file = open('df_train_test', 'rb')
df = pickle.load(file)

df0 = df.loc[df['file_path'] == '0b8bdec9d869.png']
print(df0)
