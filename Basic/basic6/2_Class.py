class firstclass:
    def add (self, v1, v2):
        return v1 + v2
    def sub(self, v1, v2):
        return v1 - v2

class Class2(firstclass):
    def __init__(self, v1, v2):
        self.v_1 = v1
        self.v_2 = v2
    def add2 (self, v1):
        return v1 + self.v_1
    def sub2 (self, v1):
        vl = self.v_2 - v1
        return vl

Cls = Class2(20, 10)
v1 = Cls.add(1,2)
v2 = Cls.add(1,2)
v3 = Cls.add2(5)
v4 = Cls.sub2(5)

print v1 , ', ' ,v2 , ', ' ,v3 , ', ' ,v4