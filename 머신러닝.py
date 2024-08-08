import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg','plas', 'pres','skin','test', 'mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',names=col_names)

# data.describe().to_csv('./results/describe.csv')
# data.corr(method= 'pearson').to_csv('./results/corr.csv')
corr = data.corr(method='pearson')
# print(data.describe())
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(col_names)
ax.set_yticklabels(col_names)
# plt.clf()
# plt.hist(data['preg'])
plt.show()