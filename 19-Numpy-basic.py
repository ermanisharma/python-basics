import numpy as np
dt = np.dtype([('Age', np.int32)])  # you can go with int8, int16 as well.
print('Data Type : ', dt)

ageList = [12, 44, 23, 65]
ageArray = np.array(ageList, dt, order='C')

print('AgeArray : ', ageArray)

ageArray_Copy = ageArray.copy()  # this will create a copy of array at the new memory address

ageArray_View = ageArray.view()  # this will create a copy of array at the same memory address
print('Age array View : ', ageArray_View)

ageArray_View[2]=100
print('Age array View after update at index 2 : ', ageArray_View)

my_array = np.arange(start=10, stop=50, step=5)
print('my array using array range : ', my_array)  # 10 15 20 25 30 35 40 45 50 i.e. 1x8 array

# here we just created array and not provided Row or Column means it's single dimension array
print('My array shape is : ', my_array.shape)

my_array = my_array.reshape(4, 2)  # 4 rows x 2 columns
print('My Array after reshape : ', my_array)

print('My array shape is : ', my_array.shape)

my_array = my_array.reshape(1, 8)  # 1 rows x 8 columns
print('My Array after reshape : ', my_array)
print('My array shape is : ', my_array.shape)

newArr = np.linspace(10,20,5)  # how many elements you want in range from 10 to 20. here taking 5 elements
print('array using linespace API : ', newArr)

index = 0
for item in np.nditer(newArr):
    print('Item at index ', index, ' is ', item)
    index = index + 1