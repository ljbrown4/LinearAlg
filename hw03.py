from matlib import *

def vec_scale(val, vec):
    # TODO
    scaled = [(val * vec.get_entry(x)) for x in range(vec.num_entries)]
    scale = Vector(scaled,vec.num_entries)

    return scale

def vec_add(v1, v2):
    # TODO
    if v1.num_entries != v2.num_entries:
        raise Exception("DIMENSION MISMATCH")
    '''
    added = []

    for x in range(v1.num_entries):
        adds = v1.get_entry(x) + v2.get_entry(x)
        added += [adds]
    add = Vector(added,v1.num_entries)
    '''
    added = [(v1.get_entry(x) + v2.get_entry(x)) for x in range (v1.num_entries)]
    add = Vector(added,v1.num_entries)

    return add

def vec_inner(v1, v2):
    # TODO
    if v1.num_entries != v2.num_entries:
        raise Exception("DIMENSION MISMATCH")
    '''
    inner_product = 0

    for x in range(v1.num_entries):
        prod = v1.get_entry(x) + v2.get_entry(x)
        inner_product += prod
    '''
    inner_product = sum((v1.get_entry(x) * v2.get_entry(x)) for x in range (v1.num_entries))

    return inner_product

def mat_vec_mul(a, v):
    # TODO
    if v.num_entries != a.cols:
        raise Exception("DIMENSION MISMATCH")
    '''
    multiplied = []

    for x in range(a.rows):
        vrow = a.get_row(x)
        multiplied += [(vec_inner(vrow,v))]
    mult = Vector(multiplied, a.rows)
    '''
    multiplied = [(vec_inner(a.get_row(x),v)) for x in range(a.rows)]
    mult = Vector(multiplied,a.rows)

    return mult



