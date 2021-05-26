# dataset information
detector used: YOLOv3 trained on COCO. 

Detections have been manually associated to categorize which detections belong to the same object.


# detection format:

'object_key': integer representing the unique object id

'image_key': integer representing image key

'image_path': relative path in the TUM dataset

'box': float image coordinates in xmin,ymin,xmax,ymax format

'objectness': float objectness score

'scores': softmax class scores (80)


# 修改
frame id
track id
class id
class name
box xyxy
score

txt_name 000000.txt (image key)

local_id x y x y confidence class_id track_id
0 237.05 93.32 390.44 231.22 0.99 63 track_id