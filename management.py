#!/usr/bin/python3

class Manager:
    value = 0
    def Manager(self):
        self.value = 1

    def getValue(self):
        return self.value
    def setValue(self, pValue):
        self.value = pValue


m = Manager()
m.setValue(5)
print(m.getValue())