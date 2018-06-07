将base,web以及z_rank放入data文件夹中
我的python版本为3.5 TensorFlow版本1.4.1 MXnet版本1.1.0 keras版本2.1.5
另外需要tqdm, glob, collections库

1.运行/Train/preprocess当中的preprocess.py

2.运行/Train/run中的benchmark.sh以及incres_fine_tuning.ipynb  nasnet_fine_tuning.ipynb
用MXNET_GLUON_REPO=https://apache-mxnet.s3.cn-north-1.amazonaws.com.cn/ bash benchmark.sh 在终端运行benchmark.sh

benchmark.sh中的两个模型分别为densenet201以及inceptionv3，使用的框架为MXNet，此处调用了
train_task.py和train_task_299.py， 分别是这两个模型的模型定义及训练代码

两个ipython文件分别为inceptionresnetv2以及NASNETLARGE的模型定义,训练代码以及预测结果,使用框架为keras


3.运行/Test/run中的benchmark_load.sh以及  使用bash benchmark_load.sh 得到densenet201以及inceptionv3的预测结果


4.运行Test/fuse中的fuse_type.sh文件  使用bash fuse_type.sh进行模型融合
得到我们的最终结果:/data/fuse_inc_dense_incres_nas文件夹中的fuse_all_final.csv文件