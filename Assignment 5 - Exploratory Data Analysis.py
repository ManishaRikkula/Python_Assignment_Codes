#!/usr/bin/env python
# coding: utf-8

# *Difficulty level -  Easy*
# 
# Dataset: You are provided with a dataset named "sales_data.csv," which contains information about sales transactions. The dataset includes columns such as "Date," "Product," "Quantity," "Price," and "Customer."
# 
# Include comments and explanations in your code to make it clear and understandable.
# Provide appropriate titles and labels for your plots
# 
# Tasks:
# 1 Load the dataset using Pandas and display the first few rows to understand its structure.
# 2 Perform data cleaning:
#     •	Check for missing values and decide on a strategy to handle them.
#     •	Identify and remove any duplicate rows.
# 3 Compute and display the following summary statistics:
#     •	Mean, median, and standard deviation of the "Quantity" and "Price" columns.
#     •	Total sales revenue (computed as the sum of Quantity * Price).
# 4 Visualize the data:
#     •	Create a histogram of the "Quantity" column to understand the distribution of sales quantities.
#     •	Generate a scatter plot of "Price" vs. "Quantity" to explore any potential relationships.
# 5 Perform categorical analysis:
#     •	Group the data by "Product" and compute the total quantity sold and average price for each product.
#     •	Visualize the product-wise sales using a bar chart.
# 6 Identify outliers:
#     •	Use the z-score method to detect potential outliers in the "Price" column.
#     •	Visualize the outliers using a box plot.
# 7 Additional Analysis:
#     •	Calculate the weekly sales by aggregating the data based on the "Date" column.
#     •	Visualize the weekly sales trend over time using a line plot.
# 

# In[36]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Task 1: Load the dataset and display the first few rows to understand its structure.
df = pd.read_csv( "sales_data.csv")
#print(df.info())
df.head()


# In[134]:


# Task 2:  Perform data cleaning: • Check for missing values and decide on a strategy to handle them.
#• Identify and remove any duplicate rows.
print("Null Value Count :", df.isnull().sum()) # There are no null values in the dataset.
print("Unqiue Values number", df.nunique()) # No. of unique elements in each column (df has 18289 rows × 6 columns)
duplicate_rows = df[df.duplicated(keep='first')] # ``first`` : Mark duplicates as ``True`` except for the first occurrence.
print(duplicate_rows.count()) #Gives the duplicate rows count
df.drop(duplicate_rows.index , inplace = True ) #Drops duplicate rows. (The df has reduced to 18267 rows × 6 columns)
df


# In[135]:


#Task 3: Compute and display the following summary statistics:
#• Mean, median, and standard deviation of the "Quantity" and "Price" columns.
#• Total sales revenue (computed as the sum of Quantity * Price)
print(df[['Quantity','Price']].describe().loc[['mean', '50%', 'std']])
Total_sales_revenue =sum(df.Quantity * df.Price)
print("Total Sales Revenue:", Total_sales_revenue)


# In[150]:


#Task 4 :   Visualize the data: 
#• Create a histogram of the "Quantity" column to understand the distribution of sales quantities.
#• Generate a scatter plot of "Price" vs. "Quantity" to explore any potential relationships.
plt.figure(figsize=(6, 3)) # fig size
# histogram of the "Quantity" column
plt.subplot(1, 2, 1)
sns.histplot(df['Quantity'] ,color='yellow',alpha=0.5)
plt.title("Distribution of Sales Quantities")
plt.xlabel("Quantity")
plt.ylabel("Frequency")

# Generate a scatter plot of "Price" vs. "Quantity"
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='Quantity', y='Price',color='red',alpha=0.5)
plt.title("Scatter Plot of Price vs. Quantity")
plt.xlabel("Quantity")
plt.ylabel("Price")

plt.tight_layout()  # To ensure proper spacing
plt.show()


# In[144]:


#Task 5 :  Perform categorical analysis:
#• Group the data by "Product" and compute the total quantity sold and average price for each product.
#• Visualize the product-wise sales using a bar chart.

df2= df.groupby('Product')[['Quantity','Price']].agg({'Quantity':'sum' ,'Price':'mean'}).reset_index()
df2.rename(columns={'Quantity': 'Total Quantity Sold', 'Price': 'Average Price'}, inplace = True)
print(df2.head())
sns.barplot(data=df2, x='Product', y='Total Quantity Sold',color='pink')
plt.title("Scatter Plot of Price vs. Quantity")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=90, ha='right')

plt.tight_layout()
plt.show()


# In[4]:


#Task 6 :6 Identify outliers: 
#• Use the z-score method to detect potential outliers in the "Price" column. 
#• Visualize the outliers using a box plot.
from sklearn.preprocessing import StandardScaler #importing StandardScaler class
sc = StandardScaler() # create sc object of StandardScaler class
z_score = sc.fit_transform(df[['Price']]) #This gives z_score array of Price coulmn
z_score_threshold = 2
# Identify potential outliers using the Z-score threshold
potential_outliers = df[abs(z_score) > z_score_threshold]

# Print potential outliers
print("Potential Outliers:")
print(potential_outliers.head(2))
print("-------")
print(potential_outliers.count())
print("-------")
print(df['Price'].describe().loc[['mean','min','max']])
# Visualize outliers using a box plot
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Price'], palette='viridis')
plt.title("Box Plot of Price with Potential Outliers")
plt.xlabel("Price")
plt.ylabel("Value")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.xticks(rotation=45, ha='right')


# In[5]:


potential_outliers.describe()


# In[6]:


#Task 7 :Additional Analysis: 
#• Calculate the weekly sales by aggregating the data based on the
#• Visualize the weekly sales trend over time using a line plot.
from datetime import date
df['Order Date'] = pd.to_datetime(df['Order Date'])
weekly_sales = df.resample('W-Mon', on='Order Date').sum()    
weekly_sales 


# In[191]:


weekly_sales['Quantity'].sum()


# In[192]:


df['Quantity'].sum()


# **Question 2**

# *Difficulty level - Medium*
# Analyse the given dataset and come up with an analysis using different metrics and plots to answer the questions below:
# 
# After each question intsert a code to justify your answer and also write down the answer in the text box itself.
# 
# 

# Q1: What does the customer rating look like and is it skewed?
# 
# Answer - The rating (4-10) has count distributed evenly, showing no skew from the histogram below. 

# In[35]:


# <Inset Code Here>
data = pd.read_csv( "supermarket_sales.csv")
print(data.info())
data.head()
sns.histplot(data['Rating'])
plt.show
print('Skew :', round(data['Rating'].skew(), 2))
plt.figure(figsize = (7, 4))


# Q2: Is there any difference in aggregate sales across branches?
# 
# A- yes, Branch A has highest sales followed by C and B.

# In[30]:


# <Inset Code Here>
print(data.columns)
data1=data.groupby(['Branch'])['Quantity'].agg('sum').reset_index()
data1.columns = ['Branch','Aggregate_Sales']
data1['Aggregate_Sales'].sort_values().inplace=True
data1


# Question 3: Which is the most pouplar payment method used by customers?
# 
# A- Ewallet is the most pouplar payment method used by customers.

# In[38]:


# <Inset Code Here>
print(data['Payment'].value_counts())
sns.countplot(data['Payment'])


# Q4: Does gross income affect the ratings that the customers provide?
# 
# A- There was no relation observed from the scatterplot below, however as the gross income increases the number of people who provides rating has fallen.

# In[224]:


# <Inset Code Here>
plt.figure(figsize=(6, 4))
sns.scatterplot(data=data,x='gross income',y='Rating')
plt.show()


# Q5: Which branch is the most profitable?
# 
# A-Branch C is the most profitable.

# In[43]:


# <Inset Code Here>
data['gross profit'] = data['gross margin percentage']*data['Total']
data3=data.groupby(['Branch'])['gross profit'].agg('sum').reset_index()
print(data3)
sns.boxplot(x=data['Branch'], y=data['gross income'])


# Q6: Is there any time trend in gross income?
# 
# A- No particular time trend is observed except for some days when the gross income is pretty high or pretty low. Overall it remains at a certain average level.

# In[264]:


# <Inset Code Here>
from datetime import date
data['Date'] = pd.to_datetime(data['Date'])
plt.figure(figsize = (14, 7))
sns.lineplot(y="gross income", x="Date", data=data)
plt.show()


# In[238]:


data['gross income'].isna().sum()


# Q7: Which product line generates most income?
# 
# A-Sports and travel generates most income.

# In[50]:


# <Inset Code Here>
data4=data.groupby(['Product line'])['gross income'].agg('sum').reset_index()
data4['gross income'].sort_values().inplace=True
print(data4)


# Q8: Show the correlation between all variable.

# In[28]:


# <Inset Code Here>
sns.heatmap(np.round(data.corr(),3), annot=True)

