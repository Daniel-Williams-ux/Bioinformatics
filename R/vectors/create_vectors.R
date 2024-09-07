# The fundamental data structure in R is the vector. A vector is a one-dimensional sequence of data elements, of the same type, stored in a sequence. The elements are most commonly of type character, logical, integer or numeric.
# 1.
v1  <-  c(1,2,3,4)
v1

# 2.
# Vector of strings
fruits <- c("banana", "apple", "orange")

# Print fruits
fruits

# 3.
v3  <-  c(TRUE, FALSE, TRUE, FALSE)
print(v3)

# Note that if you mix data types, R will coerce the vector to a single data type:
# Alert: A vector is a data structure that contains only a single data type (e.g., integers, logicals).


                                          # Creating Vectors from a Sequence of Numbers
                                          # A vector can be constructed from a sequence of numbers:

# Create a vector from the sequence of numbers 1 through 10 (inclusive):
# 1.
seq1 <- 1:10
print(seq1) #  1  2  3  4  5  6  7  8  9 10

# 2.
# Create a vector of numbers beginning from 5 and counting down through (and including) -5:
seq1 <- 5:-5
print(seq1) # 5  4  3  2  1  0 -1 -2 -3 -4 -5


                                         # A Vector Created using the seq() Function
                                         # The seq() ("sequence") function can be used to construct a vector from a sequence of numbers:

# 1.
# Create a vector of 10 numbers beginning from 1:
seq(10)

# 2.
# Create a vector of numbers from 1 through 10, but skipping every second number:
seq(1, 10, 2)

# 3.
# Create a vector of 20 numbers, evenly spaced between the numbers 1 through 10:
seq(1, 10, length=20)

# 4.
# Create a vector of numbers from 1 through 10, stepping every 0.1:
seq(from = 1, to = 10, by = 0.1)

                                              # A Vector Created from a Sample of Numbers

# Create a vector by drawing from a sample of numbers from 1 through 10, without replacement:
sample(1:10)
