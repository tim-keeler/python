'''
Author:             Tim Keeler
Created:            10-14-2022
Description:        Function to compare dataframes and output a dataframe capturing shape differences

folder_path_self:   Folder path to primary file 'self' (ex. "C:/Users/jdoe/my_project/self")
folder_path_other:  Folder path to file to compare 'self' against (ex. "C:/Users/jdoe/my_project/other")
file_name_list:     File names without extension passed as a list (ex. ["File1", "File2"])
file_extension:     Change to extension should also match applicable pd.read (csv, excel, etc.) parameter
'''


import pandas as pd

def compare_dataframe(folder_path_self, folder_path_other, file_name_list, file_extension=".csv"):
    
    # Column names that will be used as dataframe headers
    column_names = ["is_match", 
                    "file_name_list", 
                    "file_extension", 
                    "rows_self", 
                    "rows_other", 
                    "row_diff", 
                    "columns_self", 
                    "columns_other", 
                    "column_diff"]

    # Create empty datframe with headers only
    df = pd.DataFrame([], columns=column_names)

    # Loop through list of file names
    for f in range(len(file_name_list)):

        # Create full file path to self & other
        file_path_self = f"{folder_path_self}/{file_name_list[f]}{file_extension}"
        file_path_other = f"{folder_path_other}/{file_name_list[f]}{file_extension}"
        
        # Read data into dataframes
        df_self = pd.read_csv(file_path_self)
        df_other = pd.read_csv(file_path_other)

        # Variables that will be entered as rows into dataframe
        is_match = df_self.equals(df_other)
        rows_self = df_self.shape[0]
        rows_other = df_other.shape[0]
        row_diff = rows_self - rows_other
        columns_self = df_self.shape[1]
        columns_other = df_other.shape[1]
        column_diff = columns_self - columns_other

        # Create temp dataframe with values assinged to column index position
        df_temp = pd.DataFrame([{df.columns[0]:is_match, 
                                 df.columns[1]:file_name_list[f], 
                                 df.columns[2]:file_extension,
                                 df.columns[3]:rows_self, 
                                 df.columns[4]:rows_other, 
                                 df.columns[5]:row_diff, 
                                 df.columns[6]:columns_self,
                                 df.columns[7]:columns_other, 
                                 df.columns[8]:column_diff}])

        # Column to use for sorting and conditional formatting
        conditional_column = "is_match"
        # Append temp dataframe values to primary dataframe
        df = pd.concat([df, df_temp], ignore_index=True)
        # Sort dataframe by conditional column
        df = df.sort_values(by=conditional_column)

        # Function to conditionally format rows in dataframe
        def highlight_row(x):
            # Create copy of dataframe & preserve values
            df = x.copy()
            # Create True/False mask to determine formatting
            mask = df[conditional_column] == False
            df.loc[mask, :] = 'background-color: lightblue'
            df.loc[~mask,:] = 'background-color: ""'
            return df    
            
    return df.style.apply(highlight_row, axis=None)
