# 1.typeof()
#The typeof() function can be used to evaluate the data type that a vector contains:
# Mixed data types coerced to a single data type:
v4  <-  c(TRUE, FALSE, TRUE, "FALSE")
typeof(v4) # 'character'

# 2. length()
# The length() function can be used to determine the number of elements that a vector contains:
length(v4) # 4

# 3. Missing Data
# a. Missing values in R are indicated by NA (Not Available):
x <- c(0.5, 0.7, NA)
# Variable containing a vector with a misssing value
x

# b. is.na()
# is.na() can be used to test whether a value is missing. It returns a logical vector:
# Test each value in a vector as to whether it is missing or not:​
x <- c("a", NA, "c", "d", "e")​
# x is the variable containing a vector with a missing value
is.na(x)

# c. anyNA()
# anyNA() can be used to evaluate whether a vector contains any missing (NA) values:
x <- c("a", NA, "c", "d", "e")​
# x is the variable containing a vector with a misssing value
anyNA(x)
