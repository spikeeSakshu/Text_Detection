import cv2
import os
from glob import glob


data_dir= "Dataset/yolo_data/"
txtFiles = glob(data_dir+'*.txt')

output_dir = "Dataset/visualize_annotations/"

num_sample_to_visualize= 10
if num_sample_to_visualize> len(txtFiles):
    num_sample_to_visualize= len(txtFiles)

# Creating save_dir if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for txtFile in txtFiles[:num_sample_to_visualize]:
    
    with open(txtFile, 'r') as fr:
        labelList = fr.readlines()

        imagePath = txtFile.replace('txt', 'jpg')
        image = cv2.imread(imagePath)
        result_name= base_save+ os.path.basename(imagePath)

        for label in labelList:
            label = label.strip().split()
            x = float(label[1])
            y = float(label[2])
            w = float(label[3])
            h = float(label[4])

            # convert x,y,w,h to x1,y1,x2,y2
            H, W, _ = image.shape
            x1 = int((x - w / 2) * W)
            y1 = int((y - h / 2) * H)
            x2 = int((x + w / 2) * W)
            y2 = int((y + h / 2) * H)

            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imwrite(result_name, image)
        
        

