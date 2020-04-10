#!/bin/bash


#model_weigt="./logs/000/trained_weights_stage_1.h5"
model_weigt="./logs/000/trained_weights_final.h5"
classes="./model_data/predefined_classes.txt"
input_dir="/home/yuzhe/DATA/object_detection/resize_data"
#input_dir="/NAS-DS1515P/users1/T1/DATA/object_detection/raw_data/2018"
output_dir="/home/yuzhe/DATA/object_detection/output"

python3 yolo_video.py --image --input ${input_dir} --output ${output_dir} --model_path ${model_weigt} --classes_path ${classes}
#python3 yolo_video.py --input ${input_dir} --output ${output_dir} --model ${model_weigt} --classes ${classes}
