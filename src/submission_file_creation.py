class_map = {
   0 : 1011,
   1 : 1012,
   2 : 1013,
   3 : 1100,
   4 : 2050,
   5 : 1040,
   6 : 1030,
   7 : 1120,
   8 : 1110,
   9 : 1135,
   10 : 4000,
   11 : 5010,
   12 : 1003,
   13 : 1002,
   14 : 1070,
   15 : 2010,
   16 : 2000
}

class_name_map = {
    1011: 'l_klt_4147',
    1012: 'l_klt_6147',
    1013: 'l_klt_8210',
    1100: 'pallet',
    2050: 'str',
    1040: 'cabinet',
    1030: 'locker',
    1120: 'jack',
    1110: 'dolly',
    1135: 'spring_post',
    4000: 'exit_sign',
    5010: 'fire_extinguisher',
    1003: 'stillage_open',
    1002: 'stillage_close',
    1070: 'cardboard_box',
    2010: 'forklift',
    2000: 'bicycle'
}

import os
import cv2
import numpy as np


text_file_path = '/content/drive/MyDrive/BMW_Hackathon/yolov5/runs/detect/exp2/labels'
img_file_path = '/content/drive/MyDrive/BMW_Hackathon/eval/images'

files = os.listdir(text_file_path)
for label in range(len(files)):
    label_name = files[label].split('.')[0]
    # print(label_name)
    ImageID = f'{label_name}.jpg'
    print(ImageID)
    print(os.path.join(img_file_path,ImageID))
    img = cv2.imread(os.path.join(img_file_path,ImageID))
    i_h = img.shape[0]
    i_w = img.shape[1]

    with open(os.path.join(text_file_path,files[label]), 'r') as f:
        lines = f.readlines()
        for line in lines:
          line = np.float64(line.split(" "))
          cx = float(line[1])
          cy = float(line[2])
          w = float(line[3])
          h = float(line[4])
          Conf = line[5]*100
          class_id = int(line[0])
          object_class_id = class_map[class_id]
          object_name = class_name_map[object_class_id]

          bbox_left = float(cx * img.shape[1] - w * img.shape[1] / 2)
          bbox_top = float(cy * img.shape[0] - h * img.shape[0] / 2)
          bbox_right = float(cx * img.shape[1] + w * img.shape[1] / 2)
          bbox_bottom = float(cy * img.shape[0] + h * img.shape[0] / 2)

          if os.path.exists('submission.csv'):
              with open('submission.csv', 'a') as f:
                text = "\n" + ImageID + ',' + str(i_w)  + ',' + str(i_h) + ',' + str(object_class_id) + ',' + object_name + ',' + str(bbox_left) + ',' + str(bbox_top)+ ',' + str(bbox_right)+ ',' + str(bbox_bottom) + ',' + str(Conf)
                f.write(text)
          else:
              with open('submission.csv', 'w') as f:
                text =  'image_name' + ',' + 'image_width' + ',' + 'image_height' + ',' + 'object_class_id' + ',' + 'object_class_name' + ',' + 'bbox_left' + ',' + 'bbox_top' + ',' + 'bbox_right'+ ',' + 'bbox_bottom' + ',' + 'confidence'
                f.write(text)