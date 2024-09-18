import os

scenes = [24, 37, 40, 55, 63, 65, 69, 83, 97, 105, 106, 110, 114, 118, 122]
data_base_path='../../Data/DTU'
out_base_path='../exps/full_womask/DTU'
eval_path='../../Data/Offical_DTU_Dataset'
gpu_id=0

for scene in scenes:

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python train.py -s {data_base_path}/scan{scene} -m {out_base_path}/scan{scene} -r2 --ncc_scale 0.5'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python scripts/render_dtu.py -m {out_base_path}/scan{scene} -r2'
    print(cmd)
    os.system(cmd)

    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python scripts/dtu_eval.py --data {out_base_path}/scan{scene}/mesh/tsdf_fusion.ply \
    #     --scan {scene} --mode mesh --dataset_dir {eval_path} --vis_out_dir {out_base_path}/scan{scene}/mesh'
    # print(cmd)
    # os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python metrics.py -m {out_base_path}/scan{scene} -f train'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python vis_outputs.py -m {out_base_path}/scan{scene} -f train'
    print(cmd)
    os.system(cmd)