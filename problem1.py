#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""
import math
def hypotenuse(b,c,a):
    if a is True:
        A = math.sqrt(b**2 +c**2)
        return(A)
    elif a is False:
        if b > c:
            d = math.sqrt(b**2 - c**2)
            return(d)
        elif c > b:
            d = math.sqrt(c**2 - b**2)
            return(d)

if __name__ == "__main__":
    assert hypotenuse(3,4,True) == 5
    assert hypotenuse(5,12,True) == 13
    assert hypotenuse(3,5,False) == 4
    assert hypotenuse(13,12,False) == 5
    
    