"""
Saves a df to a selected folder. Automatically timestamps the
df.
"""

import datetime
import getpass
import pandas as pd

def df_to_csv_with_timestamped(df, folder_name, file_name):
    """saves a df as csv in selected folder on desktop
    :param: df: selected dataframe
    :param: folder_name: name of folder saved on desktop
    :param: file_name: name of df 
    """
    dir_path = r"C:\Users\%s\Desktop" % getpass.getuser()
    
    timestamp_file = file_name +  "_" + datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d.T%H.%M.%S") + ".csv"
    path = dir_path + "\\" + folder_name + "\\" + timestamp_file
    export_csv = df.to_csv (path, index = None, header=True, encoding='utf-8')
    print("Saved df to CSV here: ", path)
    

data_dict = {'fruit': ['apple', 'orange', 'banana', 'peach']
             ,'color': ['red', 'orange', 'yellow', 'orangish']}

df = pd.DataFrame.from_dict(data_dict)

folder_name = 'new_folder'
file_name = 'new_file'

df_to_csv_with_timestamped(df, folder_name, file_name)