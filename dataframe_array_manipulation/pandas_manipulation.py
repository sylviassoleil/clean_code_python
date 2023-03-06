import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

d = pd.DataFrame({'s':[1,2,3], 't':[2,3,4]})
m = pd.Series([2,3,4])

lower = 2
upper = 3

d.clip(lower, upper)
# if x<=lower --> lower
# if s>upper -->upper

d.s.is_monotonic_increasing()


i = pd.date_range('2018-04-09', periods=4, freq='12H')
ts = pd.DataFrame({'A': [1, 2, 3, 4]}, index=i)

i = pd.date_range('2018-04-09', periods=4, freq='2D')
ts = pd.DataFrame({'A': [1, 2, 3, 4]}, index=i)
ts.first('3D') # return 2018-04-09, 2018-04-11

# auto correlations
d.s.autocorr()
# unbiased standard error
d = d.sem()
# pandas first non-zero
df = pd.DataFrame({'s':[0, 2, 3],
                   't':[1,0,5]})

# lookup is specifically for index manipulations #first non-zero
smallest_ind = df.ne(0).idxmax().to_frame('i').assign(val=lambda d: df.lookup(d.i, d.index))
smallest_ind['v'] = smallest_ind.apply(lambda r: df.lookup(r.i, r.index), axis=0)


num_series = pd.Series(np.arange(15) + np.random.normal(1, 10, 15))

overall = pd.get_dummies(demographics[[col, *groupby_cols]], columns=[col], prefix='', prefix_sep='')
p_df  = pd.pivot_table(df, index=['m'], columns=['s'], values=['t'])
pd.melt(p_df)
user_new = pd.melt(p_df, ignore_index=False, value_name='t').reset_index()

d_melt = pd.melt(d, id_vars=['s', 'o'], value_vars=['a', 't'], var_name='break', value_name='value')

d_pivot = pd.pivot_table(d, index=['t'], columns=['s', 'a'], values=['o'])
d_pivot = d_pivot.reindex(range(len(d_pivot)))
d_delta = d_pivot-d_pivot.shift(1)
d_delta_pct = d_pivot/d_pivot.shift(1) -1
d_m = pd.melt(d_delta)
d_m.drop(columns=[None]).rename(columns={'value': 'chg'})


from functools import reduce

df_final = reduce(lambda left, right: pd.merge(left, right, on=[date_column_name, *identifier_cols]),
                  [])
