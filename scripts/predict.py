from tensorflow import keras
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time
import argparse

setup_gpu('0')

parser = argparse.ArgumentParser(
    prog='predict.py',
    description='Run prediction on retinanet model.',
)

parser.add_argument('-i', '--input', help='Input image', required=True)
parser.add_argument('-o', '--output', help='Output image', required=True)
parser.add_argument('-b', '--backbone', help='Retinanet backbone', default='resnet50')
parser.add_argument('-m', '--model', help='Retinanet model', default='NST-v3.3S-RESNET50-10E.h5')
args = parser.parse_args()

model_path = os.path.join(args.model)
model = models.load_model(model_path, backbone_name=args.backbone)

labels_to_names = [
    'otomobil',
    'motosiklet',
    'otobus',
    'kamyon',
    'gemi',
    'insan',
    'uap',
    'uai',
    'kepce',
    'tren',
    'vagon',
    'yuk_gemisi'
]
image = read_image_bgr(args.input)
draw = image.copy()

image = preprocess_image(image)
image, scale = resize_image(image)

start = time.time()
boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
print("processing time: ", time.time() - start)

boxes /= scale
for box, score, label in zip(boxes[0], scores[0], labels[0]):
    if score < 0.5:
        break
        
    color = label_color(label)
    
    b = box.astype(int)
    draw_box(draw, b, color=color)
    
    caption = "{} {:.3f}".format(labels_to_names[label], score)
    draw_caption(draw, b, caption)

cv2.imwrite(args.output, draw)