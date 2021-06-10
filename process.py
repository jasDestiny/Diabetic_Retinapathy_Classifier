import pickle
import pandas
import shutil
import os

file = open('df_train_train', 'rb')
df = pickle.load(file)
directory = {}

df0 = df.loc[df['diagnosis'] == '0']
df1 = df.loc[df['diagnosis'] == '1']
df2 = df.loc[df['diagnosis'] == '2']
df3 = df.loc[df['diagnosis'] == '3']
df4 = df.loc[df['diagnosis'] == '4']

df0fp = df0['file_path']
df1fp = df1['file_path']
df2fp = df2['file_path']
df3fp = df3['file_path']
df4fp = df4['file_path']

directory[0] = df0fp
directory[1] = df1fp
directory[2] = df2fp
directory[3] = df3fp
directory[4] = df4fp

for x, y in directory.items():
    count = 0
    for i in y:
        try:
            shutil.copy(i, str(x))
            count += 1
            if count == 150:
                break
        except Exception as e:
            print(str(x), "is not present")

file.close()
