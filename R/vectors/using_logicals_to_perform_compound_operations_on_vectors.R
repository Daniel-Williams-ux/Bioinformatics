# 1. # & is the "AND" operation in R.
# Return TRUE where each item at a given index position between the vectors is TRUE:
c(FALSE, TRUE, FALSE) & c(TRUE, TRUE, TRUE) # FALSE TRUE, FALSE

# 2. # | is the "OR" operation in R.
# Return TRUE where either item at a given index position between the vectors is TRUE:
c(FALSE, TRUE, FALSE) | c(TRUE, TRUE, TRUE) # TRUE, TRUE, TRUE

# 3. # Create the vector "v":

v = c(25, 9, 16, 4)

# 4. Test whether a value in the vector v is either less than 5 or (|) greater than 20:
(v < 5) | (v > 20) # (TRUE, FALSE, FALSE TRUE

# 5. # Place the logical operation from above between the square brackets of "v" to return the actual values.
# In otherwords, v will return any value whose index position is TRUE:
v[(v < 5) | (v > 20)] # 25  4
# explanation
v <- c(25, 9, 16, 4)
# Logical Condition:

# (v < 5) checks which elements in v are less than 5.
# For v = c(25, 9, 16, 4), the result is FALSE, FALSE, FALSE, TRUE.
# (v > 20) checks which elements in v are greater than 20.
# For v = c(25, 9, 16, 4), the result is TRUE, FALSE, FALSE, FALSE.
# OR Condition:

# The logical OR (|) combines the two conditions:
# (v < 5) | (v > 20) results in TRUE, FALSE, FALSE, TRUE.
# Filtering with Square Brackets:

# Using square brackets, v[(v < 5) | (v > 20)] returns the elements from v where the condition is TRUE.


# 6. Create a vector named "nums" containing numbers from 1 through 10.
# Within the square brackets of "nums", perform a compound operation so that only values that are either less than 4 or greater than 8 are returned.
x <- 1:10
x
squared_bracket <- x[(x < 4) | (x > 8)]
squared_bracket # 1 2 3 9 10
# explanation
# T T T F F F F F F F
# OR
# F F F F F F F F T T

# Result
# T T T F F F F F T T
# 1 2 3           9 10
