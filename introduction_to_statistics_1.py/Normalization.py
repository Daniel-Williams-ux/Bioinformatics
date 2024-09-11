# Normalization, in the general sense, refers to scaling our numeric columns to bring them into the same terms so that they fall within a smaller and standard range of values, making it easier to compare them.

# This is useful because data variables are typically measured in varied units with varied magnitudes. 
# For example, a patient's age is measured in terms of years while heart rate is measured in terms of beats per minute. These variables are measured in completely different terms which makes it difficult to make a comparison as to which may be better or worse than the other.

# However, normalization, in the specific sense, refers to scaling variables so that their values fall strictly between 0 and 1, making it easier to compare them. This is also known as min-max scaling.







# Normalizing a sample heart disease dataset
# In the sample dataset below, "age", cholesterol ("chol"), and max heart rate ("max_hr") are all measured in different units and have different magnitudes and ranges of values. Let's normalize the dataset.

# ✅ Run each of the cells below:
import pandas as pd
df = pd.read_csv("data/data_normalization/heart-disease.csv", usecols=[0,4,5])
df.head()
# age	chol	max_hr
# 0	63	233	150
# 1	37	250	187
# 2	41	204	172
# 3	56	236	178
# 4	57	354	163

# The minimum value for each column:
df.min()
# age        29
# chol      126
# max_hr     71
# dtype: int64

# The maximum value for each column:
df.max()
# age        77
# chol      564
# max_hr    202
# dtype: int64

# The normalized dataset:
(df - df.min())/(df.max() - df.min())
# age	chol	max_hr
# 0	0.708333	0.244292	0.603053
# 1	0.166667	0.283105	0.885496
# 2	0.250000	0.178082	0.770992
# 3	0.562500	0.251142	0.816794
# 4	0.583333	0.520548	0.702290
# ...	...	...	...
# 298	0.583333	0.262557	0.396947
# 299	0.333333	0.315068	0.465649
# 300	0.812500	0.152968	0.534351
# 301	0.583333	0.011416	0.335878
# 302	0.583333	0.251142	0.786260
# 303 rows × 3 columns

# Each column is now in similar terms. Each of the values falls between 0 and 1, so we have a better comparison for the magnitude of a given value relative to the other columns.
# It should now be clear why normalizing values is useful. It's an effective way of comparing values that are measured in different units and it scales values down into a standard range.

# Tip: Another scaling technique that is used to transform variables so that they are in similar terms is called standardization. This technique scales values so that they are in terms of how far they are from their respective means (in terms of standard deviations). 
#  Rather than falling between 0 and 1 as normalization does, standardized values are scaled to fall typically between -3 and 3 (see Z-score).









What is Normalization?
Normalization is a way to make different numbers from a dataset more similar in scale. Think of it as adjusting numbers so that they are all on the same playing field. This is helpful when the numbers represent different things and have different ranges, like "age", "cholesterol", and "max heart rate".

For example, if we have age values between 30 and 80 and cholesterol values between 100 and 400, the numbers are on very different scales. Normalizing helps bring these numbers closer together in terms of range, so that no one value dominates just because it's larger.

Why Do We Normalize Data?
In some machine learning models, large numbers can overshadow smaller ones, which makes the model biased toward certain features. Normalization helps balance these numbers so every feature is equally important when the computer learns from the data.

Let’s Normalize the Heart Disease Data
We have this dataset with 3 columns:

age: The age of the patient.
chol: Cholesterol levels.
max_hr: Maximum heart rate.
Here's how the data looks:

age	chol	max_hr
63	233	150
37	250	187
41	204	172
56	236	178
57	354	163
The numbers are in different ranges, so we will normalize them.

How to Normalize Data?
A common way to normalize data is by using Min-Max Normalization. This method transforms the values to a range between 0 and 1.

The formula for Min-Max normalization is:

Normalized Value
=
(
𝑋
−
Min
)
(
Max
−
Min
)
Normalized Value= 
(Max−Min)
(X−Min)
​
 
X: The value you want to normalize.
Min: The smallest value in the dataset.
Max: The largest value in the dataset.
This makes sure the smallest value becomes 0, the largest value becomes 1, and the others are scaled between 0 and 1.

Normalizing the Dataset
Let's normalize the "age", "chol", and "max_hr" columns in our heart disease dataset.

python
Copy code
# Step 1: Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 2: Load the dataset
df = pd.read_csv("data/data_normalization/heart-disease.csv", usecols=[0,4,5])

# Step 3: Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Step 4: Normalize the data (age, chol, max_hr)
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Step 5: Show the normalized data
df_normalized.head()
What Does Normalized Data Look Like?
After normalization, the values of "age", "chol", and "max_hr" will be between 0 and 1, like this:

age	chol	max_hr
0.8667	0.3594	0.4103
0.1333	0.4063	1.0000
0.2444	0.2656	0.6923
0.7111	0.3672	0.7692
0.7333	0.7813	0.5897
Age: Now ranges between 0 and 1.
Cholesterol: Scaled down to a range between 0 and 1.
Max Heart Rate: Also scaled between 0 and 1.
Now, the numbers are all in a similar range, making it easier for models or comparisons to treat them equally.

In Summary:
Normalization is like rescaling numbers to make them comparable.
It helps when different features (like age, cholesterol, heart rate) have different units and ranges.
After normalization, all the values are on the same scale (typically between 0 and 1), which helps in better data analysis and machine learning models.
This process ensures that the machine or algorithm looks at the patterns in the data, not just the size of the numbers.
