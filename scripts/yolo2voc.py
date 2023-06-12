import argparse
import multiprocessing
import os
import xml.etree.ElementTree

from PIL import Image
from pascal_voc_writer import Writer

label_dir = './Dataset/labels'
image_dir = './Dataset/images'
names = ['otomobil','motosiklet','otobus','kamyon','gemi','insan','uap','uai','kepce','tren','vagon','yuk_gemisi']

def yolo2voc(txt_file):
    w, h = Image.open(os.path.join(image_dir, f'{txt_file[:-4]}.jpg')).size
    writer = Writer(f'{txt_file[:-4]}.xml', w, h)
    with open(os.path.join(label_dir, txt_file)) as f:
        for line in f.readlines():
            label, x_center, y_center, width, height = line.rstrip().split(' ')
            x_min = int(w * max(float(x_center) - float(width) / 2, 0))
            x_max = int(w * min(float(x_center) + float(width) / 2, 1))
            y_min = int(h * max(float(y_center) - float(height) / 2, 0))
            y_max = int(h * min(float(y_center) + float(height) / 2, 1))
            writer.addObject(names[int(label)], x_min, y_min, x_max, y_max)
    writer.save(os.path.join(label_dir, f'{txt_file[:-4]}.xml'))

if __name__ == '__main__':
    txt_files = [name for name in os.listdir(label_dir) if name.endswith('.txt')]

    with multiprocessing.Pool(os.cpu_count()) as pool:
        pool.map(yolo2voc, txt_files)
    pool.close()
