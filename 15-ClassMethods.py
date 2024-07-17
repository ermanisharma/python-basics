# ClassMethod :: it'll have cls keyword in param
# StaticMethod :: can not access both classes
# instanceMethod :: it'll have self keyword in param


class Order:
    itemName = "Smart Watch"
def __init__(self):
    def instanceMethodClass(self):
        return Order.itemName
    def classMethodClass(cls,item):
        Order.itemName = item
        return 'Item name is : ' + Order.itemName

print('class method called : ',Order.classMethodClass(Order,'Smartphone'))
print('instance method called : ',Order.instanceMethodClass())