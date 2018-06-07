num_gpus=1
num_workers=32


python train_task.py --task collar_design_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task.py --task neckline_design_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task.py --task skirt_length_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task.py --task sleeve_length_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task.py --task neck_design_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task.py --task coat_length_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task.py --task lapel_design_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task.py --task pant_length_labels --model densenet201 --num-gpus $num_gpus -j $num_workers --epochs 20

python train_task_299.py --task collar_design_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task_299.py --task neckline_design_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task_299.py --task skirt_length_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task_299.py --task sleeve_length_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task_299.py --task neck_design_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task_299.py --task coat_length_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task_299.py --task lapel_design_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20
python train_task_299.py --task pant_length_labels --model inceptionv3 --num-gpus $num_gpus -j $num_workers --epochs 20



