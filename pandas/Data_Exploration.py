#Descriptive and summary statistics

import pandas as pd
df = pd.read_csv("data/heart_disease.csv")
df
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes
# ...	...	...	...	...	...	...	...	...
# 298	57	Male	0	140	241	123	0.2	No
# 299	45	Female	3	110	264	132	1.2	No
# 300	68	Female	0	144	193	141	3.4	No
# 301	57	Female	0	130	131	115	1.2	No
# 302	57	Male	1	130	236	174	0.0	No
# 303 rows × 8 columns

# The describe() method displays the descriptive statistics about a DataFrame including the mean, median, min,
# max and quartile values for each numerical column.
df.describe()
# age	chest_pain	rest_bp	chol	max_hr	st_depr
# count	303.000000	303.000000	303.000000	303.000000	303.000000	303.000000
# mean	54.366337	0.966997	131.623762	246.264026	149.646865	1.039604
# std	9.082101	1.032052	17.538143	51.830751	22.905161	1.161075
# min	29.000000	0.000000	94.000000	126.000000	71.000000	0.000000
# 25%	47.500000	0.000000	120.000000	211.000000	133.500000	0.000000
# 50%	55.000000	1.000000	130.000000	240.000000	153.000000	0.800000
# 75%	61.000000	2.000000	140.000000	274.500000	166.000000	1.600000
# max	77.000000	3.000000	200.000000	564.000000	202.000000	6.200000


# You can also call individual methods on a column (Series object) to get a particular descriptive value
# for that column:
df["age"].min()  # 29
# df["chol"].mean()


# Exercise 1
# Display the average values for max_hr and rest_bp.

# Import the data
import pandas as pd
df = pd.read_csv("data/heart_disease.csv")
df
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes
# ...	...	...	...	...	...	...	...	...
# 298	57	Male	0	140	241	123	0.2	No
# 299	45	Female	3	110	264	132	1.2	No
# 300	68	Female	0	144	193	141	3.4	No
# 301	57	Female	0	130	131	115	1.2	No
# 302	57	Male	1	130	236	174	0.0	No
# 303 rows × 8 columns

# Solution
df["max_hr"].mean()
# 149.64686468646866
df["rest_bp"].mean()
# 131.62376237623764
# Display both
df[["max_hr", "rest_bp"]].mean()
max_hr     149.646865
rest_bp    131.623762
# dtype: float64


# Tip: To view a summary of non-numerical (categorical) columns, you should set the "include" parameter of the describe method equal to "object". In pandas, categorical variables are of type "object".
# For example:  df.describe(include="object")
# The summary will include the top occurring category for each column along with its frequency.

df.describe(include="object")
# sex	target
# count	303	303
# unique	2	2
# top	Female	Yes
# freq	207	165

df["sex"].describe()
# Note: If the describe() method is called on a categorical column (as above), then include="object" is assumed and thus does not need to be passed to the method.

info()
# The info() method displays information about a DataFrame including column data type (dtype) and non-null values.
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 303 entries, 0 to 302
# Data columns (total 8 columns):
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   age         303 non-null    int64  
#  1   sex         303 non-null    object 
#  2   chest_pain  303 non-null    int64  
#  3   rest_bp     303 non-null    int64  
#  4   chol        303 non-null    int64  
#  5   max_hr      303 non-null    int64  
#  6   st_depr     303 non-null    float64
#  7   target      303 non-null    object 
# dtypes: float64(1), int64(5), object(2)
# memory usage: 19.1+ KB
# Note: Using the info() method can be a valuable way to determine if there are any missing values in our dataset. Above, note that info() indicates that the dataset has "303 entries". 
# Also, note that it indicates that each column has "303 non-null" values. A "null" value indicates a missing value, so the above suggests that there are no missing values in the dataset. 
# Further, info() helpfully provides information about the datatype (Dtype) of each column.


#Displaying the unique values
# The Series object's (a single column) unique() method will return the column's unique values.
​
df["target"].unique()
# array(['Yes', 'No'], dtype=object)

# A Series object (single column) can be passed into Python's built-in set() function 
#   to see the column's unique values.​
set(df["target"])
# {'No', 'Yes'}
# Note: The unique() method tends to be faster. Python's set() function can be a little slower primarily because it sorts the returned values, which can be helpful in locating a specific category 
# when there are a lot of distinct values within a given column.
# Uses: We often need to convert categorical variable names into numbers for data analysis and machine learning, so being able to determine the number of unique values within a column can be helpful. 
# For example, knowing that there are only two categories within a column, as shown above, we would know that we could perhaps convert 'Yes' to 1 and 'No' to 0, when numbers are required. If we hadn't 
# determined the unique values with the column, perhaps we could have missed that there was a 'Maybe' option that also needed to be converted.

#✅ Exercise 2
# Display the unique values for the variable "chest_pain".
# Import the data
df = pd.read_csv("data/heart_disease.csv")
df
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes
# ...	...	...	...	...	...	...	...	...
# 298	57	Male	0	140	241	123	0.2	No
# 299	45	Female	3	110	264	132	1.2	No
# 300	68	Female	0	144	193	141	3.4	No
# 301	57	Female	0	130	131	115	1.2	No
# 302	57	Male	1	130	236	174	0.0	No
# 303 rows × 8 columns

# Solution
df["chest_pain"].unique()
# array([3, 2, 1, 0])





# Correlation
# The DataFrame's corr() method will display the pairwise correlations among the DataFrame's columns.

df.corr(numeric_only=True)
# age	chest_pain	rest_bp	chol	max_hr	st_depr
# age	1.000000	-0.068653	0.279351	0.213678	-0.398522	0.210013
# chest_pain	-0.068653	1.000000	0.047608	-0.076904	0.295762	-0.149230
# rest_bp	0.279351	0.047608	1.000000	0.123174	-0.046698	0.193216
# chol	0.213678	-0.076904	0.123174	1.000000	-0.009940	0.053952
# max_hr	-0.398522	0.295762	-0.046698	-0.009940	1.000000	-0.344187
# st_depr	0.210013	-0.149230	0.193216	0.053952	-0.344187	1.000000

# Uses:
# It's important to be able to interpret correlation coefficients. 
# In general, the degree of correlation is as follows:
# Perfect: If the value is near ± 1, then as one variable increases, the other variable tends to also increase (if positive) or decrease (if negative).
# High: If the value lies between ± 0.50 and ± 1, then it is said to be a strong correlation.
# Moderate: If the value lies between ± 0.30 and ± 0.49, then it is said to be a moderate correlation.
# Low: When the value lies between ± .29 and 0, then it is said to be a small correlation.
# No correlation: When the value is zero there is no correlation between the variables.
# Correlation is a very valuable tool when performing data analysis. We will discuss this in more detail  in subsequent modules that cover data analysis. 


# You also can select specific columns of interest and use the corr() method to see the pairwise correlations.
​df[["age", "max_hr"]].corr()
# age	max_hr
# age	1.000000	-0.398522
# max_hr	-0.398522	1.000000
# Note: Identifying correlations among the columns (independent variables) in a dataset can be very important. This is known as collinearity and can be detrimental to training a machine learning model.

# ✅ Exercise 3
# Display the correlation between max_hr and chest_pain.
import pandas as pd
df = pd.read_csv("data/heart_disease.csv")
df
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes
# ...	...	...	...	...	...	...	...	...
# 298	57	Male	0	140	241	123	0.2	No
# 299	45	Female	3	110	264	132	1.2	No
# 300	68	Female	0	144	193	141	3.4	No
# 301	57	Female	0	130	131	115	1.2	No
# 302	57	Male	1	130	236	174	0.0	No
# 303 rows × 8 columns

# Solution
df[["max_hr", "chest_pain"]].corr()
# max_hr	chest_pain
# max_hr	1.000000	0.295762
# chest_pain	0.295762	1.000000



# Sorting
# The DataFrame's sort_values() method takes a "by" parameter to indicate which column the DataFrame should be sorted by:

# df.sort_values(by="age").head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 72	29	Female	1	130	204	202	0.0	Yes
# 58	34	Female	3	118	182	174	0.0	Yes
# 125	34	Male	1	118	210	192	0.7	Yes
# 65	35	Male	0	138	183	182	1.4	Yes
# 157	35	Female	1	122	192	174	0.0	Yes
# Alert: By default, sort_values() will sort the values from smallest to largest.

# Alert: Remember, when modifying a DataFrame, pandas typically returns a copy so that the original DataFrame is unchanged. 
# To transfer the modification to the original Dataframe, you can either set the original Dataframe (df) equal to what pandas returns:
df = df.sort_values(by="age")
#Or you can set the method's "inplace" parameter to True so that the Dataframe itself is changed:
df.sort_values(by="age", inplace=True)

# Setting the "ascending" parameter of the sort_values() method to False will sort the values in descending order:
df.sort_values(by="age", ascending=False).head()

# ✅ Exercise 4
# Sort the DataFrame by max_hr in descending order.
import pandas as pd
df = pd.read_csv("data/heart_disease.csv")
df
# 	age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes
# ...	...	...	...	...	...	...	...	...
# 298	57	Male	0	140	241	123	0.2	No
# 299	45	Female	3	110	264	132	1.2	No
# 300	68	Female	0	144	193	141	3.4	No
# 301	57	Female	0	130	131	115	1.2	No
# 302	57	Male	1	130	236	174	0.0	No
# 303 rows × 8 columns

# Solution
df.sort_values(by="max_hr", ascending=False)
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 72	29	Female	1	130	204	202	0.0	Yes
# 248	54	Female	1	192	283	195	0.0	No
# 103	42	Female	2	120	240	194	0.8	Yes
# 125	34	Male	1	118	210	192	0.7	Yes
# 62	52	Female	3	118	186	190	0.0	Yes
# ...	...	...	...	...	...	...	...	...
# 136	60	Male	2	120	178	96	0.0	Yes
# 262	53	Female	0	123	282	95	2.0	No
# 297	59	Female	0	164	176	90	1.0	No
# 243	57	Female	0	152	274	88	1.2	No
# 272	67	Female	0	120	237	71	1.0	No
# 303 rows × 8 columns





# We can also sort by requesting the "nlargest" or "nsmallest" of a given column:
# Get the top n of a feature
# Use the nlargest() method to sort by a given column and display n number of rows. Pass in the value of n (the number of rows to display) and use the "column" parameter to indicate which row to sort by:

df[["age", "sex", "max_hr"]].nlargest(10, columns="age")
age	sex	max_hr
# 238	77	Female	162
# 144	76	Male	116
# 129	74	Male	121
# 25	71	Male	162
# 60	71	Male	130
# 151	71	Male	125
# 145	70	Female	143
# 225	70	Female	125
# 234	70	Female	109
# 240	70	Female	112


# Get the bottom n of a feature
# Use the nsmallest() method to sort by a given column and display n number of rows. Pass in the value of n (the number of rows to display) and use the "column" parameter to indicate which row to sort by:
df[["age", "sex", "max_hr"]].nsmallest(10, columns=["max_hr"])
# age	sex	max_hr
# 272	67	Female	71
# 243	57	Female	88
# 297	59	Female	90
# 262	53	Female	95
# 136	60	Male	96
# 233	64	Female	96
# 216	62	Male	97
# 198	62	Female	99
# 226	62	Female	103
# 269	56	Female	103


# You can sort by multiple columns by passing in a list of the desired columns to sort by, in order:
df[["age", "sex", "max_hr"]].nsmallest(10, columns=["max_hr", "age"])
# age	sex	max_hr
# 272	67	Female	71
# 243	57	Female	88
# 297	59	Female	90
# 262	53	Female	95
# 136	60	Male	96
# 233	64	Female	96
# 216	62	Male	97
# 198	62	Female	99
# 269	56	Female	103
# 226	62	Female	103
