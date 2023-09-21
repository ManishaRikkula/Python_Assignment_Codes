#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import pandas as pd 


# __Performing the Calulation on one excel__

# In[50]:


df = pd.read_excel('13-07-2023_Region_mu_sigma_1.xlsx')
df.head(1)


# In[39]:


df.columns 


# In[51]:


# Melt the DataFrame for mu values
melted_mu_df = pd.melt(
    df,
    id_vars=["Rating"],
    value_vars=['NorthAfrica_mu','SouthAfrica_mu',
      'Europe_mu'],
    var_name="region",
    value_name="mu"
)

# Melt the DataFrame for sigma values
melted_sigma_df = pd.melt(
    df,
    id_vars=["Rating"],
    value_vars=[ 'NorthAfrica_sigma', 
       'SouthAfrica_sigma','Europe_sigma'],
    var_name="region",
    value_name="sigma"
)
# Extract the region from the 'region' column
melted_mu_df["region"] = melted_mu_df["region"].str.replace("_mu", "")
melted_sigma_df["region"] = melted_sigma_df["region"].str.replace("_sigma", "")
print(melted_mu_df.head(1))
print("-------------------")
print(melted_sigma_df.head(1))


# In[52]:


melted_mu_df


# In[41]:


# Create the 'Date'
melted_mu_df["Date"] = "13-07-2023"
melted_sigma_df["Date"] = "13-07-2023"
#Set date as index 
#melted_mu_df.set_index('Date', inplace = True)
#melted_sigma_df.set_index('Date', inplace = True)


# In[42]:


# Reorder columns for both DataFrames
melted_mu_df = melted_mu_df[["Date", "Rating", "region", "mu"]]
melted_sigma_df = melted_sigma_df[["Date", "Rating", "region", "sigma"]]

# Merge the two DataFrames based on Date, Rating, and region
output_df = pd.merge(melted_mu_df, melted_sigma_df, on=["Date", "Rating", "region"])
print(melted_mu_df.head(1))
print("-------------------")
print(melted_sigma_df.head(1))
print("-------------------")
print(output_df.head(1))


# In[43]:



output_df.set_index("Date", inplace=True)

# Print the resulting DataFrame
print(output_df)


# __Doing the above on all files at once__

# In[44]:


import os

folder_path = r'C:\Users\CF753NV\Downloads\Pyhton Training sessions\Pandas\Que3_files'
excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]
print(excel_files)


# In[31]:


df.head(1)


# In[45]:


# List of Excel file names
excel_file_names = [
    '01-02-2018_Region_mu_sigma_10.xlsx',
    '01-09-2027_Region_mu_sigma_5.xlsx',
    '03-04-2019_Region_mu_sigma_9.xlsx',
    '05-05-2021_Region_mu_sigma_7.xlsx',
    '12-07-2020_Region_mu_sigma_8.xlsx',
    '13-07-2023_Region_mu_sigma_1.xlsx',
    '14-03-2024_Region_mu_sigma_2.xlsx',
    '14-07-2022_Region_mu_sigma_6.xlsx',
    '19-08-2026_Region_mu_sigma_4.xlsx',
    '31-05-2025_Region_mu_sigma_3.xlsx'
]
 #Dict with  keys 'mu' and 'sigma', 
common_column_pattern = {
    'mu': '_mu',
    'sigma': '_sigma'
}

# Initialize an empty list to store the processed DataFrames
output_dfs = []

# Loop through each Excel file
for file_name in excel_file_names:
    # Extract date from the file name
    file_date = file_name.split("_")[0]

    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_name)

    # Melt the DataFrame for mu values
    melted_mu_df = pd.melt(
        df,
        id_vars=['Rating'],
        value_vars=[col for col in df.columns if common_column_pattern['mu'] in col],
        var_name='region',
        value_name='mu'
    )

    # Melt the DataFrame for sigma values
    melted_sigma_df = pd.melt(
        df,
        id_vars=['Rating'],
        value_vars=[col for col in df.columns if common_column_pattern['sigma'] in col],
        var_name='region',
        value_name='sigma'
    )

    # Extract the region from the 'region' column
    melted_mu_df['region'] = melted_mu_df['region'].str.replace(common_column_pattern['mu'], '')
    melted_sigma_df['region'] = melted_sigma_df['region'].str.replace(common_column_pattern['sigma'], '')

    # Set the 'Date' column to the extracted date
    melted_mu_df['Date'] = file_date
    melted_sigma_df['Date'] = file_date

    # Reorder columns for mu and sigma DataFrames
    melted_mu_df = melted_mu_df[['Date', 'Rating', 'region', 'mu']]
    melted_sigma_df = melted_sigma_df[['Date', 'Rating', 'region', 'sigma']]

    # Merge the two DataFrames based on Date, Rating, and region
    output_df = pd.merge(melted_mu_df, melted_sigma_df, on=['Date', 'Rating', 'region'])
    output_df.set_index('Date', inplace=True)

    # Append the processed DataFrame to the list
    output_dfs.append(output_df)

# Print the resulting DataFrames
for idx, output_df in enumerate(output_dfs):
    print(f'Processed DataFrame for file {excel_file_names[idx]}:')
    print(output_df)
    print('-------------------')


# In[46]:


# List of Excel file names
excel_file_names = [
    '01-02-2018_Region_mu_sigma_10.xlsx',
    '01-09-2027_Region_mu_sigma_5.xlsx',
    '03-04-2019_Region_mu_sigma_9.xlsx',
    '05-05-2021_Region_mu_sigma_7.xlsx',
    '12-07-2020_Region_mu_sigma_8.xlsx',
    '13-07-2023_Region_mu_sigma_1.xlsx',
    '14-03-2024_Region_mu_sigma_2.xlsx',
    '14-07-2022_Region_mu_sigma_6.xlsx',
    '19-08-2026_Region_mu_sigma_4.xlsx',
    '31-05-2025_Region_mu_sigma_3.xlsx'
]

# Initialize an empty list to store the processed DataFrames
output_dfs = []

# Loop through each Excel file
for file_name in excel_file_names:
    # Extract date from the file name
    file_date = file_name.split("_")[0]

    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_name)

    # Melt the DataFrame for mu values
    melted_mu_df = pd.melt(
        df,
        id_vars=['Rating'],
        value_vars=[col for col in df.columns if '_mu' in col,],
        var_name='region',
        value_name='mu'
    )

    # Melt the DataFrame for sigma values
    melted_sigma_df = pd.melt(
        df,
        id_vars=['Rating'],
        value_vars=[col for col in df.columns if '_sigma' in col],
        var_name='region',
        value_name='sigma'
    )

    # Extract the region from the 'region' column
    melted_mu_df['region'] = melted_mu_df['region'].str.replace('_mu', '')
    melted_sigma_df['region'] = melted_sigma_df['region'].str.replace('_sigma', '')

    # Set the 'Date' column to the extracted date
    melted_mu_df['Date'] = file_date
    melted_sigma_df['Date'] = file_date

    # Reorder columns for mu and sigma DataFrames
    melted_mu_df = melted_mu_df[['Date', 'Rating', 'region', 'mu']]
    melted_sigma_df = melted_sigma_df[['Date', 'Rating', 'region', 'sigma']]

    # Merge the two DataFrames based on Date, Rating, and region
    output_df = pd.merge(melted_mu_df, melted_sigma_df, on=['Date', 'Rating', 'region'])
    output_df.set_index('Date', inplace=True)

    # Append the processed DataFrame to the list
    output_dfs.append(output_df)

# Print the resulting DataFrames
for idx, output_df in enumerate(output_dfs):
    print(f'Processed DataFrame for file {excel_file_names[idx]}:')
    print(output_df)
    print('-------------------')


# In[47]:


num_rows = len(output_df)
print("Number of rows:", num_rows)


# In[53]:


file_date1 = file_name.split("_")[0]
file_date1

