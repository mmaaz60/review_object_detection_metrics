import os
import shutil

annotations_path = "/home/maaz/PycharmProjects/OWOD/datasets/VOC2007/Annotations_Unknown"
mdetr_detections_path = "/home/maaz/PycharmProjects/OWOD/datasets/VOC2007/mdetr_detections"
images_path = "/home/maaz/PycharmProjects/OWOD/datasets/VOC2007/JPEGImages"


all_test_txt_path = "/home/maaz/PycharmProjects/OWOD/datasets/VOC2007/ImageSets/Main/all_task_test.txt"


output_ann_path = "/home/maaz/PycharmProjects/VOC_EVAL/tmp/all_task_ann_pseudo"
output_mdetr_dets_path = "/home/maaz/PycharmProjects/VOC_EVAL/all_task_mdetr_dets"
output_images_path = "/home/maaz/PycharmProjects/VOC_EVAL/all_task_images"

with open(all_test_txt_path, 'r') as f:
    lines = f.read()

image_names = lines.split('\n')

for image in image_names:
    annotation_file_path = f"{annotations_path}/{image}.xml"
    # mdetr_det_file_path = f"{mdetr_detections_path}/{image}.txt"
    # image_path = f"{images_path}/{image}.jpg"
    if os.path.exists(annotation_file_path):
        shutil.copy(annotation_file_path, f"{output_ann_path}/{image}.xml")
    # if os.path.exists(mdetr_det_file_path):
    #     shutil.copy(mdetr_det_file_path, f"{output_mdetr_dets_path}/{image}.txt")
    # if os.path.exists(image_path):
    #     shutil.copy(image_path, f"{output_images_path}/{image}.jpg")
