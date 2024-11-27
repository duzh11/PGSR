import os

scenes = ['Courthouse', 'Truck', 'Caterpillar', 'Barn', 'Meetingroom', 'Ignatius']
tnt_360_scenes = ['Barn', 'Caterpillar', 'Ignatius', 'Truck']
tnt_large_scenes = ['Meetingroom', 'Courthouse']

data_devices = ['cpu', 'cuda', 'cuda','cuda','cuda', 'cuda']
data_base_path='../../Data/TNT'
out_base_path='../exps/full/TNT'
eval_path='../../Data/Official_TNT_dataset'
gpu_id=0

for id, scene in enumerate(scenes):

    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python train.py -s {data_base_path}/{scene} -m {out_base_path}/{scene} -r2 --eval --ncc_scale 0.5 \
    #     --densify_abs_grad_threshold 0.00015 --opacity_cull_threshold 0.05 --exposure_compensation'
    # print(cmd)
    # os.system(cmd)

    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python scripts/render_tnt.py -m {out_base_path}/{scene} -r2 --eval --use_depth_filter'
    # if scene in tnt_360_scenes:
    #     cmd += ' --voxel_size 0.004 --sdf_trunc 0.016 --max_depth 3.0'
    # elif scene in tnt_large_scenes:
    #     cmd += ' --voxel_size 0.006 --sdf_trunc 0.024 --max_depth 4.5'
    # print(cmd)
    # os.system(cmd)

    # require open3d==0.9
    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python scripts/tnt_eval/run.py --dataset-dir {eval_path}/{scene} --traj-path {data_base_path}/{scene}/{scene}_COLMAP_SfM.log --ply-path {out_base_path}/{scene}/mesh_wo_depth_filter/tsdf_fusion_womask_post.ply --out-dir {out_base_path}/{scene}/mesh_wo_depth_filter'
    print(cmd)
    os.system(cmd)

    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python metrics.py -m {out_base_path}/{scene} -f train'
    # print(cmd)
    # os.system(cmd)

    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python metrics.py -m {out_base_path}/{scene} -f test'
    # print(cmd)
    # os.system(cmd)

    # cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python vis_outputs.py -m {out_base_path}/{scene} -f train test'
    # print(cmd)
    # os.system(cmd)