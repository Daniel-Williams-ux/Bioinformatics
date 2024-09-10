# Import the pandas data analysis library
# First, we'll import the pandas library into our notebook so that it's functionality is available to us. Traditionally, "pd" is used as the alias for pandas. Therefore, whenever you see pd. in the code, it's referring to the use of pandas and its capabilities.
import pandas as pd

# A Series is a one-dimensional object containing a sequence of values, very similar to a column of data in an Excel spreadsheet. The Series data structure has an associated index which can be either numbers, or strings (ie. named labels).
series_obj = pd.Series([10,20,30,40,50])
series_obj
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# Note: The index of the Series object is displayed on the left, the values are displayed on the right and the data type is displayed beneath.
# Note: "dtype: int64" in the above output means data is stored as integers. Data type (dtype) represents how a value is stored in memory and, for numbers, it indicates how precisely it can be represented in memory.
# It is helpful to know the data type of a value because different data types have different capabilities that dictate how they can be handled and dictate the result of any operations performed on them. 
# For example, knowing whether the value 10 is stored as an integer or as a string (e.g., “10”) is important. 
# Math can’t be applied to the string “10” so perhaps it would need to be converted to an integer (int64) data type in order to get descriptive statistics of the column (e.g., mean, standard deviation) or to perform machine learning.

# Wearable data is somewhat unique and can be represented as any of the data types depending upon the values being collected. For example, the date of collection would be represented as type date64 in Pandas. 
# The delta or difference between two time points would be stored as type timedelta. Moreover, wearable data is typically time series data that is stored as float64.



# Accessing values by index position
# The values, in a Series object, can be accessed by placing the associated index position within square brackets. It is similar to how we access values from within a Python List.
eries_obj = pd.Series([10,20,30,40,50])
series_obj[0]
# 10



# Accessing a slice of the data
series_obj[0:3]
# 0    10
# 1    20
# 2    30
# dtype: int64
# Alert: Remember, Python considers the first item to be at index position 0. And the ending index position that you provide will not be included in what is returned. The closing index position should be just beyond the position you would like included in the slice. 
# That's why, in the example above, index position 3 is not included in the values returned.



# Using named labels
# A label can be used to identify each data point (row) by providing a list of the desired labels to the index property of the Series object.
series_obj = pd.Series([10,20,30,40,50], index = ["CA", "FL", "NY", "PA", "TX"])
series_obj
# CA    10
# FL    20
# NY    30
# PA    40
# TX    50
# dtype: int64



# Accessing values by named label
# When the values in a Series object have labels, you can use the labels to select values.
series_obj["CA"]
# 10
series_obj["CA":"TX"]
# CA    10
# FL    20
# NY    30
# PA    40
# TX    50
# dtype: int64
# Note: When selecting a slice of entries using named labels, the end point (stopping point) is inclusive.



# If you're requesting more than one label (index), they must be placed within a list:
series_obj[["CA", "NY", "TX"]]
# CA    10
# NY    30
# TX    50
# dtype: int64
# Note: Even though the index above uses named labels, you can still use the numerical index position of a value to access it.



# Element-wise operations
# Create a Series object.
series_obj = pd.Series([10,20,30,40,50])
series_obj
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64
# An operation can be applied to each element in a Series object. Element-wise operations are convenient as we don't need to use a for loop to apply the operation. Pandas will apply the operation to each element in the Series for us.
series_obj * 2
# 0     20
# 1     40
# 2     60
# 3     80
# 4    100
# dtype: int64
series_obj + 100
# 0    110
# 1    120
# 2    130
# 3    140
# 4    150
# dtype: int64
# Create a new Series object.​
series_obj2 = pd.Series([1,2,3,4,5])
series_obj2
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
# We can apply element-wise operations to combine two Series objects.

# Combine the two Series objects, element-wise.​
series_obj + series_obj2
# 0    11
# 1    22
# 2    33
# 3    44
# 4    55
# dtype: int64



# Boolean selection
# We can filter the values that we want by using a boolean array.
# We can query each item in the Series, returning True or False boolean values.​
series_obj >20
# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
# dtype: bool

# We can use the results (the boolean array) of the boolean query in order to filter the values. By placing the query between the square brackets of the Series object, only the values whose index position returns True will be returned.
series_obj[series_obj > 20]
# 2    30
# 3    40
# 4    50
# dtype: int64

# Remember: When filtering the values by using a boolean query, you're asking the Series object a question. For every index location that returns True to your question, only those associated values (rows) will be returned.
