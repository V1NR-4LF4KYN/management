#!/usr/bin/python3

class Student:
    def __init__(self, pName, pId, pAge, pSex, pRoom):
        self.name = pName
        self.id = pId
        self.age = pAge
        self.sex = pSex
        self.room = pRoom

    # getters 
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getAge(self):
        return self.age
    def getSex(self):
        return self.age
    def getRoom(self):
        return self.room
    
    # setters
    def setName(self, pName):
        self.name = pName
    def setId(self, pId):
        self.id = pId
    def setAge(self, pAge):
        self.age = pAge
    def setSex(self, pSex):
        self.age = pSex
    def setRoom(self, pRoom):
        self.room = pRoom