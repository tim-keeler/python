'''
Author:             Tim Keeler
Created:            10-14-2022
Description:        Function to extract row differences between two dataframes

folder_path_self:   Folder path to primary file 'self' (ex. "C:/Users/jdoe/my_project/self")
folder_path_other:  Folder path to file to compare 'self' against (ex. "C:/Users/jdoe/my_project/other")
file_name:          Takes a single file name without extension (ex. "File1")
file_extension:     Change to extension should also match applicable pd.read (csv, excel, etc.) parameter
'''


import pandas as pd

def extract_row_differences(folder_path_self, folder_path_other, file_name, file_extension=".csv"):
    

    # Create full file path to self & other
    file_path_self = f"{folder_path_self}/{file_name}{file_extension}"
    file_path_other = f"{folder_path_other}/{file_name}{file_extension}"

    # Read data into dataframes
    df_self = pd.read_csv(file_path_self)
    df_other = pd.read_csv(file_path_other)

    compare_column = "Index"            # Column used to align & compare dataframes
    rows_self = df_self.shape[0]        # Number of rows in self
    rows_other = df_other.shape[0]      # Number of rows in other
    row_diff = rows_self - rows_other   # Row difference between self & other

    if row_diff < 0:
        # Other has more rows than self
        df_common = df_other.merge(df_self,on=[compare_column,compare_column])
        return df_other[(~df_other[compare_column].isin(df_common[compare_column])) & (~df_other[compare_column].isin(df_common[compare_column]))]
    elif row_diff > 0:
        # Self has more rows than other
        df_common = df_self.merge(df_other,on=[compare_column,compare_column])
        return df_self[(~df_self[compare_column].isin(df_common[compare_column])) & (~df_self[compare_column].isin(df_common[compare_column]))]
    else:
        return print("No differences to between dataframes")
