# using 'import' keyword
# Alias name for an imported module
# Import part of a module - using 'from' keyword

from builtins import staticmethod

import item

class Order :
    companyName = 'Walmart Inc.' # class level variable -- this variable can
                                                      # be accessed by Class method, but not static method.
    def __init__(self, orderDate, itemList, totalPrice) :
        self.orderDate=orderDate
        self.itemList=itemList
        self.totalPrice=totalPrice

    def  calculateOrderValue(self,itemList) :
        totalPrice=0
        for item in itemList :
             totalPrice+=item.price
        return totalPrice

#   class method - similar to static method in C++, Java
    def changeComanyName(cls,companyNm) :
        Order.companyName = companyNm
        print('After change, Company name : ', Order.companyName, ', Name : ')

#   static method - can not access both class & instance variables.
    @staticmethod
    def checkOrdersCount_ForMonth() :
        # can not access both class & instance variables.
        # print('Company name : ', companyName)
        pass
    def __str__(self) : # similar to toString() , in Java language
        orderDetails='OrderDate : ' + self.orderDate + '\n   '
        for item in self.itemList :
           orderDetails +='\n Item name : ' + item.name
        return orderDetails

item_1 = item.items('Lenova Laptop', 1500)
item_2 = item.items('Dell Laptop', 2200)
order1 = Order('17-Jul-2024',[item_1,item_2] ,0 )

print('Order_1 instance method : ', order1.calculateOrderValue([item_1,item_2]))
print('Order Class method : ', Order.changeComanyName(Order,'Amazon Incorporation'), 'Static method : ' , Order.checkOrdersCount_ForMonth())