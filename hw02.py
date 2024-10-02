from sympy import *

def leading_entry_index(a):
    # TODO
    for x in range(a.cols):
        if a[0,x] != 0:
            return x
    return None

def is_echelon(a):
    # TODO
    prev = 0
    zerorow = False
    pos = 0
    for x in range(a.rows):
        if leading_entry_index(a[x,:]) is None:
            zerorow = True
            #pos = 999
            zero = 0
        else:
            if zerorow and leading_entry_index(a[x,:]) is not None:
                return False
            elif leading_entry_index(a[x,:]) is not None:
                pos = leading_entry_index(a[x,:])
                zero = 1

        if pos <= prev and zero != 0:
            return False
        prev = pos

    return True

def is_rref(a):
    # TODO
    if is_echelon(a) == False:
        return False
    
    for x in range(a.rows):
        pos = leading_entry_index(a[x,:])

        if pos is not None:
            if a[x,pos] != 1:
                return False
            
            for y in range(a.rows):
                if y != x and a[y,pos] != 0:
                    return False
    return True

def back_sub(a):
    # TODO
    for x in range(a.rows):
        if leading_entry_index(a[x,:]) is not None:
            y = leading_entry_index(a[x,:])
            a[x,:] /= a[x,y]
            
            for z in range (x):
                a[z, :] = a[z, :] - a[z, y] * a[x, :]
    return None


