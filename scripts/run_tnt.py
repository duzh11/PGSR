import os

scenes = ['Courthouse', 'Truck', 'Caterpillar', 'Barn', 'Meetingroom', 'Ignatius']
data_devices = ['cpu', 'cuda', 'cuda','cuda','cuda', 'cuda']
data_base_path='../../Data/TNT'
out_base_path='../exps/full/TNT'
eval_path='../../Data/Offical_TNT_Dataset'
gpu_id=1

for id, scene in enumerate(scenes):

    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python train.py -s {data_base_path}/{scene} -m {out_base_path}/{scene} -r2 --eval --ncc_scale 0.5 \
    #     --densify_abs_grad_threshold 0.00015 --opacity_cull_threshold 0.05 --exposure_compensation'
    # print(cmd)
    # os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python scripts/render_tnt.py -m {out_base_path}/{scene} -r2 --eval --use_depth_filter'
    print(cmd)
    os.system(cmd)

    # # require open3d==0.9
    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python scripts/tnt_eval/run.py --dataset-dir {data_base_path}/{scene} --traj-path {data_base_path}/{scene}/{scene}_COLMAP_SfM.log --ply-path {out_base_path}/{scene}/{out_name}/mesh/tsdf_fusion.ply --out-dir {out_base_path}/{scene}/{out_name}/mesh'
    # print(cmd)
    # os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python metrics.py -m {out_base_path}/{scene} -f train'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python metrics.py -m {out_base_path}/{scene} -f test'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python vis_outputs.py -m {out_base_path}/{scene} -f train test'
    print(cmd)
    os.system(cmd)