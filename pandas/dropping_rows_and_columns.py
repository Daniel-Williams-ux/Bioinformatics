# You can use the drop() method on the DataFrame to drop entries. Adding the desired axis will determine whether rows or columns will be dropped. There are two axes in pandas:

# Axis 0 indicates that you intend to drop a row.
# Axis 1 indicates that you intend to drop a column.
import pandas as pd
data = {"Name": ["Tim Miller", "Ann Carter", "Ellen Lee", "Sam Carr", "Al Ball", "Carl Zee", "Sara Martin"], 
        "Gender": ["Male", "Female", "Female", "Male", "Male", "Male", "Female"],
        "Age": [32, 44, 21, 19, 45, 27, 39]}
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# 3	Sam Carr	Male	19
# 4	Al Ball	Male	45
# 5	Carl Zee	Male	27
# 6	Sara Martin	Female	39


# Dropping rows
# Row with index 6 will be dropped
df.drop(6, axis = 0)
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# 3	Sam Carr	Male	19
# 4	Al Ball	Male	45
# 5	Carl Zee	Male	27
# Alert: Axis = 0 indicates that you intend for rows to be dropped. In the example above, you are indicating that you would like for the row at index position 6 to be dropped. Using axis = 1 would indicate that you intend for columns to be dropped. 
# For example, you could type `df.drop("Age", axis = 1). This would indicate that you intend to drop the column 'Age'. Using any other value other than 0 or 1 for axis will return an error. 
# Alternatively, you could use 'df.drop(index = 6)' to drop the row at index position 6. And you could use 'df.drop(columns = "Age")' to drop the column 'Age'.

# Note that drop() returns a copy of the DataFrame so that the original DataFrame (df) remains unmodified:
# Original DataFrame is unmodified.​
df
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# 3	Sam Carr	Male	19
# 4	Al Ball	Male	45
# 5	Carl Zee	Male	27
# 6	Sara Martin	Female	39

# Remember: By default, when modifications are made to a DataFrame, pandas returns a copy, leaving the original DataFrame unmodified. 
# If you would like for the changes to be reflected in the original DataFrame (df), then you can set the original DataFrame (df) equivalent to the returned copy following the drop, as demonstrated below.


Remember: By default, when modifications are made to a DataFrame, pandas returns a copy, leaving the original DataFrame unmodified. If you would like for the changes to be reflected in the original DataFrame (df), then you can set the original DataFrame (df) equivalent to the returned copy following the drop, as demonstrated below.
# The returned copy replaces the original DataFrame so that df is now modified.
​
df = df.drop(6, axis = 0)​
df
# Note: If you prefer to just have the DataFrame modify itself in place rather than return a copy of itself, then you can set the drop method's "inplace" parameter to True, as shown below:
df.drop(6, axis=0, inplace=True)
# Alert: Be careful when making changes "inplace". Inplace changes modify the original data and the only way to get it back is by reimporting it. 
# Alternatively, by working with a copy, you can easily return to the original DataFrame when circumstances require it without needing to reimport data.


Alternatively, instead of setting the axis parameter to 0, you can set the drop method's index parameter which signals that rows will be dropped:
df = df.drop(index = [3, 6])​
df
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# 4	Al Ball	Male	45
# 5	Carl Zee	Male	27
# Alert: If you would like for more than one row or column to be dropped, then you must put them in a list, as shown above.





# Dropping columns
# # By setting the axis to 1, the column with the name "Age" will be dropped.
​
df = df.drop("Age", axis = 1)
df
# Name	Gender
# 0	Tim Miller	Male
# 1	Ann Carter	Female
# 2	Ellen Lee	Female
# 4	Al Ball	Male
# 5	Carl Zee	Male

# Resetting the DataFrame​
df = pd.DataFrame(data)
df
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# 3	Sam Carr	Male	19
# 4	Al Ball	Male	45
# 5	Carl Zee	Male	27
# 6	Sara Martin	Female	39
# Alternatively, instead of setting the axis parameter to 1, you can set the drop method's columns parameter which signals that columns will be dropped:

# Columns "Gender" and "Age" will be dropped.
df = df.drop(columns = ["Gender", "Age"])​
df
# Name
# 0	Tim Miller
# 1	Ann Carter
# 2	Ellen Lee
# 3	Sam Carr
# 4	Al Ball
# 5	Carl Zee
# 6	Sara Martin
# Alert: To drop more than one row or column, you must place the entries within a list.
