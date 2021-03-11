class Fish:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def speed_up(self, speed):
        print("Move speed to "+speed+" mph")

p1 = Fish("blue","0.5")
print(p1.color)
print(p1.age)
p1.speed_up("100")