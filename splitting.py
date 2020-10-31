from glob import glob
from random import sample
import shutil
import os

def create_folders(train_dir, val_dir, test_dir):
    
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)

    if not os.path.exists(val_dir):
        os.mkdir(val_dir)
    
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
    
    return

def split_data(data_dir, base_save, train_split, val_split):

    print('\nSplitting the data into Train, Val and Test')
    train_dir= os.path.join(base_save, 'Train')
    val_dir= os.path.join(base_save, 'Val')
    test_dir= os.path.join(base_save, 'Test')

    create_folders(train_dir, val_dir, test_dir)

    images= glob(data_dir+'*.jpg')

    len_train_images= int(len(images)* train_split)
    len_train_images= int(len(images)* val_split)

    for image in sample(images, len_train_images):
        anntotaion_file= image.split('.')[0]+'.txt'
        shutil.copy(image, train_dir)
        shutil.copy(anntotaion_file, train_dir)

        images.remove(image)

    for image in sample(images, len_train_images):
        anntotaion_file= image.split('.')[0]+'.txt'
        shutil.copy(image, val_dir)
        shutil.copy(anntotaion_file, val_dir)

        images.remove(image)

    for image in images:
        anntotaion_file= image.split('.')[0]+'.txt'
        shutil.copy(image, test_dir)
        shutil.copy(anntotaion_file, test_dir)

    print('Done splitting data!!')
    return



