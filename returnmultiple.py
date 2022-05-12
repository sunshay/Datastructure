#!/usr/bin/python

class verification():
    def __init__(self):
        self.str = "ok"
        self.x = 20

def fun():
    return verification()

t = fun()
print(t.str)
print(t.x) #call method fun in the verification class
    
       
        

