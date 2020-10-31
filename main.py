import os
from convert_coco2yolo import convert_json

def creating_folders():
    # Creating output_dir if not exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Creating model_dir if not exists
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

json_file = "Dataset/COCO_Text.json"
image_dir= 'Dataset/train2014/'
output_dir = "Dataset/yolo_data/"
model_dir= 'Models/'

if os.path.exists(image_dir) and os.path.exists(json_file):
    # Converting data from JSON file to YOLO format
    convert_json(json_file)
else:
    print('Please check the path for json and image_dir')
    exit()
