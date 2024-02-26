# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:01:20 2023

@author: prave
"""

###Using sql to python database connectivity to load the cleaned dtaset from sql database.
####pip install mysql-connector-python
import mysql.connector
import pandas as pd


# Replace these values with your MySQL server details
host = "127.0.0.1"
user = "user3"
password = "user3"
database = "SCM"

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

#Fetching data from 'Pallet_SCM' table in the 'SCM' database
cursor.execute("SELECT * FROM Pallet_SCM")
result = cursor.fetchall()

#Converting the fetched data into a Pandas DataFrame
columns = [i[0] for i in cursor.description]
df = pd.DataFrame(result, columns=columns)

#Before Data Preprocessing

#Four moments of business decision

#######Measures of Central Tendency / First moment business decision#######

import pandas as pd

#Mean

#QTY
df.QTY.mean()

#Median
#QTY
df.QTY.median()

#Mode
df.Date.mode()
df.CustName.mode()
df.City.mode()
df.Region.mode()
df.State.mode()
df.Product_Code.mode()
df.Transaction_Type.mode()
df.QTY.mode()
df.WHName.mode()

#######Measures of Dispersion / Second moment business decision########

# variance
df.QTY.var()

# standard deviation
df.QTY.std()

#Range
QTY_range= max(df.QTY) - min(df.QTY)
QTY_range

########Third Moment of Business Decision#######
#Skewness
df.QTY.skew()

########Fourth moment business decision########
#Kurtosis
df.QTY.kurt()

#------------------------------------------------------------------------------

#identifying duplicates

duplicates = df.duplicated() #The 'duplicate' variable identifies duplicates in the data.
duplicates.unique() #Data will be of true or false (True if data duplicate is present else false)
duplicates.sum() ## Output 'sum()' indicates the count of duplicates found.16938 Duplicates were present

#Count of null values
df.isna().sum()

#OUTLERS COUNT#
#using IQR method 
# QTY
IQR = df['QTY'].quantile(0.75) - df['QTY'].quantile(0.25) #Using the Interquartile Range (IQR) method to identify outliers in the 'QTY' column.
# Define lower and upper bounds
lower_limit = df['QTY'].quantile(0.25) - 1.5 * IQR
lower_limit
upper_limit = df['QTY'].quantile(0.75) + 1.5 * IQR
upper_limit # Calculating lower and upper bounds for outlier detection.

# Count outliers
outliers_count = len(df[(df['QTY'] < lower_limit) | (df['QTY'] > upper_limit)])
outliers_count ## Counting the number of outliers found based on these bounds.

# Display the result
print(result)

df
df.dtypes
df.head()
df.tail()
df.describe()
##########################DATA PREPROCESSING################################
### Dropping the duplicates
data1=df.drop_duplicates() #Removing duplicates using 'drop_duplicates()' method and storing the cleaned data in 'data1'.
print(data1)


## Rechecking for duplicates in the cleaned data and counting them.
duplicate=data1.duplicated()
duplicate.unique() #Data will be of true or false (True if data duplicate is present else false)
duplicate.sum()

###################GRAPHICAL REPRESENTATION(univariant,Bivariant,Multivaraiant)#############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#UNIVARIANT
#QTY
sns.boxplot(data1.QTY)
plt.title('QTY Box Plot')

#HISTOGRAM 
#QTY
plt.hist(data1.QTY,bins=20,color='purple') 
#Plotting histogram with KDE curve
sns.histplot(data1.QTY,bins=20,kde=True, color='purple')
plt.xlabel('QTY')
plt.title('QTY histogram')
#QTY Histogram Insights-->
#The range of QTY values seems to be quite large, as the x-axis extends from -400 to 600.
#The interquartile range (IQR) could be a useful measure to quantify the spread of the central 50% of data points.
#The histogram clearly shows a right skew, with a longer tail extending towards higher QTY values.
 
 
#DISTRIBUTION PLOT 
sns.distplot(data1.QTY)
plt.title('DISTRIBUTION Plot  QTY')
##QTY Distribution plot Insights-->
#Wide range (-600 to 600) indicates large spread in quantity values.
#Right skew evident with longer tail towards higher QTY values.

#BARPLOT
plt.bar(height=data1.QTY,x = np.arange(1,64025, 1))
plt.title('Bar Plot  QTY')

#DENSITY PLOT
sns.kdeplot(data1.QTY)
plt.title('Density Plot  QTY')

#SCATTER PLOT
#CustName Vs QTY
plt.scatter(x=data1.CustName,y=data1.QTY)
plt.xlabel('CustName')
plt.ylabel('QTY')
plt.title('Scatter Plot CustName Vs QTY')

# City Vs QTY
plt.scatter(x=data1. City,y=data1.QTY)
plt.xlabel(' City')
plt.ylabel('QTY')
plt.title('Scatter Plot City Vs QTY')

#Region Vs QTY
plt.scatter(x=data1.Region,y=data1.QTY)
plt.xlabel('Region')
plt.ylabel('QTY')
plt.title('Scatter Plot Region Vs QTY')

#State Vs QTY
plt.scatter(x=data1.State,y=data1.QTY)
plt.xlabel('State')
plt.ylabel('QTY')
plt.title('Scatter Plot State Vs QTY')

#ProductCode Vs QTY
plt.scatter(x=data1.Product_Code,y=data1.QTY)
plt.xlabel('Product_Code')
plt.ylabel('QTY')
plt.title('Scatter Plot Product_Code Vs QTY')

#TransactionType Vs QTY
plt.scatter(x=data1.Transaction_Type,y=data1.QTY)
plt.xlabel('Transaction_Type')
plt.ylabel('QTY')
plt.title('Scatter Plot TransactionType Vs QTY')

#  WHName  Vs QTY
plt.scatter(x=data1.Transaction_Type,y=data1.QTY)
plt.xlabel('  WHName ')
plt.ylabel('QTY')
plt.title('Scatter Plot   WHName  Vs QTY')


# Integration of 'CustName' and 'QTY' for supply chain optimization
# Assuming 'CustName' and 'QTY' are available in another dataset or the same 'data' DataFrame
# Visualizing 'CustName' and 'QTY' data
plt.figure(figsize=(8, 5))
plt.scatter(df['CustName'], df['QTY'],color='Lightpink',alpha=0.7)
plt.xlabel('Customer Name')
plt.ylabel('Quantity')
plt.title('Quantity ordered by Customer')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability if needed
plt.tight_layout()
plt.show()

# Sweetviz
###########
#pip install sweetviz
import sweetviz as sv

s = sv.analyze(data1)
s.show_html()


# Autoviz
###########
# pip install autoviz
from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
a = av.AutoViz(r"C:\Users\prave\Desktop\Data Analytics\Project Supply Chain Management\Dataset\pallet_Masked_fulldata.xlsx", chart_format = 'html')

import os
os.getcwd()

# If the dependent variable is known:
a = av.AutoViz(r"C:\Users\prave\Desktop\Data Analytics\Project Supply Chain Management\Dataset\pallet_Masked_fulldata.xlsx", depVar = 'QTY') # depVar - target variable in your dataset


# D-Tale
########

# pip install dtale   # In case of any error then please install werkzeug appropriate version (pip install werkzeug==2.0.3)
import dtale
import pandas as pd

df = pd.read_csv(r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\pallet_Masked_fulldata.csv")

d = dtale.show(df)
d.open_browser()
