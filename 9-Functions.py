# user defined function -- def is short form for definition
# def add():
#     a = 50
#     b = 40
#     c = 30

#global variable
customerList = ['Ray','Brown']
orderList = ['Mobile','Laptop']

print('Customer list : ', customerList)
def placeOrder():
    # local variable here inside a function
    # Always declare global in starting of functions
    global customerList
    customerList = ['AA', 'BB']

    isOrdered = True
    customerAddress = '45,Mount Road, New Delhi'
    print('Order placed : ', isOrdered , '. Address : ', customerAddress)

    # custoemrList = ['AA','BB'] # It will replace the values in existing customerList variable
    print('Customer list : ', customerList) #gloabl var accessible but if available in local scope it will access that one



placeOrder()

# print('Customer list : ', customerList)