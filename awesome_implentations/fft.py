import numpy as np

# Fast Fourier Transformation for polynomial multiplication

# A(x) = 6*x**3+7*x**2-10*x+9
# B(x) = (-2)*x**3+4*x-5
# coefficient rep A: (9, -10, 7, 6)
# coefficient rep B: (-5, 4, 0, -2)
# x_k = w_k, w = exp(2pi*i/n)
# interpolation (inverse FFT, IFFT)
co_1 = np.random.rand(int(1e6))
co_2 = np.random.rand(int(1e4))

def polynomial_multiplication_naive(coef_1, coef_2):
    len_co1 = len(coef_1)
    len_co2 = len(coef_2)
    if len_co2+len_co2==2:
        return coef_1[0]*coef_2[0]

    coefficients = [0 for _ in range(len_co2+len_co1-1)]
    for i in range(len_co1):
        for j in range(len_co2):
            coefficients[i+j]+=coef_1[i]*coef_2[j]
    return coefficients

def polymul_method(coef_1, coef_2):
    p1 = np.poly1d(coef_1)
    p2 = np.poly1d(coef_2)
    return np.polymul(p2, p1)

# inverse of DFT
def fft_method(coef_1, coef_2):
    L = len(coef_1) + len(coef_2)
    a_f = np.fft.rfft(coef_1, L) #real valued coefficients
    b_f = np.fft.rfft(coef_2, L)
    return np.fft.irfft(a_f*b_f)

def fft_method_complex(coef_1, coef_2):
    L = len(coef_1) + len(coef_2)
    a_f = np.fft.fft(coef_1, L) #both real & complex valued
    b_f = np.fft.fft(coef_2, L)
    return np.fft.ifft(a_f*b_f)


if __name__ == '__main__':

    # polymul_res = polymul_method(co_1, co_2)
    # coef = polynomial_multiplication_naive(co_1, co_2)
    # coef_fft = fft_method(co_1, co_2)
    # coef_fft_complex = fft_method_complex(co_1, co_2)

    '''performance'''
    import timeit

    fft_res_time = timeit.Timer(lambda: fft_method(co_1, co_2)).timeit(100)
    print('fft_res_time: %s' % (fft_res_time))
    '''fft_res_time: 10.452518927981146 '''

    fft_complex_res_time = timeit.Timer(lambda: fft_method_complex(co_1, co_2)).timeit(100)
    print('fft_complex_res_time: %s' % (fft_complex_res_time))
    ''' fft_complex_res_time: 28.963519667013315 '''
    # polymul_res_time = timeit.timeit(stmt=polymul_res, number=1000, setup="from fft import polymul_method")
    polymul_res_time = timeit.Timer(lambda: polymul_method(co_1, co_2)).timeit(100)
    print('polymul_res_time: %s' % (polymul_res_time))
    '''polymul_res_time: 155.80697801199858'''

    polymul_naive_res_time = timeit.Timer(lambda: polynomial_multiplication_naive(co_1, co_2)).timeit(100)
    # polymul_naive_res_time = timeit.timeit(stmt=coef, number=1000, setup="from fft import polynomial_multiplication_naive")
    print('polymul_naive_res_time: %s' % (polymul_naive_res_time))


    fft_complex_res_time: 28.963519667013315






