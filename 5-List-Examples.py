# similar to arrays
# mixed data types allowed
# concatenation using + operator on list can be applied
itemsInOrder = [111, 222, 'Samsung Mobile','Mobile Case']

itemsInOrder2 = list() # initialize list using constructor

itemsInOrder2.append(itemsInOrder[0])
itemsInOrder2.append(itemsInOrder[1])
itemsInOrder2.append('OTG')

print('Items in Order 2 : ', itemsInOrder2)

itemsInOrder3 = ['Charger']

itemsInOrder3[0] = 'iPhone' # Allowed for List

# Copy - make a copy of all the items to variable
itemsInOrder4 = itemsInOrder3.copy()

print('All items are : ', itemsInOrder2 + itemsInOrder4)

index = 0
itemsInOrder5 = list()

for item in itemsInOrder:
    index = index + 1
    if index == 1:
        itemsInOrder5.append(itemsInOrder[index])
print('Item in 5 : ', itemsInOrder5)