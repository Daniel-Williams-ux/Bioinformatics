import pandas as pd
# We renamed the "target" column to "heart_disease" column in Lesson 6. Here, we will do this again.

df = pd.read_csv("data/heart_disease.csv")
df = df.rename(columns={"target":"heart_disease"})
df["sex"] = df["sex"].map({"Male":0, "Female":1})
df
# Preview the heart disease dataset.
df.head()
# 	age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
# 0	63	1	3	145	233	150	2.3	Yes
# 1	37	1	2	130	250	187	3.5	Yes
# 2	41	0	1	130	204	172	1.4	Yes
# 3	56	1	1	120	236	178	0.8	Yes
# 4	57	0	0	120	354	163	0.6	Yes


# Conditional selection
# Asking each value in the column "sex" whether it is equivalent to 1 ("Female"):
​
df["sex"]==1
# 0       True
# 1       True
# 2      False
# 3       True
# 4      False
#        ...  
# 298    False
# 299     True
# 300     True
# 301     True
# 302    False
# Name: sex, Length: 303, dtype: bool

# Alert: Conditional (boolean) selection is a question and always returns either True or False. This result can be placed within the square brackets of a DataFrame, using .loc, 
# and only the rows that were True will be returned.



# Use booleans for row selection
# (Review the use of .loc if needed.)
# Select the rows where the column "sex" is equivalent to 1 ("Female"). Then display just the column "age":
# df.loc[df["sex"]==1, "age"]
# 0      63
# 1      37
# 3      56
# 5      57
# 7      44
#        ..
# 295    63
# 297    59
# 299    45
# 300    68
# 301    57
# Name: age, Length: 207, dtype: int64

count()
# The count() method displays the number of rows that are included in a selection.
# Get the rows where the column chest_pain is equivalent to 3. Return only the column "sex", and display the number of rows returned:
# Use count() to get the number of rows (returned) in a selection.​
df.loc[df["chest_pain"]== 3, "sex"].count()
# 23


value_counts()
# The value_counts() method displays the itemized counts of each category within a column. In other words, it breaks the column down into its individual categories then sums by category. 
# For example, if the column "sex" contained the values [M, F, F, M, F, M, F, F], value_counts() would return that there are 5 of the category F and 3 of the category M:
# F 5
# M 3

# Get the rows where the column chest_pain is equivalent to 3. Return only the column "sex", and itemize the number of rows returned by gender:
# Use value_counts() to get the count of each unique category within a column.​
df.loc[df["chest_pain"]== 3, "sex"].value_counts()
sex
# 1    19
# 0     4
# Name: count, dtype: int64


# ✅ Exercise 6
# Display how many people had heart disease in this dataset.
# Import the data
import pandas as pd
df = pd.read_csv("data/heart_disease.csv")
# Rename the variable "target" to "heart_disease" as done above.
df = df.rename(columns={"target":"heart_disease"})
df
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
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

#Solution
# The column "sex" was chosen here but any column can usually be chosen 
#   as we're just counting how many rows are returned for the query.​
df.loc[df["heart_disease"]== "Yes", "sex"].count()
# 165
df.loc[df["heart_disease"]== "Yes"].count()
# age              165
# sex              165
# chest_pain       165
# rest_bp          165
# chol             165
# max_hr           165
# st_depr          165
# heart_disease    165
# dtype: int64



# Multiple conditions
# Using .loc, you can set multiple conditions for a query. The ampersand (&) means "and" and the pipe symbol (|) means "or".

# And (&) operation
# Get the rows where the column "sex" is equivalent to 1 ("Female") AND where the column "max_hr" is greater than the average "max_hr". Return only the column "sex", and display the number of rows returned:

mean_max_heart_rate = df["max_hr"].mean()
df.loc[(df["sex"]== 1) & (df["max_hr"] > mean_max_heart_rate), "sex"].count()
# 110

# Or ( | ) operation
# Get the rows where the column "chest_pain" is equivalent to 0 OR the column "age" is greater than 60; AND, from among those rows, get the rows where the column 
# "sex" is equivalent to 0 ("Male"). Return only the column "heart disease", and display the itemized count of how many did and did not have heart disease:
df.loc[((df["chest_pain"] == 0) | (df["age"] > 60)) &
        (df["sex"] == 0), "heart_disease"].value_counts()
# heart_disease
# Yes    34
# No     22
# Name: count, dtype: int64

# Alert: Because of precedence and the order of operations, it's important to place parentheses around each condition to clarify the desired order of operations.
# ✅ Exercise 7
# Get the rows where the column "max_hr" is less than 120 OR the column "chol" is greater than 300; 
# AND, from among those rows, get the rows where the column "sex" is equivalent to 1 ("Female"). Then display the itemized count of the patients who had and did not have heart disease.
# Import the data
import pandas as pd
df = pd.read_csv("data/heart_disease.csv")
# Rename the variable "target" to "heart_disease", as done above.
df = df.rename(columns={"target":"heart_disease"})
# For the variable "sex", transform "Male" to 0 and "Female" to 1, as done above.
df["sex"] = df["sex"].map({"Male":0, "Female":1})   
df
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
# 0	63	1	3	145	233	150	2.3	Yes
# 1	37	1	2	130	250	187	3.5	Yes
# 2	41	0	1	130	204	172	1.4	Yes
# 3	56	1	1	120	236	178	0.8	Yes
# 4	57	0	0	120	354	163	0.6	Yes
# ...	...	...	...	...	...	...	...	...
# 298	57	0	0	140	241	123	0.2	No
# 299	45	1	3	110	264	132	1.2	No
# 300	68	1	0	144	193	141	3.4	No
# 301	57	1	0	130	131	115	1.2	No
# 302	57	0	1	130	236	174	0.0	No
# 303 rows × 8 columns

# Solution
df.loc[((df["max_hr"] < 120) | (df["chol"] > 300)) &
       (df["sex"] == 1), "heart_disease"].value_counts()
# heart_disease
# No     34
# Yes     9
# Name: count, dtype: int64
