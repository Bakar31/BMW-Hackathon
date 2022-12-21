import cv2
import pybboxes as pbx
import json
import os
import tqdm

class_map = {
    1011: 0,
    1012: 1,
    1013: 2,
    1100: 3,
    2050: 4,
    1040: 5,
    1030: 6,
    1120: 7,
    1110: 8,
    1135: 9,
    4000: 10,
    5010: 11,
    1003: 12,
    1002: 13,
    1070: 14,
    2010: 15,
    2000: 16
}

def convert(file, bboxes):
    path = 'dataset/images/'+file[:-5] + '.jpg'
    img = cv2.imread(path)
    W = img.shape[1]
    H = img.shape[0]
    yolo_boxes = pbx.convert_bbox(bboxes, from_type="voc", to_type="yolo", image_size=(W,H))
    return yolo_boxes

for file in tqdm.tqdm(os.listdir('dataset/json_labels')):
    path = 'dataset/json_labels/' + file
    
    with open(path) as f:
        objects_classes = json.load(f)
    
    for objects in objects_classes:
        try:
            class_id = int(objects['ObjectClassId'])
            class_id = class_map[class_id]
            x1 = objects['Left']
            y1 = objects['Top']
            x2 = objects['Right']
            y2 = objects['Bottom']
            bboxes = (x1, y1, x2, y2)
            
            yolo_boxes = list(convert(file, bboxes))
            text = str(class_id) + ' ' + str(yolo_boxes[0]) + ' ' + str(yolo_boxes[1]) + ' ' + str(yolo_boxes[2]) + ' ' + str(yolo_boxes[3]) + '\n'

            text_path = 'dataset/labels/' + file[:-5] + '.txt'
            if os.path.exists(text_path):
                with open(text_path, 'r') as text_file:
                    lines = text_file.readlines()
                    if text in lines:
                        pass
                    else:
                        with open(text_path, 'a') as text_file:
                            text_file.write(text)
            else:
                with open(text_path, 'w') as text_file:
                    text_file.write(text)
        except:
            pass