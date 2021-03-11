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

class Tunnelcar(Car):
    def __init__(self,model,year,tunnelmeter,gas_meter):
        super().__init__(model,year)
        self.tunnelmeter = tunnelmeter
        self.gas_meter = gas_meter

    def speed_up(self, speed,power):
        print("move speed to " + speed + " mph, power is " + power)

    def velocity(self, meter):
        print("Velocity meter to " + meter)

p3=Tunnelcar("Tunnelcar1","2025","3000","34")
print(p3.model)
print(p3.year)
p3.speed_up("1000","300")