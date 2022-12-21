import json
import cv2

with open('objectclasses.json') as f:
    objects = json.load(f)

class_dict = {}
for classes in objects:
    class_dict[classes['Id']] = classes['Name']


with open('labels/51.json') as f:
    objects_classes = json.load(f)

img = cv2.imread('images/51.jpg')
for objects in objects_classes:
    class_id = objects['ObjectClassId']
    x1 = objects['Left']
    y1 = objects['Top']
    x2 = objects['Right']
    y2 = objects['Bottom']
    print(class_id, x1, y1, x2, y2)
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0))
    
cv2.imshow('box', img)
cv2.waitKey(0)