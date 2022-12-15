import cv2
import pybboxes as pbx

def convert(file, bboxes):
    path = ''
    img = cv2.imread(path)
    W = img.shape[1]
    H = img.shape[0]
    yolo_boxes = pbx.convert_bbox(bboxes, from_type="voc", to_type="yolo", image_size=(W,H))