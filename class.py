#!/usr/bin/python
from re import sub


class student():
    def __init__(self,fname,lname,age,section): 
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.section = section

    def introductions(self):
        print("I am " + self.firstname + self.age +" and I have "+ self.age)

subject = student('Mike','Doussey', 35, 'male')
print(subject)
print(subject.introductions)
