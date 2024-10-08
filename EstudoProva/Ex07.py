class Access:
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c

v = Access("A", "B", "C")
print(v.public)
v._protected = "P"
print(v._protected)
print(v._Access__private)
print(v.__private)
