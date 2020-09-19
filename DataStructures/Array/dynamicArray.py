
import array

#array(data type, value list) 
arr = array.array('i', [1,2,3, 2,5, 6,7, 2])
arr1 = array.array('i', [10,20,30,50, 60,70])
for i in range(len(arr)):
	print(arr[i], end="  ")

# using typecode to print datatype of array 
print("\nTypecode: ", arr.typecode)

#using itemsize to print the size of the array
print("\nItemsize: ", arr.itemsize)

# using buffer_info() to print buffer info. of array 
print("\n Buffer Info :", arr.buffer_info())

# Count the number of occurence of a element 
print("\n Occurence of 2 in the Array: ",arr.count(2))

# appends a whole array mentioned in its arguments to the specified array
arr.extend(arr1) 

#This function is used to add the value mentioned in its arguments at the end of the array.
arr.append(4)
print("\n")
for i in range(len(arr)):
	print(arr[i], end=" ")


#This function is used to add the value at the position specified in its argument.
arr.insert(2,45)
print("\n")
for i in range(len(arr)):
	print(arr[i], end=" ")
#This function removes the element at the position mentioned in its argument, and returns it.
arr.pop(2)
print("\n")
for i in range(len(arr)):
	print(arr[i], end="  ")

#This function is used to remove the first occurrence of the value mentioned in its arguments.
arr.remove(2)
print("\n")
for i in range(len(arr)):
	print(arr[i], end="  ")

#This function returns the index of the first occurrence of value mentioned in arguments.
arr.index(4)
print("\n", arr.index(4))
#for i in range(len(arr)):
#	print(arr[i], end="  ")

#This function reverses the array.
arr.reverse()
print("\n")
for i in range(len(arr)):
	print(arr[i], end="  ")

