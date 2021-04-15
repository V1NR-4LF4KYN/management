#!/usr/bin/python3

class Manager:
    value = 0
    def __init__(self):
        self.value = 1
    def __init__(self, sValue):
        self.value = sValue


    def getValue(self):
        return self.value
    def setValue(self, pValue):
        self.value = pValue


m = Manager(244)
n = Manager(3)
print(n.getValue())
#m.setValue(5)
print(m.getValue())
