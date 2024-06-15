# Write circle_calc() function that takes radius
#  of a circle as an input from user and then it
#  calculates and returns area, 
# circumference and diameter. 
# You should get these values in your main program 
# by calling circle_calc function and 
# then print them

import math # import the math module

def circle_calc(radius):
    
    diameter = radius*2
    circumference = 2 * math.pi * radius
    area = math.pi* radius ** 2

    return {"diameter":diameter,"circumference":circumference,"area":area}

value=circle_calc(1)

for k ,v in value.items():
    print(f"{k} ==> {v} ")


