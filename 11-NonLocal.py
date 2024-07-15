# NonLocal - used in nested function - to indicate a variable within an inner function
# to say that particular variable is located in the outer function

def outer_fun():
    var = 20
    def inner_fun():
        nonlocal var #to allow outer scope to access this value, only apply to inner scope
        var = 24
        print("The value inside the inner function : ",var)
    inner_fun()
    print("The value inside the inner function : ", var)
outer_fun()

#Example 2

itemPrice = 100

def the_outer_function():
#    global itemPrice
    itemPrice = 10
    def the_inner_function():
        global itemPrice
        itemPrice = 15
#        itemPrice = itemPrice * 2.5 + 35
        print("The value inside the inner function: ", itemPrice)  # 15
    the_inner_function()
    print("The value inside the outer function: ", itemPrice)   # 10

the_outer_function()
print("Main program. ItemPrice : ", itemPrice)