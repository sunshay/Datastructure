#!/usr/bin/python

# convert 2 lists to 1 dictionnary
# C = [1,2,3,4]
# D = ['noir','bleu','rouge','gris']
# E = dict(zip(C,D))

# convert list of tuples into dictionnary
# F = [('noir',1),('bleu',2),('rouge',3),('gris',4)]
#G = dict(F)
# keys = G.keys()
# values = G.values()
# print('keys',keys)
# print('values',values)
# print('My dictionnary', G)
#type(G) 

# with a function 
def convertion(F):
    return dict(F)

F = [('or',1),('diamant',2),('saphir',3)]
print(convertion(F))