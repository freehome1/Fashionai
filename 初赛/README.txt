��base,web�Լ�z_rank����data�ļ�����
�ҵ�python�汾Ϊ3.5 TensorFlow�汾1.4.1 MXnet�汾1.1.0 keras�汾2.1.5
������Ҫtqdm, glob, collections��

1.����/Train/preprocess���е�preprocess.py

2.����/Train/run�е�benchmark.sh�Լ�incres_fine_tuning.ipynb  nasnet_fine_tuning.ipynb
��MXNET_GLUON_REPO=https://apache-mxnet.s3.cn-north-1.amazonaws.com.cn/ bash benchmark.sh ���ն�����benchmark.sh

benchmark.sh�е�����ģ�ͷֱ�Ϊdensenet201�Լ�inceptionv3��ʹ�õĿ��ΪMXNet���˴�������
train_task.py��train_task_299.py�� �ֱ���������ģ�͵�ģ�Ͷ��弰ѵ������

����ipython�ļ��ֱ�Ϊinceptionresnetv2�Լ�NASNETLARGE��ģ�Ͷ���,ѵ�������Լ�Ԥ����,ʹ�ÿ��Ϊkeras


3.����/Test/run�е�benchmark_load.sh�Լ�  ʹ��bash benchmark_load.sh �õ�densenet201�Լ�inceptionv3��Ԥ����


4.����Test/fuse�е�fuse_type.sh�ļ�  ʹ��bash fuse_type.sh����ģ���ں�
�õ����ǵ����ս��:/data/fuse_inc_dense_incres_nas�ļ����е�fuse_all_final.csv�ļ�