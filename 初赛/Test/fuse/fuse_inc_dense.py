import pandas as pd

a = pd.read_csv('../../data/submission/collar_design_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/collar_design_labels_inceptionv3.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1

for i in c.index:
    c.iloc[i, [10]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[5]] * 0.65)[0]
    c.iloc[i, [11]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[6]] * 0.65)[1]
    c.iloc[i, [12]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[7]] * 0.65)[2]
    c.iloc[i, [13]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[8]] * 0.65)[3]
    c.iloc[i, [14]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[9]] * 0.65)[4]

c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse1.csv', sep = ';', header = None, index = None)


a = pd.read_csv('../../data/submission/neckline_design_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/neckline_design_labels_inceptionv3.csv',header=None,sep=';')
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
    c.iloc[i, [20]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[10]] * 0.65)[0]
    c.iloc[i, [21]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[11]] * 0.65)[1]
    c.iloc[i, [22]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[12]] * 0.65)[2]
    c.iloc[i, [23]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[13]] * 0.65)[3]
    c.iloc[i, [24]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[14]] * 0.65)[4]
    c.iloc[i, [25]] = (c.iloc[i,[5]] * 0.35 + c.iloc[i,[15]] * 0.65)[5]
    c.iloc[i, [26]] = (c.iloc[i,[6]] * 0.35 + c.iloc[i,[16]] * 0.65)[6]
    c.iloc[i, [27]] = (c.iloc[i,[7]] * 0.35 + c.iloc[i,[17]] * 0.65)[7]
    c.iloc[i, [28]] = (c.iloc[i,[8]] * 0.35 + c.iloc[i,[18]] * 0.65)[8]
    c.iloc[i, [29]] = (c.iloc[i,[9]] * 0.35 + c.iloc[i,[19]] * 0.65)[9]
# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse2.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/submission/skirt_length_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/skirt_length_labels_inceptionv3.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1
c['t5'] = 1


for i in c.index:
    c.iloc[i, [12]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[6]] * 0.65)[0]
    c.iloc[i, [13]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[7]] * 0.65)[1]
    c.iloc[i, [14]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[8]] * 0.65)[2]
    c.iloc[i, [15]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[9]] * 0.65)[3]
    c.iloc[i, [16]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[10]] * 0.65)[4]
    c.iloc[i, [17]] = (c.iloc[i,[5]] * 0.35 + c.iloc[i,[11]] * 0.65)[5]

# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse3.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/submission/sleeve_length_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/sleeve_length_labels_inceptionv3.csv',header=None,sep=';')
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
    c.iloc[i, [18]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[9]] * 0.65)[0]
    c.iloc[i, [19]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[10]] * 0.65)[1]
    c.iloc[i, [20]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[11]] * 0.65)[2]
    c.iloc[i, [21]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[12]] * 0.65)[3]
    c.iloc[i, [22]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[13]] * 0.65)[4]
    c.iloc[i, [23]] = (c.iloc[i,[5]] * 0.35 + c.iloc[i,[14]] * 0.65)[5]
    c.iloc[i, [24]] = (c.iloc[i,[6]] * 0.35 + c.iloc[i,[15]] * 0.65)[6]
    c.iloc[i, [25]] = (c.iloc[i,[7]] * 0.35 + c.iloc[i,[16]] * 0.65)[7]
    c.iloc[i, [26]] = (c.iloc[i,[8]] * 0.35 + c.iloc[i,[17]] * 0.65)[8]
# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse4.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/submission/neck_design_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/neck_design_labels_inceptionv3.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1

for i in c.index:
    c.iloc[i, [10]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[5]] * 0.65)[0]
    c.iloc[i, [11]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[6]] * 0.65)[1]
    c.iloc[i, [12]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[7]] * 0.65)[2]
    c.iloc[i, [13]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[8]] * 0.65)[3]
    c.iloc[i, [14]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[9]] * 0.65)[4]

c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse5.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/submission/coat_length_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/coat_length_labels_inceptionv3.csv',header=None,sep=';')
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
    c.iloc[i, [16]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[8]] * 0.65)[0]
    c.iloc[i, [17]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[9]] * 0.65)[1]
    c.iloc[i, [18]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[10]] * 0.65)[2]
    c.iloc[i, [19]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[11]] * 0.65)[3]
    c.iloc[i, [20]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[12]] * 0.65)[4]
    c.iloc[i, [21]] = (c.iloc[i,[5]] * 0.35 + c.iloc[i,[13]] * 0.65)[5]
    c.iloc[i, [22]] = (c.iloc[i,[6]] * 0.35 + c.iloc[i,[14]] * 0.65)[6]
    c.iloc[i, [23]] = (c.iloc[i,[7]] * 0.35 + c.iloc[i,[15]] * 0.65)[7]

# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse6.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/submission/lapel_design_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/lapel_design_labels_inceptionv3.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1

for i in c.index:
    c.iloc[i, [10]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[5]] * 0.65)[0]
    c.iloc[i, [11]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[6]] * 0.65)[1]
    c.iloc[i, [12]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[7]] * 0.65)[2]
    c.iloc[i, [13]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[8]] * 0.65)[3]
    c.iloc[i, [14]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[9]] * 0.65)[4]

c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse7.csv', sep = ';', header = None, index = None)

a = pd.read_csv('../../data/submission/pant_length_labels_densenet201.csv',header=None,sep=';')
b = pd.read_csv('../../data/submission/pant_length_labels_densenet201.csv',header=None,sep=';')
c = pd.concat([a,b], axis=1)
c['t'] = 1
c['t1'] = 1
c['t2'] = 1
c['t3'] = 1
c['t4'] = 1
c['t5'] = 1


for i in c.index:
    c.iloc[i, [12]] = (c.iloc[i,[0]] * 0.35 + c.iloc[i,[6]] * 0.65)[0]
    c.iloc[i, [13]] = (c.iloc[i,[1]] * 0.35 + c.iloc[i,[7]] * 0.65)[1]
    c.iloc[i, [14]] = (c.iloc[i,[2]] * 0.35 + c.iloc[i,[8]] * 0.65)[2]
    c.iloc[i, [15]] = (c.iloc[i,[3]] * 0.35 + c.iloc[i,[9]] * 0.65)[3]
    c.iloc[i, [16]] = (c.iloc[i,[4]] * 0.35 + c.iloc[i,[10]] * 0.65)[4]
    c.iloc[i, [17]] = (c.iloc[i,[5]] * 0.35 + c.iloc[i,[11]] * 0.65)[5]

# d = pd.DataFrame({'label':d})
c.drop(c.columns[[0,1,2,3,4,5,6,7,8,9,10,11]], axis = 1, inplace = True)
c= c.round(8)
c.to_csv('../../data/fuse_inc_dense/fuse8.csv', sep = ';', header = None, index = None)
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
