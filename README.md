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

file named by frame idx
txt format:
local_id xmin ymin xmax ymax confidence class_id track_id