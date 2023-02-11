import json
import random

def ad(a,b):
    if a<b:
        c = a+b
    else:
        c = a-b
    return c

def lambda_handler(event, context):
    x = random.randint(0,50)
    y = random.randint(0,50)
    print(x,y)
    res = ad(x,y)
    
    return res