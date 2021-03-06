# -*- coding: utf-8 -*-
"""lab3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14dhFug525nFaEVgv1Awb_Ki_EP8ZhrMv

Лабораторная работа №3

Выполнил студент группы 18-АС

Чумарина Екатерина

Вариант детектора: 1 (OpenCV)

Вариант сети: 3 (OpenFace)
"""

#!pip install deepface
from deepface import DeepFace
import cv2
import pandas as pd
import matplotlib.pyplot as plt

"""обнаружение лиц"""

def detect_face(img):
    detected_face = DeepFace.detectFace(img, detector_backend = 'opencv')
    plt.imshow(cv2.cvtColor(detected_face, cv2.COLOR_BGR2RGB))

"""Вывод оригинальной фотки"""

def detect_face_orig(img):
    orig = cv2.imread(img)
    plt.imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB))

"""сравнение """

def verify_images(img1, img2, results):
    obj = DeepFace.verify(img1, img2, distance_metric='euclidean', model_name='OpenFace', detector_backend = 'opencv')
    results.append(obj)

"""функция вывода результата"""

def get_verification_results(results):
    count = 1
    for el in results:
        print(str(count)+") " + str(el["verified"]))
        count += 1

imgs = ["/content/drive/MyDrive/lab3/photo_2020.jpg", "/content/drive/MyDrive/lab3/photo_2020_2.jpg","/content/drive/MyDrive/lab3/photo_2020_3.jpg"]
results = []

detect_face_orig(imgs[0])

detect_face_orig(imgs[1])

detect_face_orig(imgs[2])

detect_face(imgs[0])

detect_face(imgs[1])

detect_face(imgs[2])

verify_images(imgs[0], imgs[2], results)
get_verification_results(results)

verify_images(imgs[0], imgs[1], results)
get_verification_results(results)