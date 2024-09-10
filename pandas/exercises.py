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
# max_hr     149.646865
# rest_bp    131.623762
# dtype: float64



# Exercise 2
# Display the unique values for the variable "chest_pain".
# Import the data
df = pd.read_csv("data/heart_disease.csv")
df
Solution
df["chest_pain"].unique()
array([3, 2, 1, 0])
# Interpretation:
# The numbers in the "chest_pain" column likely represent different categories of chest pain in a clinical setting. For example:

# 0: Might represent no chest pain.
# 1: Could represent mild chest pain.
# 2: Might indicate moderate chest pain.
# 3: Could denote severe chest pain.
