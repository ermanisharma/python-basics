
#ID returns the memory address of Value not the variable

item1_Price = 20000
item2_Price = 88.765283
item3_Price = item1_Price

print('Id (Memory address) : ', id (item1_Price), id(item2_Price))
print('Compare IDs : ', id (item1_Price) == id(item3_Price) )
print('Compare IDs, using is keyword : ', item1_Price is item2_Price )


