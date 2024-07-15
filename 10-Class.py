# Class

class person:
    def __init__(self, name, age:int, place): # This is the constructor with 2 params
        self.name = name # initilizing values from param
        self.age = age   # initilizing values from param
        print('Name is ', name,' & age is ', age,' from ', place)

# Calling class
p1 = person("Manish", '30', 'India')