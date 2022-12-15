import cv2
import pybboxes as pbx
import json
import os

def convert(file, bboxes):
    path = 'images/'+file[:-5] + '.jpg'
    img = cv2.imread(path)
    W = img.shape[1]
    H = img.shape[0]
    yolo_boxes = pbx.convert_bbox(bboxes, from_type="voc", to_type="yolo", image_size=(W,H))
    return yolo_boxes

for file in os.listdir('labels'):
    path = 'labels/' + file
    # print(path)
    
    with open(path) as f:
        objects_classes = json.load(f)

    for objects in objects_classes:
        try:
            print(objects)
            class_id = objects['ObjectClassId']
            x1 = objects['Left']
            y1 = objects['Top']
            x2 = objects['Right']
            y2 = objects['Bottom']
            bboxes = (x1, y1, x2, y2)
            print(class_id, bboxes)
            
            yolo_boxes = list(convert(file, bboxes))
            text = str(class_id) + ' ' + str(yolo_boxes[0]) + ' ' + str(yolo_boxes[1]) + ' ' + str(yolo_boxes[2]) + ' ' + str(yolo_boxes[3]) + '\n'
            print(text)

            text_path = 'text_labels/' + file[:-4] + '.txt'
            if os.path.exists(text_path):
                with open(text_path, 'a') as text_file:
                    text_file.write(text)
            else:
                with open(text_path, 'w') as text_file:
                    text_file.write(text)
        except:
            pass
                