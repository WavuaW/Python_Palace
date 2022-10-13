class Robot(object):
    pass
x = Robot()
Robot.brand = "KUKU"
print(x.brand) 

x.brand = "Chicken"
print(Robot.brand)

y = Robot()
print(y.brand)

Robot.brand = "Chicken"
print(y.brand)
print(x.brand)
print(x.__dict__)
print(Robot.__dict__)

