# csv file
# Below, we will use pandas' read_csv() function to import a heart disease dataset. Pandas imports the dataset as a DataFrame.

import pandas as pd
df
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


#Preview dataset
head()
df.head()
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 0	63	Female	3	145	233	150	2.3	Yes
# 1	37	Female	2	130	250	187	3.5	Yes
# 2	41	Male	1	130	204	172	1.4	Yes
# 3	56	Female	1	120	236	178	0.8	Yes
# 4	57	Male	0	120	354	163	0.6	Yes
# Dataset: This heart disease dataset, from the University of California Irvine's Machine Learning Repository, enables the evaluation of some of the variables that may be predictive of heart disease. 
# Datasets like this, which have a series of predictive variables (called "features" in data science) paired with a known outcome variable (called the "target"), are exteremly useful toward 
# developing machine learning models that can be trained to accurately predict patient outcomes. For example, using this dataset, we could train a model to predict which patients are most likely to suffer 
# from heart disease in the future and are at risk of having a heart attack or stroke.

# sample()
# Instead of having the DataFrame simply return the first five or last five rows, as head() and tail(), respectively, do, the DataFrame's sample() method returns a random sampling of rows from the dataset. 
# The number passed to the method determines the number of rows returned.
df.sample(10)
# age	sex	chest_pain	rest_bp	chol	max_hr	st_depr	target
# 255	45	Female	0	142	309	147	0.0	No
# 138	57	Female	0	110	201	126	1.5	Yes
# 175	40	Female	0	110	167	114	2.0	No
# 161	55	Male	1	132	342	166	1.2	Yes
# 240	70	Female	2	160	269	112	2.9	No
# 101	59	Female	3	178	270	145	4.2	Yes
# 170	56	Female	2	130	256	142	0.6	No
# 278	58	Male	1	136	319	152	0.0	No
# 90	48	Female	2	124	255	175	0.0	Yes
143	67	Male	0	106	223	142	0.3	Yes
