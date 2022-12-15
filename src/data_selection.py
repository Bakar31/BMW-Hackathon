import shutil
import os

img_path_source = 'Data/SORDI_2022_Single_Assets/SORDI_2022_h4018_KLT on rack/images/'
label_path_source = 'Data/SORDI_2022_Single_Assets/SORDI_2022_h4018_KLT on rack/labels/json/'

img_path_dest = 'S_Data/SORDI_2022_Single_Assets/SORDI_2022_h4020_warehouse/images/'
label_path_dest = 'json_lbl/'


for i in range(0, len(os.listdir(img_path_source)), 50):
    print('Now copying label - ', i)
    img_src = img_path_source + str(i) + '.jpg'
    lbl_src = label_path_source + str(i) + '.json'
    img_dest = img_path_dest + str(i) + '.jpg'
    lbl_dest = label_path_dest + str(i) + '.json'

    try:
        # shutil.copyfile(img_src, img_dest)
        shutil.copyfile(lbl_src, lbl_dest)
    except:
        pass