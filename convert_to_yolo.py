import json
import os
import cv2


all_labels = os.listdir('labels')

for label in all_labels:
    image_name = f'{os.path.splitext(label)[0]}.jpg'
    image_path = os.path.join('images',image_name)
    label_path = os.path.join('labels',label)
    print(label_path)
    
    with open(label_path,'r') as f:
        data = json.load(f)
        img = cv2.imread(image_path)

        image_width = img.shape[0]
        image_height = img.shape[1]

        for i in range(len(data)):
            print(data[i]['Left'])

