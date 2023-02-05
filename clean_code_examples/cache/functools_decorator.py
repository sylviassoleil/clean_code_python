from functools import lru_cache, cache


def fib_non_cache(n):
    '''
    timeit: 0.18831847838591784
    '''
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=128)
def fib(n):
    '''
    0.04013887136243284
    :param n:
    :return:
    '''
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@cache
def fib_cache(n):
    ''' 0.038320558797568086'''
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def catalan_number(n):
    # todo

    return


output_path = []


def hanoi(n, from_rod, to_rod, aux_rod, output_path):
    # from_rod, to_rod, aux_rod, n
    if n == 0:
        return
    hanoi(n - 1, from_rod, aux_rod, to_rod, output_path)
    print(n, from_rod, to_rod)
    # output_path.append((n, from_rod, to_rod))
    hanoi(n - 1, aux_rod, to_rod, from_rod, output_path)
    return output_path


def tower_of_hanoi_noncache(n, from_rod, to_rod, aux_rod):
    output_path = []
    return hanoi(n, from_rod, to_rod, aux_rod, output_path)


# Tower of Hanoi
# only 1 disk can be moved at a time
# each move consists of taking upper disk from 1 of the stacks and placing it on top of another stack


fib_cache = {1: 1, 2: 2}

def fib_(n):
    # starting from 1
    # n_1 = 1
    # n_2 = 2
    # if n<3:
    #     return n
    if n in fib_cache:
        return fib_cache[n]
    fib_v = fib(n - 1) + fib(n - 2)
    fib_cache.update({n: fib_v})
    return fib_v


def even_fib(n):
    if n == 1:
        return 2
    return even_fib(n - 1) + fib_(3 * n - 1)


def get_even_sum(N):
    n = 1
    while 1:
        fib_n = -1 + 3 * n
        fib_num = fib_(fib_n)
        if fib_num > N:
            return even_fib(n - 1)
        n += 1


if __name__ == '__main__':
    print(get_even_sum(10))
    S
    pass
    n, from_rod, to_rod, aux_rod = 3, 'A', 'C', 'B'
    o = tower_of_hanoi(n, from_rod, to_rod, aux_rod)

    # STOP
    import timeit
    import numpy as np

    input_string = "3, 'A', 'C', 'B'"
    # t_non_cached = np.mean(timeit.repeat(f'tower_of_hanoi({input_string})', setup="from functools_decorator import tower_of_hanoi"))
    t = np.mean(timeit.repeat(f'tower_of_hanoi_noncache({input_string})',
                              setup="from functools_decorator import tower_of_hanoi_noncache"))
    # t_cache = np.mean(timeit.repeat('fib_cache(100)', setup="from functools_decorator import tower_of_hanoi_noncache"))

    # t_non_cached = np.mean(timeit.repeat('fib_non_cache(100)', setup="from functools_decorator import fib_non_cache"))
    # t = np.mean(timeit.repeat('fib(100)', setup="from functools_decorator import fib"))
    # t_cache = np.mean(timeit.repeat('fib_cache(100)', setup="from functools_decorator import fib_cache"))
    # g = timeit.timeit(stmt="generator_sum()", number=10000000, setup="from timeit_func import generator_sum")
