def maximo (x,y,z):
    if x > y:
        return x
    if y > x and y > z:
        return y
    else:
        return z
