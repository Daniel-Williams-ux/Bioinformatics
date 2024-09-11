import pandas as pd
df = pd.read_csv("data/heart_disease.csv")
df.head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes

# Rename a column
# When working with a dataset, it can helpful if the column (feature) names are clearly understood. 
# For example, even though the target variable (what we are trying to learn to predict) is whether an individual has heart disease, the name "target" may not be very clear, 
# especially to others who may be less familiar with the data set. Thus, renaming the column to "heart disease" may be helpful.

# The DataFrame's rename() method uses a column parameter. Set the column parameter equal to a dictionary representing the present column name paired with the name that you would like the column renamed to:

df = df.rename(columns={"target":"heart_disease"})
df.head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes



# Transform categorical variables to numbers
# Most machine learning algorithms require numbers, so it can be imperative to convert all categorical variables to numerical representations.

# The DataFrame's map() method takes a dictionary of pairs representing the present value paired with the desired transformed value:
df.head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes
df["sex"] = df["sex"].map({"Male":0, "Female":1})
df.head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
# 0	63	1	3	145	233	150	2.3	Yes
# 1	37	1	2	130	250	187	3.5	Yes
# 2	41	0	1	130	204	172	1.4	Yes
# 3	56	1	1	120	236	178	0.8	Yes
# 4	57	0	0	120	354	163	0.6	Yes
# Alert: Remember, a copy is returned so we set the existing column equal to the transformed values.

# ✅ Exercise 5
# Transform the target variable "heart_disease" to numbers. Transform "No" to 0 and "Yes" to 1.
# Import the data
import pandas as pd
df = pd.read_csv("data/heart_disease.csv")

# Rename the variable "target" to "heart_disease" as done above.
df = df.rename(columns={"target":"heart_disease"})

# Prior to transformation:
df.head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes

# Confirm the unique values before transforming
df["heart_disease"].unique()
# array(['Yes', 'No'], dtype=object)

# Solution
df["heart_disease"] = df["heart_disease"].map({"No": 0, "Yes": 1})
df.head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	heart_disease
# 0	63	Female	3	145	233	150	2.3	1
# 1	37	Female	2	130	250	187	3.5	1
# 2	41	Male	1	130	204	172	1.4	1
# 3	56	Female	1	120	236	178	0.8	1
# 4	57	Male	0	120	354	163	0.6	1

# Alert: It is extremely useful to confirm a column's unique values prior to tranformation. 
# It can clarify spelling and whether uppercase or lowercase was used. And, importantly, it can expose hidden spaces preceding or following a value.
# (e.g. " yes", " No ")
