# key value pair
# internally bucket are used
# initial bucket size is 8
# 8 diff keys are allowed initially
# clear(), pop()

# for learning purpose alone - hard coded values are used
studentDetails = {'x': 'Saravana', 'y': 'Sumanth', 3: 'Rajesh', 4: 'Vladimir'}

# Printing dictionary
print('Student details : ',studentDetails)

# Accesing value using keys
print("1st name is " + studentDetails['x'])
print("xth name is " + studentDetails['y'])
print("1st name is " + studentDetails[3])
print("xth name is " + studentDetails[4])

# in real time - following approach is used
studentDetails_2 = dict()

print('\n Keys : ', studentDetails.keys())
index = 0
for key in studentDetails.keys():
    print('For  ', index, ', using index, value is ',studentDetails.get(index))
    index += 1

print('\n Values : ',studentDetails.values())
