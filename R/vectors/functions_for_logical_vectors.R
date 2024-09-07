                                         #Functions for logical vectors
# Test each value in the vector v as to whether it is greater than 10 or not (returns TRUE or FALSE):
​
v = c(25, 9, 16, 4)​
v > 10 # TRUE FALSE TRU EFALSE

# any() returns TRUE if any of the logicals are TRUE:
any(v > 10)

# # all() returns TRUE if all of the logicals are TRUE:​
all(v > 10)

# which() returns the indices/locations of the TRUE values (interpreted as as "Which index positions are TRUE?"):​
which(v > 10)
