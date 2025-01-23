#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(a,b):
    for i in a:
        g = i
        for j in b:
            h = j
            if j > i:
                Δx = j - i
            elif i > j:
                Δx = i - j
            break
        break
    for i in a:
        if i == g:
            continue
        else:
            for j in b:
                if j == h:
                    continue
                else:
                    if j > i:
                        Δy = j - i
                    elif i > j:
                        Δy = i - j
                break
        break
    W = math.sqrt(Δx**2 + Δy**2)
    return(W)

if __name__ == "__main__":
    d = distance( (2,4) , (6,3) )
    assert round(d,3) == 4.123
    d = distance( (-3,2.2) , (1,2))
    assert round(d,3) == 4.005


