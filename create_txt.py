from glob import glob

data_dir= 'Dataset/'

train_data_dir= 'Dataset/yolo_data_split/Train/'
val_data_dir= 'Dataset/yolo_data_split/Val/'

train_images= glob(train_data_dir+'*.*p*')
val_images= glob(val_data_dir+'*.*p*')

train = open(data_dir+'train.txt' , "w+")
for train_image in train_images:
    train.write(train_image)
    train.write("\n")

val = open(data_dir+'val.txt' , "w+")
    for val_image in val_images:
        val.write(val_image)
        val.write("\n")  