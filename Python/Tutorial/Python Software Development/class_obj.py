class Point:
    def setLocation(self, newX, newY):
        self.X = newX
        self.Y = newY

my_point = Point()
my_point.setLocation(2, 5)
print(my_point.X)