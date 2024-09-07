# 1. # Create a vector named "items":
items <- c(5,10,15,20,25,30,35,40)
items

# 2. # Assign 100 to the item at index position 2:
items[2] <- 100
items # 5,100,15,20,25,30,35,40

# 3. # Assign 0 to every index position except 2:

items[-2] <- 0
items # 0,100,0,0,0,0,0,0
