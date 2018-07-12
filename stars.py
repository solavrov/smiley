def my_sum(*args):
    s = 0
    for e in args:
        s += e
    return s


def cube_vol(**kwargs):
    return kwargs['x']*kwargs['y']*kwargs['z']

