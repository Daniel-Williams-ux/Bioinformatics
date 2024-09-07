You can also remove list items. The following example creates a new, updated list without an "apple" item:

Example
Remove "apple" from the list:

thislist <- list("apple", "banana", "cherry")

newlist <- thislist[-1]

# Print the new list
newlist 
# 'banana'
# 'cherry'
