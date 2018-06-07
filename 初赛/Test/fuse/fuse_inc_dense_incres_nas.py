import pandas as pd

a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse1.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/collar_design_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1

for i in c.index:
    c.iloc[i, [10]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[5]] * 0.27)[0]
    c.iloc[i, [11]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[6]] * 0.27)[1]
    c.iloc[i, [12]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[7]] * 0.27)[2]
    c.iloc[i, [13]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[8]] * 0.27)[3]
    c.iloc[i, [14]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[9]] * 0.27)[4]

c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse1.csv', sep = ';', header = None, index = None)


a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse2.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/neckline_design_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1
c['t5'] = 1
c['t6'] = 1
c['t7'] = 1
c['t8'] = 1
c['t9'] = 1

for i in c.index:
    c.iloc[i, [20]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[10]] * 0.27)[0]
    c.iloc[i, [21]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[11]] * 0.27)[1]
    c.iloc[i, [22]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[12]] * 0.27)[2]
    c.iloc[i, [23]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[13]] * 0.27)[3]
    c.iloc[i, [24]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[14]] * 0.27)[4]
    c.iloc[i, [25]] = (c.iloc[i,[5]] * 0.73 + c.iloc[i,[15]] * 0.27)[5]
    c.iloc[i, [26]] = (c.iloc[i,[6]] * 0.73 + c.iloc[i,[16]] * 0.27)[6]
    c.iloc[i, [27]] = (c.iloc[i,[7]] * 0.73 + c.iloc[i,[17]] * 0.27)[7]
    c.iloc[i, [28]] = (c.iloc[i,[8]] * 0.73 + c.iloc[i,[18]] * 0.27)[8]
    c.iloc[i, [29]] = (c.iloc[i,[9]] * 0.73 + c.iloc[i,[19]] * 0.27)[9]
# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse2.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse3.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/skirt_length_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1
c['t5'] = 1


for i in c.index:
    c.iloc[i, [12]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[6]] * 0.27)[0]
    c.iloc[i, [13]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[7]] * 0.27)[1]
    c.iloc[i, [14]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[8]] * 0.27)[2]
    c.iloc[i, [15]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[9]] * 0.27)[3]
    c.iloc[i, [16]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[10]] * 0.27)[4]
    c.iloc[i, [17]] = (c.iloc[i,[5]] * 0.73 + c.iloc[i,[11]] * 0.27)[5]

# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse3.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse4.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/sleeve_length_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1
c['t5'] = 1
c['t6'] = 1
c['t7'] = 1
c['t8'] = 1


for i in c.index:
    c.iloc[i, [18]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[9]] * 0.27)[0]
    c.iloc[i, [19]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[10]] * 0.27)[1]
    c.iloc[i, [20]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[11]] * 0.27)[2]
    c.iloc[i, [21]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[12]] * 0.27)[3]
    c.iloc[i, [22]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[13]] * 0.27)[4]
    c.iloc[i, [23]] = (c.iloc[i,[5]] * 0.73 + c.iloc[i,[14]] * 0.27)[5]
    c.iloc[i, [24]] = (c.iloc[i,[6]] * 0.73 + c.iloc[i,[15]] * 0.27)[6]
    c.iloc[i, [25]] = (c.iloc[i,[7]] * 0.73 + c.iloc[i,[16]] * 0.27)[7]
    c.iloc[i, [26]] = (c.iloc[i,[8]] * 0.73 + c.iloc[i,[17]] * 0.27)[8]
# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse4.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse5.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/neck_design_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1

for i in c.index:
    c.iloc[i, [10]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[5]] * 0.27)[0]
    c.iloc[i, [11]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[6]] * 0.27)[1]
    c.iloc[i, [12]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[7]] * 0.27)[2]
    c.iloc[i, [13]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[8]] * 0.27)[3]
    c.iloc[i, [14]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[9]] * 0.27)[4]

c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse5.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse6.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/coat_length_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1
c['t5'] = 1
c['t6'] = 1
c['t7'] = 1


for i in c.index:
    c.iloc[i, [16]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[8]] * 0.27)[0]
    c.iloc[i, [17]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[9]] * 0.27)[1]
    c.iloc[i, [18]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[10]] * 0.27)[2]
    c.iloc[i, [19]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[11]] * 0.27)[3]
    c.iloc[i, [20]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[12]] * 0.27)[4]
    c.iloc[i, [21]] = (c.iloc[i,[5]] * 0.73 + c.iloc[i,[13]] * 0.27)[5]
    c.iloc[i, [22]] = (c.iloc[i,[6]] * 0.73 + c.iloc[i,[14]] * 0.27)[6]
    c.iloc[i, [23]] = (c.iloc[i,[7]] * 0.73 + c.iloc[i,[15]] * 0.27)[7]

# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse6.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse7.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/lapel_design_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1

for i in c.index:
    c.iloc[i, [10]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[5]] * 0.27)[0]
    c.iloc[i, [11]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[6]] * 0.27)[1]
    c.iloc[i, [12]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[7]] * 0.27)[2]
    c.iloc[i, [13]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[8]] * 0.27)[3]
    c.iloc[i, [14]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[9]] * 0.27)[4]

c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse7.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/fuse_inc_dense_incres/fuse8.csv',header=None,sep=';')
b = pd.read_csv('../../data/nasnet/pant_length_labels.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1
c['t5'] = 1


for i in c.index:
    c.iloc[i, [12]] = (c.iloc[i,[0]] * 0.73 + c.iloc[i,[6]] * 0.27)[0]
    c.iloc[i, [13]] = (c.iloc[i,[1]] * 0.73 + c.iloc[i,[7]] * 0.27)[1]
    c.iloc[i, [14]] = (c.iloc[i,[2]] * 0.73 + c.iloc[i,[8]] * 0.27)[2]
    c.iloc[i, [15]] = (c.iloc[i,[3]] * 0.73 + c.iloc[i,[9]] * 0.27)[3]
    c.iloc[i, [16]] = (c.iloc[i,[4]] * 0.73 + c.iloc[i,[10]] * 0.27)[4]
    c.iloc[i, [17]] = (c.iloc[i,[5]] * 0.73 + c.iloc[i,[11]] * 0.27)[5]

# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense_incres_nas/fuse8.csv', sep = ';', header = None, index = None)
# a.drop(a.columns[[0,1]], axis=1, inplace=True)
# b.drop(b.columns[[0,1]], axis=1, inplace=True)
# # #
# a.to_csv('/ext/fashionai/keras/inc_den201_fuse/all_sub_fuse_inc_201_collar.csv',header=None,index=None)
# b.to_csv('/ext/fashionai/keras/incresv2/pred_inceptionresnetv2_collar.csv',header=None,index=None)

# b = pd.read_csv('/ext/fashionai/answer_all/pred_nasnet_fine_tuning_8clf_2.csv',header=None)
# b.columns = ['path', 'task', 'label']
# for i in b.index:
#     if b.at[i, 'task'] != 'neckline_design_labels':
#         b = b.drop([i])
# b.to_csv('/ext/fashionai/keras/pred_nasnet_fine_tuning_neckline.csv', header = None, index = None)
