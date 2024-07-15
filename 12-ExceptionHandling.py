# Exception Handling

# initializing the variables
var1 = 4
var2 = 0

try:
   d = var1 // var2
   print(d)
except ZeroDivisionError:
    print("Exception because of divide by zero")
except:
    print("Catch general exception")
finally:
    print("This is finally block")
# using assert keyword
print("The value of var1 / var2 : ")
# assert var2 != 0, "Divide by 0 error"


try:
    assert var2 != 0, "Divide by 0 error!"
except AssertionError:
    print('Assertion error')