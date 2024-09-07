# If desired, you can use key/value pairs to assign a name to each element within a vector. You can then use the element's name to access its value:

# Create a vector giving names to each element:
​
groceries <- c("milk"=3.56, "bread"=4.29, "rice"=5.98)
groceries
# Place the element's name within the square brackets of the vector to return its value:
​
groceries["rice"]
# Use a vector of names to return more than one element's value:
​
groceries[c("rice", "bread")]
