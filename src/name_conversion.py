import os
import shutil
import tqdm

src_path_img =  'dataset/SORDI_2022_Single_Assets/SORDI_2022_h4020_warehouse/images/'
src_path_lbl =  'dataset/SORDI_2022_Single_Assets/SORDI_2022_h4020_warehouse/labels/'

dest_path_img = 'dataset/images/'
dest_path_lbl = 'dataset/json_labels/'

img_ext = '_h4020.jpg'
lbl_ext = '_h4020.json'

for img_file in tqdm.tqdm(os.listdir(src_path_img)):
    img = src_path_img + img_file
    dest_img = dest_path_img + img_file[:-4] + img_ext
    shutil.copy(img, dest_img)

for json_file in tqdm.tqdm(os.listdir(src_path_lbl)):
    json = src_path_lbl + json_file
    dest_lbl = dest_path_lbl + json_file[:-5] + lbl_ext
    shutil.copy(json, dest_lbl)