##please note that this is not hthe right way to create instances of attributra and it's just me testing out some code 

class Robot:
    pass
x = Robot()
y = Robot()

x.name = "R2-D2"
x.model = "1969"

y.name = "C3PO"
y.model = "1970"

print(y.name, "made in", y.model)
print(x.name, "made in", x.model)

print (x.__dict__)
print (y.__dict__)

