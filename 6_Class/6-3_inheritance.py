class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def speed_up(self, speed):
        print("move speed to " + speed + " mph")

#p1=Car("Mustang","2019")
#print(p1.model)
#print(p1.year)
#p1.speed_up("100")

class flyingcar(Car):
    pass

p2=flyingcar("flyingcar1","2025")
print(p2.model)
print(p2.year)
p2.speed_up("1000")