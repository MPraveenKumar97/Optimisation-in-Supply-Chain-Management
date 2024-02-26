create database SCM;

use SCM;

create table Pallet_SCM (
     Date text,
     CustName varchar(50) ,
     City text null,
     Region text null,
     State text null,
	Product_Code text null,
     Transaction_Type text null,
     QTY double null,
     WHName double null
 );
 
#Imported Dataset using Table Data Import Wizard in the existing table
 
#Total rows count
select count(*) from Pallet_SCM;

describe pallet_full_data; #Describe the structure of the "pallet_full_data" table


/*------Before Data Preprocessing-----*/

/*First Moment Business Decision*/

/*Mean*/

#------- Calculating the mean value for QTY--------
SELECT AVG (QTY) AS mean_value FROM Pallet_SCM;


/*Median*/

# Median for QTY
SELECT AVG(QTY) AS median
FROM (
    SELECT QTY,
            ROW_NUMBER() OVER (ORDER BY QTY) AS row_num,
            COUNT(*) OVER () AS total_count
    FROM Pallet_SCM
) AS median_subquery
WHERE row_num BETWEEN (total_count + 1) / 2 AND total_count / 2 + 1;


/*Mode*/

###MODE
##CustName mode
(SELECT 'CustName' AS parameter,CustName AS mode, COUNT(CustName) AS frequency
FROM Pallet_SCM
GROUP BY CustName 
ORDER BY frequency DESC
LIMIT 1)
UNION
##City 
(SELECT 'City' AS parameter,City AS mode, COUNT(City ) AS frequency
FROM Pallet_SCM
GROUP BY City 
ORDER BY frequency DESC
LIMIT 1)
UNION
## Region 
(SELECT 'Region' AS paramter,Region AS mode, COUNT(Region ) AS frequency
FROM Pallet_SCM
GROUP BY Region  
ORDER BY frequency DESC
LIMIT 1)
UNION
##State
(SELECT 'State' AS  paramter,State AS mode, COUNT(State ) AS frequency
FROM Pallet_SCM
GROUP BY State  
ORDER BY frequency DESC
LIMIT 1)
UNION
##ProductCode 
(SELECT 'Product_Code'  AS paramter,Product_Code as mode, COUNT(Product_Code) AS frequency
FROM Pallet_SCM
GROUP BY Product_Code  
ORDER BY frequency DESC
LIMIT 1)
UNION 
##TransactionType 
(SELECT 'Transaction_Type' AS paramter,Transaction_Type as mode, COUNT(Transaction_Type) AS frequency
FROM Pallet_SCM
GROUP BY Transaction_Type  
ORDER BY frequency DESC
LIMIT 1)
UNION
##QTY
(SELECT 'QTY' AS paramter,QTY as mode, COUNT(QTY) AS frequency
FROM Pallet_SCM
GROUP BY QTY  
ORDER BY frequency DESC
LIMIT 1)
UNION
##WHName
(SELECT 'WHName' AS paramter, WHName AS mode, COUNT(WHName) AS frequency
FROM Pallet_SCM
GROUP BY WHName 
ORDER BY frequency DESC
LIMIT 1); #Calculate the mode for various columns


/*Second Moment Business Decision*/

/*Variance*/

#------- Calculating the Variance for QTY--------
SELECT VARIANCE(QTY) FROM Pallet_SCM;


/*Standard Deviation*/

#------- Calculating the Standard Deviation value for QTY--------
SELECT STDDEV(QTY) AS standard_deviation FROM Pallet_SCM;


/*Range with Min & Max*/

-- Range for Wind_speed
SELECT Min(QTY), Max(QTY), Max(QTY) - Min(QTY) AS range_QTY FROM Pallet_SCM;


/*Third Moment Business Decision*/

/*Skewness*/

#------- Skewness value for Wind_speed--------
SELECT 3 * AVG(POW((QTY - (SELECT AVG(QTY) FROM Pallet_SCM)) / (SELECT STDDEV(QTY) FROM Pallet_SCM), 3))
  AS skewness FROM Pallet_SCM;
  
  
/*Fourth Moment Business Decision*/

/*Kurtosis*/

#------- kurtosis value for Wind_speed--------
SELECT AVG(POW((QTY - (SELECT AVG(QTY) FROM Pallet_SCM)) / (SELECT STDDEV(QTY) FROM Pallet_SCM), 4))
AS kurtosis FROM Pallet_SCM;


################ DATA PREPROCESSING(BEFORE) #################
#finding whether there is any null values present
###NULL VALUES COUNT    
select count(*) from Pallet_SCM where Date is null
UNION
select count(*) from Pallet_SCM where CustName is null
UNION
select count(*) from Pallet_SCM where City is null
UNION
select count(*) from Pallet_SCM where Region is null
UNION
select count(*) from Pallet_SCM where State is null
UNION
select count(*) from Pallet_SCM where Product_Code is null
UNION
select count(*) from Pallet_SCM where Transaction_Type is null
UNION
select count(*) from Pallet_SCM where QTY is null
UNION
select count(*) from Pallet_SCM where WHName is null; #Count null values in different columns

###HANDLING DUPLICATES
####DUPLICATE VALUES COUNT
select Date,CustName,City,Region,State,Product_Code,Transaction_Type,QTY,WHName, count(*) as duplicate_count
from Pallet_SCM
group by Date,CustName,City,Region,State,Product_Code,Transaction_Type,QTY,WHName
having count(*) > 1; #Identify and count duplicate rows based on certain columns

####OUTLIERS COUNT USING Z-SCORE METHOD
#QTY outlier count
SELECT(
    COUNT(CASE WHEN ABS((QTY - (SELECT mean_value FROM (SELECT AVG(QTY) AS mean_value
    FROM Pallet_SCM) AS mean_stats)) / (SELECT std_dev FROM (SELECT STDDEV(QTY) AS std_dev FROM Pallet_SCM) 
    AS std_dev_stats)) > 3 THEN 1 END)) AS outlier_count
FROM Pallet_SCM; #Identify outliers using Z-score method for the 'QTY' column

#-------------------------------------------------------DATA CLEANING PROCESS-----------------------------------------------
################ DATA PREPROCESSING(AFTER) #################
create table cleaned_Pallet as select * from Pallet_SCM;  #Create a copy of the table pallet_full_data
select * from cleaned_Pallet; # Attempt to select all from the dropped table
select count(*) from cleaned_Pallet;  #Attempt to count rows in the dropped table

####DROP DUPLICATES
create table temp_pallet_full_data as select distinct * from cleaned_Pallet; #Create a temporary table to hold distinct values from pallet_full_data_clean


truncate table cleaned_Pallet;  #Truncate the original clean table to remove all its data

insert into cleaned_Pallet
select * from temp_pallet_full_data; #Insert the distinct values back into the cleaned table

drop table temp_pallet_full_data; #Drop the temporary table

#After EDA

----- Four Moments of Business Decision -----

/*First Moment Business Decision*/

/*Mean*/

#------- Calculating the mean value for QTY--------
SELECT AVG (QTY) AS mean_value FROM cleaned_Pallet;


/*Median*/

# Median for QTY
SELECT AVG(QTY) AS median
FROM (
    SELECT QTY,
            ROW_NUMBER() OVER (ORDER BY QTY) AS row_num,
            COUNT(*) OVER () AS total_count
    FROM cleaned_Pallet
) AS median_subquery
WHERE row_num BETWEEN (total_count + 1) / 2 AND total_count / 2 + 1;


/*Mode*/

###MODE
##CustName mode
(SELECT 'CustName' AS parameter,CustName AS mode, COUNT(CustName) AS frequency
FROM cleaned_Pallet
GROUP BY CustName 
ORDER BY frequency DESC
LIMIT 1)
UNION
##City 
(SELECT 'City' AS parameter,City AS mode, COUNT(City ) AS frequency
FROM cleaned_Pallet
GROUP BY City 
ORDER BY frequency DESC
LIMIT 1)
UNION
## Region 
(SELECT 'Region' AS paramter,Region AS mode, COUNT(Region ) AS frequency
FROM cleaned_Pallet
GROUP BY Region  
ORDER BY frequency DESC
LIMIT 1)
UNION
##State
(SELECT 'State' AS  paramter,State AS mode, COUNT(State ) AS frequency
FROM cleaned_Pallet
GROUP BY State  
ORDER BY frequency DESC
LIMIT 1)
UNION
##ProductCode 
(SELECT 'Product_Code'  AS paramter,Product_Code as mode, COUNT(Product_Code) AS frequency
FROM cleaned_Pallet
GROUP BY Product_Code  
ORDER BY frequency DESC
LIMIT 1)
UNION 
##TransactionType 
(SELECT 'Transaction_Type' AS paramter,Transaction_Type as mode, COUNT(Transaction_Type) AS frequency
FROM cleaned_Pallet
GROUP BY Transaction_Type  
ORDER BY frequency DESC
LIMIT 1)
UNION
##QTY
(SELECT 'QTY' AS paramter,QTY as mode, COUNT(QTY) AS frequency
FROM cleaned_Pallet
GROUP BY QTY  
ORDER BY frequency DESC
LIMIT 1)
UNION
##WHName
(SELECT 'WHName' AS paramter, WHName AS mode, COUNT(WHName) AS frequency
FROM cleaned_Pallet
GROUP BY WHName 
ORDER BY frequency DESC
LIMIT 1); #Calculate the mode for various columns

/*Second Moment Business Decision*/

/*Variance*/

#------ Calculating the Variance for QTY--------
SELECT VARIANCE(QTY) FROM cleaned_Pallet;


/*Standard Deviation*/

#------- Calculating the Standard Deviation value for QTY--------
SELECT STDDEV(QTY) AS standard_deviation FROM cleaned_Pallet;


/*Range with Min & Max*/

-- Range for Wind_speed
SELECT Min(QTY), Max(QTY), Max(QTY) - Min(QTY) AS range_QTY FROM cleaned_Pallet;


/*Third Moment Business Decision*/

/*Skewness*/

#------- Skewness value for Wind_speed--------
SELECT 3 * AVG(POW((QTY - (SELECT AVG(QTY) FROM cleaned_Pallet)) / (SELECT STDDEV(QTY) FROM cleaned_Pallet), 3))
  AS skewness FROM cleaned_Pallet;
  
  
/*Fourth Moment Business Decision*/

/*Kurtosis*/

#------- kurtosis value for Wind_speed--------
SELECT AVG(POW((QTY - (SELECT AVG(QTY) FROM cleaned_Pallet)) / (SELECT STDDEV(QTY) FROM cleaned_Pallet), 4))
AS kurtosis FROM cleaned_Pallet;

select * from cleaned_Pallet;