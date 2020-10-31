import json
import os
import shutil

def save_classes(categories, model_dir):
    sorted_dict=  sorted(categories.items())
    print('\tcoco names', sorted_dict)
    with open(os.path.join(model_dir, 'coco-text.names'), 'w', encoding='utf-8') as f:
        for cls in sorted_dict:
            f.write(cls[1] + '\n')
            
    f.close()

def copy_image_file(image_file, image_dir, output_dir):
    image_path= os.path.join(image_dir, image_file)
    shutil.copy(image_path, output_dir)

def save_txt(anno_dict, coco_name_list, image_dir, output_dir):
    for k, v in anno_dict.items():
        # Transfering the image into output_dir
        copy_image_file(v[0][0], image_dir, output_dir)

        file_name = v[0][0].split(".")[0] + ".txt"

        with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as f:
            # print(k, v)
            for obj in v:

                cat_name = obj[1]
                category_id = coco_name_list.index(cat_name)
                box = ['{:.6f}'.format(x) for x in obj[2]]
                box = ' '.join(box)
                line = str(category_id) + ' ' + box
                f.write(line + '\n')

def bbox_2_yolo(bbox, img_w, img_h):
    
    x, y, w, h = bbox[0], bbox[1], bbox[2], bbox[3]
    centerx = bbox[0] + w / 2
    centery = bbox[1] + h / 2
    dw = 1 / img_w
    dh = 1 / img_h
    centerx *= dw
    w *= dw
    centery *= dh
    h *= dh
    return centerx, centery, w, h

def convert_anno(labels, images_info):
    
    anno_dict = dict()
    for anno_id in labels['anns']:
        bbox = labels['anns'][anno_id]['bbox']
        image_id = labels['anns'][anno_id]['image_id']
        category_id = labels['anns'][anno_id]['class']

        image_info = images_info[image_id]
        image_name = image_info[0]
        img_w = image_info[1]
        img_h = image_info[2]
        yolo_box = bbox_2_yolo(bbox, img_w, img_h)

        anno_info = (image_name, category_id, yolo_box)
        anno_infos = anno_dict.get(image_id)
        if not anno_infos:
            anno_dict[image_id] = [anno_info]
        else:
            anno_infos.append(anno_info)
            anno_dict[image_id] = anno_infos
    return anno_dict
    
def load_images_info(labels):
    images_info = {}
    for image_id in labels['imgs']:

        id_= labels['imgs'][image_id]['id']
        file_name = labels['imgs'][image_id]['file_name']
        w = labels['imgs'][image_id]['width']
        h = labels['imgs'][image_id]['height']
        images_info[id_] = (file_name, w, h)

    return images_info

def find_categories(labels):
    categories = {}
    for cls_id in labels['cats']['class']:
        categories[cls_id] = labels['cats']['class'][cls_id]['name']

    return categories

def convert_json(json_file, output_dir, image_dir, model_dir):
    print('Loading JSON file')
    labels = json.load(open(json_file, 'r', encoding='utf-8'))
    print('Done loading JSON file')

    print('\nGetting unique categories')
    coco_id_name_map = find_categories(labels)
    coco_name_list = list(coco_id_name_map.values())
    print('Total categories: {}'.format(len(coco_id_name_map)))

    print("\nLoading image info...")
    images_info = load_images_info(labels)
    print("Loading done, total images", len(images_info))

    print("\nStart converting...")
    anno_dict = convert_anno(labels, images_info)
    print("Converting done, total labels", len(anno_dict))

    print("\nSaving txt file and transferring images...")
    save_txt(anno_dict, coco_name_list, image_dir, output_dir)
    print("Saving done")

    print("\nSaving 'Coco-text.names' file")
    save_classes(coco_id_name_map, model_dir)
    print("DONE!!")


