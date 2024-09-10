# Matrix
# A matrix is a two-dimensional collection of data elements. Like vectors, matrices can only contain a single data type. You can create a matrix by using the matrix( ) function.

# To create a matrix, you first specify a vector and then you can specify the desired dimensions (rows x cols).
matrix(1:12, nrow=3, ncol=4)
# A matrix: 3 × 4 of type int
# 1	4	7	10
# 2	5	8	11
# 3	6	9	12

# Note: The numbers 1 to 12 will be filled column-wise by default (i.e., the matrix will be populated down the columns first).

# Alternatively, after specifying a vector, you can indicate the desired number of rows and the number of columns will be calculated.
matrix(c(1:12), nrow = 3)
# A matrix: 3 × 4 of type int
# 1	4	7	10
# 2	5	8	11
# 3	6	9	12

# Alternatively, after specifying a vector, you can indicate the desired number of columns and the number of rows will be calculated.
matrix(c(1:12), ncol = 2)
# A matrix: 6 × 2 of type int
# 1	7
# 2	8
# 3	9
# 4	10
# 5	11
# 6	12
