rows = int(input("rows=>")) # taking input for rows
cols = int(input("Cols=>")) # taking input for columns
array = int(input("array=>")) # taking input for array

arr = [[[i for i in range(cols)] for j in range(rows)]for k in range(array)]
print(arr)
