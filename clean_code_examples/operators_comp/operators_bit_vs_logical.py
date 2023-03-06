def log_output(func):
    def wrapper(*arg, **karg):
        out = func(*arg, **karg)
        print('%s is %s' % (func.__name__, out))
        return out
    return wrapper

@log_output
def check_gt(a, b):
    return a>b


@log_output
def check_lt(a, b):
    return a<b



if __name__ == '__main__':
    pass
    res = check_gt(1, 0) or check_lt(0, 1) #True -
    res = check_lt(1, 0) or check_gt(1, 0)
    res = check_lt(1, 0) and check_gt(0, 1) #False -

    # bitwise operator
    bit_res = check_gt(1, 0) | check_lt(0, 1) #will check the both conditions regardless of the result fo the first condition
    bit_and = check_gt(1, 0) & check_lt(0, 1)
    # cond ^ cond = 1 if only 1 of the 2 bits is 1
    # ~cond # invert all the bits
    # x<<2 zero fill left shift, push zeros in from the right
    # a<<n = a*2**n
