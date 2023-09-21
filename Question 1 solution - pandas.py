#!/usr/bin/env python
# coding: utf-8

# Questions
# 1. Which region is delivering maximum orders?
# 2. Check the performance of all the managers and give rating to each manager start rating from A as top manager
# 3. Remove special characters, fill missing values, remove duplicate rows, convert OrderDate column to datetime
# 4. Calculate the number of days from todays date and check how old the order is?
# 5. create a Pivot table and count the manager wise sale and mean value of sale amount. 
# 6. create a Pivot table and find the total sale amount region wise, manager wise, sales man wise where Manager = "Douglas"
# 7. keep those rows which are having atmost two NaNs
# 8. Group on Region, Manager, SalesMan, Item then sort sum of Sale_amt within the group
# 9. split the dataframe in the groups based on region and set manager, salesman and item column values into list of values
# 10. Check if OrderDate is business day (weekday) or not

# In[9]:


import numpy as np
import pandas as pd
## Read the entire Excel file into a DataFrame
df = pd.read_excel('data.xlsx',sheet_name='Que')
df.head(2)
df.columns


# In[91]:


#1.Which region is delivering maximum orders
print(df.groupby('Region')['Units'].agg(['sum', 'max', 'min']))
print("Central region is delivering highest orders- 1199")


# In[118]:


#2.Check the performance of all the managers and give rating to each manager start rating from A as top manager
df1=df.groupby(['Manager'])['Units'].agg(['sum']).sort_values(by='sum',ascending=False)
df1['Ratings']=["A","B","C","D"]
df1


# In[101]:


#3.Remove special characters, fill missing values, remove duplicate rows, convert OrderDate column to datetime

# Remove duplicate rows
df.drop_duplicates(inplace=True)
#df.drop_duplicates(subset=['col1', 'col2'], inplace=True)

# Convert OrderDate column to datetime
from datetime import datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%Y-%m-%d')


# In[100]:


nan_values = df.isna()  # or df.isnull()
nan_counts = df.isna().sum() #no.of nan count in each coulmn
#has_nan = df.isna().any().any()  # Returns True if any NaN value exists
pd.isna(df)
print(nan_counts)
# There are no nan values as this gives False( pd.isna(df))for all the data points.


# In[102]:


#4. Calculate the number of days from todays date and check how old the order is?
# Convert 'OrderDate' column to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
# Calculate the number of days from today's date
current_date = datetime.now().date()
df['DaysSincelastOrder'] = (current_date - df['OrderDate'].dt.date).dt.days  #df['OrderDate'].dt.date: This extracts the date part from the 'OrderDate' column, resulting in a Series containing only the dates (without the time component).

# Print the DataFrame with the new column
print(df,current_date)


# In[ ]:


# Create a pivot table
pivot_table = pd.pivot_table(
    df,                      # DataFrame
    values='ValueColumn',    # Column to aggregate
    index='IndexColumn',     # Rows (index) or the rows you want in pivot table 
    columns='ColumnToPivot', # Columns or the columns you want in pivot table 
    aggfunc='sum'            # Aggregation function on values  (e.g., 'sum', 'mean', 'count', etc.)
)


# In[57]:


df.columns


# In[105]:


#5.##create a Pivot table and count the manager wise sale and mean value of sale amount.
table1=pd.pivot_table(df, values="Units", index=["Manager"], aggfunc={'Units': ['sum','mean']} )
table1.columns = [ 'Mean of Units/Sales' ,'Sum of Sales Units']
print(table1)


# In[106]:


#6.create a Pivot table and find the total sale amount region wise, manager wise, sales man wise where Manager = "Douglas"

filtered_df = df[df['Manager'] == 'Douglas']

# Create the pivot table
pivot_table = pd.pivot_table(
    filtered_df,
    values='Units', 
    index=['Region', 'Manager','SalesMan' ],  # Rows (index)
    aggfunc='sum' 
)

# Print the pivot table
print(pivot_table)


# In[107]:


filtered_df


# In[108]:


#7.keep those rows which are having atmost two NaNs

max_nan_threshold = 2
filtered1_df = df.dropna(thresh=len(df.columns) - max_nan_threshold + 1)
# Print the filtered DataFrame
print(filtered1_df)


# In[112]:


#8.Group on Region, Manager, SalesMan, Item then sort sum of Sale_amt within the group
grouped = df.groupby(['Region', 'Manager', 'SalesMan', 'Item'])['Sale_amt'].sum()
#print(grouped,df.columns)
# Convert the grouped Series back to a DataFrame
result_df = grouped.reset_index()
# Sort the DataFrame by the sum of Sale_amt within each group
sorted_df = result_df.sort_values(by='Sale_amt', ascending=False)

# Print the sorted DataFrame
#print(result_df)
print(sorted_df)


# In[111]:


group = df.groupby(['Region', 'Manager', 'SalesMan', 'Item'])['Sale_amt'].agg(['sum']).sort_values(by='sum', ascending=False)
print(group)
#df.groupby(['col1'])['col2'].agg(['sum']).sort_values(by='sum',ascending=False)


# In[121]:


#9.split the dataframe in the groups based on region and set manager, salesman and item column values into list of values

grouped1 = df.groupby('Region').apply(lambda x: {
    'Manager': x['Manager'].tolist(),
    'SalesMan': x['SalesMan'].tolist(),
    'Item': x['Item'].tolist()
}).reset_index()

# Print the result
print(grouped1)


# In[120]:


#10.Check if OrderDate is business day (weekday) or not.
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Check if each date is a business day

df['IsBusinessDay'] = df['OrderDate'].dt.weekday < 5 #.weekday: This is a property accessed using the .dt accessor. It returns the day of the week as an integer, where Monday is 0 and Sunday is 6.

# Print the DataFrame
print(df)


# In[119]:


true_count = df['IsBusinessDay'].sum()
print(true_count)


# In[11]:


df2 = ['Sale_amt','OrderDate', 'Region', 'Manager', 'SalesMan', 'Item', 'Units',
       'Unit_price' ]
df3 =df[df2]
df3.head(1)


# In[12]:


df4 =df[['Sale_amt','OrderDate', 'Region', 'Manager', 'SalesMan', 'Item', 'Units',
       'Unit_price']]
df4.head(1)


# In[17]:


df['Region'].unique()

