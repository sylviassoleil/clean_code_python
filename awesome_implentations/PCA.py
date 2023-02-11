import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from string import ascii_lowercase
cols = ['id', *np.random.choice(list(ascii_lowercase), 5, replace=False)]
data = pd.DataFrame(np.concatenate([np.arange(15).reshape((15,1)), np.random.random((15, 5))], axis=1), columns=cols)
data = data.set_index('id')
data_normalized = data-data.mean()
cov_mat = data_normalized.cov()
eig_values, eig_vectors = np.linalg.eig(cov_mat)


#sorting the eigenvectors

e_indices = np.argsort(eig_values)[::-1]
eigenvectors_sorted = eig_vectors[:,e_indices]

''' explain the variance '''
variance_explained = []
for i in eig_values:
    variance_explained.append(i/sum(eig_values)*100)

# reproject the data
n_compoents = 2
eigenvectors_sorted[:n_compoents]