# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting value at the second position
my_list.insert(1, 15)  # Note that list positions start at 0, so position 1 is the second position

# Extending my_list with another list
my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop()  # Removes the last item in the list

# Sorting the list in ascending order
my_list.sort()

# Finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print("The index of value 30 in my_list is:", index_of_30)
