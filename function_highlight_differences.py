'''
Author:             Tim Keeler
Created:            10-14-2022
Description:        Function to compare dataframes of equal size and highlight differences

folder_path_self:   Folder path to primary file 'self' (ex. "C:/Users/jdoe/my_project/self")
folder_path_other:  Folder path to file to compare 'self' against (ex. "C:/Users/jdoe/my_project/other")
file_name:          Takes a single file name without extension (ex. "File1")
file_extension:     Change to extension should also match applicable pd.read (csv, excel, etc.) parameter
'''


import pandas as pd

def highlight_differences(folder_path_self, folder_path_other, file_name, file_extension=".csv"):

    # Create full file path to self & other
    file_path_self = f"{folder_path_self}/{file_name}{file_extension}"
    file_path_other = f"{folder_path_other}/{file_name}{file_extension}"

    # Read data into dataframes
    df_self = pd.read_csv(file_path_self)
    df_other = pd.read_csv(file_path_other)

    try:
        if df_self.equals(df_other):
            print("No differences between dataframes")
        else:
            # Create True/False mask to flag differences
            df_mask = df_self.compare(df_other, keep_shape=True).notnull().astype('int')
            df_other = df_self.compare(df_other, keep_shape=True, keep_equal=True)
            
            # Function to conditionally format differences in dataframe 
            def apply_color(x):
                colors = {1: 'lightblue', 0: 'white'}
                return df_mask.applymap(lambda val: 'background-color: {}'.format(colors.get(val,'')))
            
            return df_other.style.apply(apply_color, axis=None)
    except:
        print("Dataframes must be of equal shape")