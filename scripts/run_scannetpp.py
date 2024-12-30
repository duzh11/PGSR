import os

scenes = ['8b5caf3398', '116456116b', '13c3e046d7', '0a184cf634', '578511c8a9', '21d970d8de']

data_base_path='../../Data/ScanNetpp'
out_base_path='../exps/full/scannetpp'
gpu_id=2

for id, scene in enumerate(scenes):

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python train.py -s {data_base_path}/{scene} -m {out_base_path}/{scene} -r 2 --eval --ncc_scale 0.5 \
        --densify_abs_grad_threshold 0.00015 --opacity_cull_threshold 0.05 --exposure_compensation'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python scripts/render_scannetpp.py -s {data_base_path}/{scene} -m {out_base_path}/{scene} -r 2 --eval \
        --voxel_size 0.01 --max_depth 5.0 --sdf_trunc 0.05'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python metrics.py -m {out_base_path}/{scene} -f train'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python metrics.py -m {out_base_path}/{scene} -f test'
    print(cmd)
    os.system(cmd)

    cmd = f'CUDA_VISIBLE_DEVICES={gpu_id} python vis_outputs.py -m {out_base_path}/{scene} -f train test'
    print(cmd)
    os.system(cmd)

    # evaluate mesh, depth & normal
    cmd = f"CUDA_VISIBLE_DEVICES={gpu_id} python scripts/eval_geometry.py -s {data_base_path}/{scene} -m {out_base_path}/{scene} \
        -f train test -p tsdf"
    print(cmd)
    os.system(cmd)