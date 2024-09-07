# You can specify a range of indexes by specifying where to start and where to end the range, by using the : operator:

# Example
# Return the second, third, fourth and fifth item:

thislist <- list("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

(thislist)[2:5]
# 'banana'
# 'cherry'
# 'orange'
# 'kiwi'

# Note: The search will start at index 2 (included) and end at index 5 (included).

# Remember that the first item has index 1.
