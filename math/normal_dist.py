# Enter your code here. Read input from STDIN. Print output to STDOUT

from scipy.stats import norm as norm
import math


def get_prob_norm(mean, standard_dev, lower_bound=None, upper_bound=None):
    # lower_bound
    # upper_bound
    lb_prob = 0
    ub_prob = 1
    if lower_bound is not None:
        lb_standardized = (lower_bound - mean) / standard_dev
        lb_prob = cdf(lb_standardized)

    if upper_bound is not None:
        up_standardized = (upper_bound - mean) / standard_dev
        ub_prob = cdf(up_standardized)

    return ub_prob - lb_prob

def cdf(x):
    # equivalent is norm.cdf(x)
    return 0.5+math.erf(x/math.sqrt(2))/2

if __name__ == '__main__':
    mean, standard_dev = 30, 4
    inputs = [(None, 40), (21, None), (30, 35)]

    for lb, ub in inputs:
        print(get_prob_norm(mean, standard_dev, lower_bound=lb, upper_bound=ub))
