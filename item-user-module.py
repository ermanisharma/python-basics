class items :
    def __init__(self, name, price) :
        self.name = name
        self.price = price

    def __str__(self):
        print('Name : ', self.name ,'. Price : ', self.price)
        return ''