
class item:
    def calcuate_price(self,x,y):
        return(x*y)

    def get_quantity(self,x):
        return x

    def get_price(self,y):
        return y

    def greet (self):
        print("hello thre!")

def greet (self):
        print("hello! ")

item1 = item()
item1.price = 10
item1.quantity = 4
print(item1.calcuate_price(item1.price,item1.quantity))

item2 = item()
item2.price = 200
item2.quantity =1
print(item2.calcuate_price(item2.price,item2.quantity))

item3 = item()
item3.price = 120
item3.quantity = 2
print(item3.calcuate_price(item3.price,item3.quantity))

print("this is the price: ")
print(item1.get_price(item1.price))
print(item2.get_price(item2.price))
print(item3.get_price(item3.price))

print("This is the quantity: ")
print(item1.get_quantity(item1.quantity))
print(item2.get_quantity(item2.quantity))
print(item3.get_quantity(item3.quantity))

item1.greet()
item2.greet()
item3.greet()



