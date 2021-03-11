class Customer:
    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state

    def purchase(self,month):
        print("$200 in "+month)

p1 = Customer("peter","Austin","Washington")
print(p1.name)
print(p1.city)
print(p1.state)
p1.purchase("Sept")