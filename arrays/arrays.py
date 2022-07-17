import array

# initializes array with signed integers
arr = array.array('i',[1,2,3])

# insert new value at the end
arr.append(4)

# insert 5 at the second position
arr.insert(2,5)

# remove element at 2nd position
arr.pop(2)

# remove 1st occurence of 1
arr.remove(1)

# reverses array
arr.reverse()

# count - counts the number of occurrences
arr.count()

# transform array to a list
li2 = arr.tolist()

