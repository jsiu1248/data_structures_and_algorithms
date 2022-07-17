# collection of items of the same type stored at contiguous memory locations
# location of next index depends on the data type we use
# fixed size gets memory statically allocated
# the complier is the only one that can destroy it.


# N-based indexing: allows negative index values

# Pros
# random access to elements
# better cache locality

# Applications
# store same data type
# when size of data is known
# lookup tables

# different data types have different sizes/bytes

# typecode - returns the data type
# itemsize - size of single array element
# buffer_info - address of where array is stored

