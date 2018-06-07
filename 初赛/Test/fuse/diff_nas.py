import pandas as pd
b = pd.read_csv('../../data/pred_nasnet.csv', header=None)
b.columns = ['path', 'task', 'label']

for a in b.groupby('task'):
    a[1].to_csv('../../data/nasnet/'+a[0]+'.csv', header = None, index = None)

