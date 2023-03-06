import numpy as np

def generate_random_array():
    d = np.random.random((5, 2, 3, 7)) #half-open interval [0.0, 1.0)
    # 5X2X3X7
    # 1d array
    np.rand.seed(1)
    np.random.rand(int(1e5)) #uniform [0, 1]
    np.arange(24).reshape((2, 3, 4))

    sampl = np.random.uniform(low=0.5, high=13.3, size=(50,))
    np.random.randint(low=0, high=5, size=(2,))

    np.random.choice(d, size=None, replace=False, p=None) #uniuqe items

    np.linespace(start, stop, num) #inclusive evenly spaced from start to end
    np.random.permutation(10)
    np.random.permutation([1, 4, 9, 12, 15])
    np.random.permutation(arr)

    # bootstrap


d = np.random.random((2,3))
d.flat[3]

def construct_array():
    a = np.random.random((2,3))
    np.zeros_like(a) #return an array of zeros
    x = np.array([[1, 2, 3], [4, 5, 6]])
    np.ravel(x) # 1,2,3,4,5,6

# just related
def generate_random():
    import random
    random.sample(range(low=1, high=100), n=5) #unique random
    return
# statistics
def statistics():
    np.ptp(np.array([[1,2], [2,5]])) #4 largest - smallest (global)
    a = np.arange(5)
    v = np.arange(5)
    np.correlate(a, v) #2 1-d sequences

    X = np.random.random((3, 3))
    Y = np.random.random((3, 3))

    np.cov(X, Y)
    np.corrcoef(X, Y)[0,1] == np.cov(X,Y)[0,1]/(np.std(X, ddof=1)*np.std(Y, ddof=1))

    np.bincount(x, weights=w) #return cutoff


#     auto correlation
    data = np.random.random(20)
    # Mean
    mean = np.mean(data)

    # Variance
    var = np.var(data)

    # Normalized data
    ndata = data - mean

    acorr = np.correlate(ndata, ndata, 'full')[len(ndata) - 1:]
    acorr = acorr / var / len(ndata)


def sorting_search():
    ar = np.random.randint(0, 10)
    np.partition(ar, pivot_ind=7)
    # return a rearranged array with x_i<=ar[pivot_ind], for i<pivot_index
    # x_i>=ar[pivot_ind] for i>=pivot_index

    return
def cov_variance():
    X = np.random.random((3,3))
    Y = np.random.random((3, 3))
    Z = X+Y
    # x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2
def solve_linear_equations(y, coefficient):
    return np.linalg.solve(y, coefficient)

def solve_linear_equation():
    v1 = np.array([[1, 2, 3], [3, 5, 8], [4, 6, 8]])
    v2 = np.array([1, 2, 6])
    sol = solve_linear_equations(v1, v2)

np.linalg.det(np.random.uniform(1,5,(2,2))) #last 2 dimensions must be square

np.trace(M) # sum of diagonals
np.linalg.matrix_rank(M) # rank

# LSE linear regression
# y = mx+c
x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
A = np.vstack([x, np.ones(len(x))]).T
# equivalent to np.concatenate([x.reshape(len(x), 1), np.ones((len(x),1))], axis=1)
m, c = np.linalg.lstsq(A, y, rcond=None)[0]


def dot():
    np.dot(3,4)
    np.dot([2j, 3j], [2j, 3j]) #complex number
    ''' np.vdot handles complex number differently, can only works on vectors of complex numbers'''
    # np.dot(2j, 1j) = -2+0j
    # np.vdot(2j, 1j) = 2+0j

    A = np.random.random((10000, 100))
    B = np.random.random((100, 10))
    C = np.random.random((10, 15))
    D = np.random.random((15, 18))
    np.linalg.multi_dot([A, B, C, D]) == ((A.dot(B)).dot(C)).dot(D)

    def cost(A, B):
        return A.shape[0] * A.shape[1] * B.shape[1]

    a = np.random.random((2,3,4))
    b = np.arange(4)
    np.inner(a, b) == np.tensordot(a, b, axes=(-1, -1))
    # 1D
    # np.inner np.dot
    # 2D
    # dot --> equivalent to matrix multiplication
    # inner --> a sum product over the last axis
# get_angle
def unit_vector(v):
    return v/np.linalg.norm(v)
v1 = np.random.random(5)
v2 = np.random.random(5)
v1_u = unit_vector(v1)
v2_u = unit_vector(v2)

a = np.arccos(np.clip(np.dot(v1_u, v2_u), -1, -1))
def solve_qr():
    a = np.random.randn(9, 6) #9*6
    q, r = np.linalg.qr(a)
    np.allclose(a, np.dot(q, r))
    np.dot(q, r) == np.matmul(q, r) #All True

if __name__ =='__main__':
    pass

