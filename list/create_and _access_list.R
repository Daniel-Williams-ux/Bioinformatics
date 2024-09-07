# A list is a collection of items but unlike vectors, lists can contain any mixture of elements of any type. Lists can even contain other lists.
# 1. You can use the list() function to crerate a list:
L <- list("a", 1, 2.5, TRUE)
L
# 'a'
# 1
# 2.5
# TRUE

# 2. Elements within a list can be accessed by placing the element's index position within square brackets:
L[4]
# TRUE
L[2:3]
# 1
# 2.5

# 4. Named lists
# Lists can also use names by creating key/value pairs to assign a name to each element within the list. You can then access an element within the list by using the element's name/key:

a_list <- list("San Francisco"= 1, "Santa Clara" = 2, "San Jose" = 3)
a_list
# $`San Francisco`
# 1
# $`Santa Clara`
# 2
# $`San Jose`
# 3
# Note: The '$' preceding the characters in the output above indicates that the characters are a key from the named list as opposed to a value.
a_list["San Jose"]
