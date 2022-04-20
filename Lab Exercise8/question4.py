class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '(%d,%d,%d)'%(self.x,self.y,self.z)

x = 1
y = 2
z = 3

P=Point3D(x,y,z)
mypoint=repr(P)
print(mypoint)
