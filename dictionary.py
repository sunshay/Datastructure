#!usr/bin/python3

from multiprocessing.sharedctypes import Value
from textwrap import indent
import json


scone = {
    "sel-raising flour" : "350",
    "baking powder" : "1",
    "butter" : "85",
    "caster sugar" : "3",
    "milk" : "175",
    "egg" : "1"
}
#for key, value in scone.items():
    #print(key, value)
formatted = json.dumps(scone, indent=4)
print(formatted)
