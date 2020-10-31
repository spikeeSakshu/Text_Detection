import os
from convert_coco2yolo import convert_json
from splitting import split_data

def create_folders():
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
split_dir= 'Dataset/yolo_data_split/'

train_split = 0.75
val_split= 0.15

if os.path.exists(image_dir) and os.path.exists(json_file):
    # Creating output_dir and model_dir if not exists
    create_folders()

    # Converting data from JSON file to YOLO format
    convert_json(json_file, output_dir, image_dir, model_dir)

    # Splitting the data into Train, Val and Test
    split_data(output_dir, split_dir, train_split, val_split)

else:
    print('Please check the path for json and image_dir')
    exit()
