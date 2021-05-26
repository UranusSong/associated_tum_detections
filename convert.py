import json

file_name = "./associated_detections/fr3_office.json"
with open(file_name) as f:
    detect_list = json.load(f)

idx = 0
local_idx = 0
for det in detect_list:
    if(det["image_key"] > idx):
        idx = idx+1
        local_idx = 0
    txt_name = "tracklet_yolo_txt/fr3_office/{:0>6d}.txt".format(idx)
    file = open(txt_name,'a')
    box = det["box"]
    confidence = det["objectness"]
    scores = det["scores"]
    class_id = scores.index(max(scores)) + 1
    track_id = det["object_key"]
    line = "{:d} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:d} {:d}\n".format(
        local_idx,box[0],box[1],box[2],box[3],confidence,class_id,track_id)
    #print(line)
    file.write(line)
    local_idx = local_idx + 1


