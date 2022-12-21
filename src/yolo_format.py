import cv2
import pybboxes as pbx

img = cv2.imread('./images/1.jpg')
box = (419, 113, 820, 396)
img_width = img.shape[1]
img_height = img.shape[0]

W, H = img_width, img_height 
yolo_boxes = pbx.convert_bbox(box, from_type="voc", to_type="yolo", image_size=(W,H))
print(yolo_boxes)

cx = float(yolo_boxes[0])
cy = float(yolo_boxes[1])
w = float(yolo_boxes[2])
h = float(yolo_boxes[3])

x1 = int(cx * img.shape[1] - w * img.shape[1] / 2)
y1 = int(cy * img.shape[0] - h * img.shape[0] / 2)
x2 = int(cx * img.shape[1] + w * img.shape[1] / 2)
y2 = int(cy * img.shape[0] + h * img.shape[0] / 2)

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('box', img)
cv2.waitKey(0)