#########################
#--- train and eval ----#
#########################

python train.py -s data_path -m out_path --max_abs_split_points 0 --opacity_cull_threshold 0.05

# render images and (un)bounded TSDF fusion
# Rendering and Extract Mesh
python render.py -m out_path --max_depth 10.0 --voxel_size 0.01

# evaluation


# +++++++++ DTU +++++++++ # 
# scan24, scan37, scan40, scan55, scan63, scan65, scan69, scan83, 
# scan97, scan105, scan106, scan110, scan114, scan118, scan122

python train.py -s ../../Data/DTU/scan24 -m ../exps/full/DTU/scan24 -r 2
python scripts/render_dtu.py -s ../../Data/DTU/scan24 -m ../exps/full/DTU/scan24 -r 2
python scripts/evaluate_dtu_mesh.py --DTU ../../Data/Offical_DTU_Dataset -s ../../Data/DTU/scan24 -m ../exps/full/DTU/scan24

python metrics.py -m ../exps/full/DTU/scan24 -f train

# +++++++++ TNT +++++++++ # 
# Barn, Caterpillar, Courthouse, Ignatius, Meetingroom, Truck
python train.py -s ../../Data/TNT/Barn -m ../exps/full/TNT/Barn -r 2

python metrics.py -m ../exps/full/TNT/Barn -f train
python metrics.py -m ../exps/full/TNT/Barn -f test

# /home/home/raid/zhenhua2023/conda/pgsr