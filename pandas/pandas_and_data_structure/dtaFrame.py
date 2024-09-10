# DataFrame
# The DataFrame is another data structure in pandas. A DataFrame is a two-dimensional array of values. Much like an Excel spreadsheet, it is a rectangular table of columns and rows with both a row index and a column index. 
# It can, somewhat, be thought of as a collection of Series objects, each of which can have a different data type (e.g., strings, numbers).
# Typically, pandas will import data (e.g., from a csv file) as a DataFrame. However, a DataFrame may be constructed, for example, by using a dictionary (key/value pairs) with the key being the column name and the value being a list of row values.

# Creating a sample DataFrame using a dictionary of lists of values.
data = {"Name": ["Tim Miller", "Ann Carter", "Ellen Lee", "Sam Carr", "Al Ball", "Carl Zee", "Sara Martin"], 
        "Gender": ["Male", "Female", "Female", "Male", "Male", "Male", "Female"],
        "Age": [32, 44, 21, 19, 45, 27, 39]}
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



# Preview a DataFrame
head()
# The head() method is used to display only the first 5 rows.​
df.head() # == df.head(5)
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# 3	Sam Carr	Male	19
# 4	Al Ball	Male	45

tail()
# The tail() method is used to display only the last 5 rows.​
df.tail()  # == df.tail(5)
# Name	Gender	Age
# 2	Ellen Lee	Female	21
# 3	Sam Carr	Male	19
# 4	Al Ball	Male	45
# 5	Carl Zee	Male	27
# 6	Sara Martin	Female	39
# Note: The DataFrame's head() and tail() methods default to displaying five rows. To display a different number of rows, place the desired number within the method's parentheses (e.g. df.head(25)) and that number of rows wil be displayed.



# Column selection
# You can retrieve a column from a DataFrame by using the column's name between square brackets. (A Series object is returned.):

# Returns a column/Series object
​
df['Name']     # Dictionary notation
# 0     Tim Miller
# 1     Ann Carter
# 2      Ellen Lee
# 3       Sam Carr
# 4        Al Ball
# 5       Carl Zee
# 6    Sara Martin
# Name: Name, dtype: object

# You can also use dot notation to retrieve a column (Series) from a DataFrame, but only if the column name is a valid Python variable name (e.g., no spaces):
df.Name     # Attribute (dot) notation
# 0     Tim Miller
# 1     Ann Carter
# 2      Ellen Lee
# 3       Sam Carr
# 4        Al Ball
# 5       Carl Zee
# 6    Sara Martin
# Name: Name, dtype: object
df
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# 3	Sam Carr	Male	19
# 4	Al Ball	Male	45
# 5	Carl Zee	Male	27
# 6	Sara Martin	Female	39
Tip: When using dot notation (attribute notation), following the dot, you can use the tab key to complete the column name (or any other attribute). For example, using the above DataFrame, try typing just 'df.N'.
# Then use the tab key, and Jupyter will complete the rest, or present any other options that begin with 'df.N'. 
# This is known as tab completion and is provided as a convenience by Jupyter.



# You can determine the order of your columns by placing the names in a list, in the desired order:
df[["Age", "Gender", "Name"]]    
# Age	Gender	Name
# 0	32	Male	Tim Miller
# 1	44	Female	Ann Carter
# 2	21	Female	Ellen Lee
# 3	19	Male	Sam Carr
# 4	45	Male	Al Ball
# 5	27	Male	Carl Zee
# 6	39	Female	Sara Martin
# Alert: By default, pandas returns a copy of the original DataFrame with the requested modifications. The original DataFrame remains unmodified.



 #Row selection
# You can retrieve specific rows from a DataFrame by using index notation and slicing as with Lists in Python:
df[0:1]
# Name	Gender	Age
# 0	Tim Miller	Male	32
df[:3]
# Name	Gender	Age
# 0	Tim Miller	Male	32
# 1	Ann Carter	Female	44
# 2	Ellen Lee	Female	21
# Note: Row selection syntax is used to select rows (e.g., df[:3]). Passing the string name of a column selects columns (e.g., df["Age"]).
