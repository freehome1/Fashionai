import pandas as pd

a = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse1.csv', header = None)
b = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse2.csv', header = None)
c = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse3.csv', header = None)
d = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse4.csv', header = None)
e = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse5.csv', header = None)
f = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse6.csv', header = None)
g = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse7.csv', header = None)
h = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse8.csv', header = None)
all = pd.concat([a, b], axis = 0)
all1 = pd.concat([all, c], axis = 0)
all2 = pd.concat([all1, d], axis = 0)
all3 = pd.concat([all2, e], axis = 0)
all4 = pd.concat([all3, f], axis = 0)
all5 = pd.concat([all4, g], axis = 0)
all6 = pd.concat([all5, h], axis = 0)

all6.to_csv('../../data/fuse_inc_dense_incres_nas/fuse_all.csv', header = None, index = None)
a = pd.read_csv('../../data/pred_incres_model.csv', header = None)
b = pd.read_csv('../../data/fuse_inc_dense_incres_nas/fuse_all.csv', header = None)
a.columns = ['path', 'task', 'label']
a1 = a[['path', 'task']]
c = pd.concat([a1,b],axis=1)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse_all_final.csv', header = None, index = None)
