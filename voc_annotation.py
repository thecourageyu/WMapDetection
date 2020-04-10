#!/usr/local/bin/python3

import xml.etree.ElementTree as ET

from os import getcwd
import os
import glob


# classes = ["aeroplane",
#            "bicycle",
#            "bird",
#            "boat",
#            "bottle",
#            "bus",
#            "car",
#            "cat",
#            "chair",
#            "cow",
#            "diningtable",
#            "dog",
#            "horse",
#            "motorbike",
#            "person",
#            "pottedplant",
#            "sheep",
#            "sofa",
#            "train",
#            "tvmonitor"]

wd = getcwd()
classes = ["H", "L", "typhoon_center", "warm_front", "cold_front", "stationary_front", "occluded_front", "TD", "TC"]
annotation_dir = "E:/GoogleDrive/ProgramDesign/AIA/AI/AI_projects/DataSet/MomentInvariant"
annotation_dir = "E:/GoogleDrive/DataScience/object_detection"
annotation_dir = "/home/yuzhe/DATA/object_detection"  # 127
annotation_dir = "/NAS-DS1515P/users1/T1/DATA/object_detection/raw_data"
# sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#sets = [(annotation_dir, 'train')]
sets = [(annotation_dir, '2018'), (annotation_dir, '2017')]


def convert_annotation(annotation_file, list_file):
    in_file = open(annotation_file, "r")
    tree = ET.parse(in_file)
    root = tree.getroot()
    print(filename)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        print(cls)
        if cls not in classes or int(difficult) == 1:
            print("Error: something went wrong.")
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


for input_dir, image_set in sets:
    annotations = glob.glob("{0}/{1}/*.xml".format(annotation_dir, image_set))
    print(annotations)
    #list_file = open("{0}.txt".format(image_set), "w")
    list_file = open("annotation.txt", "w")
    for annotation_file in annotations:
        filename = os.path.basename(annotation_file)
        list_file.write("{0}/{1}/{2}.png".format(input_dir, image_set, filename[0:-4]))  # check jpg or png
        convert_annotation(annotation_file, list_file)
        list_file.write('\n')
    list_file.close()

# for year, image_set in sets:
#     annotations = glob.glob("{0}/*.xml".format(annotation_dir))
#     image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt' % (year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt' % (year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg' % (wd, year, image_id))
#         convert_annotation(year, image_id, list_file)
#         list_file.write('\n')
#     list_file.close()


