def hi(obj):
    print("Hi, I am " + obj.name + "!")
class Robot:
    pass

x = Robot()
x.name = "Marvin"
hi(x)

# binging the function hi to a class attribute (say_hi)

def hi(obj):
    print ("Hi, I am " + obj.name)

class Robot():
    say_hi = hi # say hi is called a method and is called in the format x.say_hi()

x = Robot()
x.name = "Marvin"
Robot.say_hi(x)
