# There are several ways to join, or concatenate, two or more lists in R.

# The most common way is to use the c() function, which combines two elements together:

# Example
list1 <- list("a", "b", "c")
list2 <- list(1,2,3)
list3 <- c(list1,list2)

list3
# 'a'
# 'b'
# 'c'
# 1
# 2
# 3
