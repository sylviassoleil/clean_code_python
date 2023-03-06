import scipy.stats

# Perform a hypothesis test to determine whether there is a relationship between the type of operating system a visitor uses and whether they made a purchase.
# scipy.stats.power_divergence(f_obs, f_exp=None, ddof=0, axis=0, lambda_=None)
#
tstat, p = scipy.stats.ttest_ind(X_1, X_2)
tstat, p = scipy.stats.ttest_1samp(X_1, mean_tested)
import numpy as np
from scipy import stats
rng = np.random.default_rng()

rvs1 = stats.norm.rvs(loc=5, scale=10, size=500, random_state=rng)
rvs2 = (stats.norm.rvs(loc=5, scale=10, size=500, random_state=rng)
        + stats.norm.rvs(scale=0.2, size=500, random_state=rng))

# ‘two-sided’, ‘less’, ‘greater’
stats.ttest_rel(rvs1, rvs2, alternative='').pvalue

tstat, p = scipy.stats.normaltest(a)