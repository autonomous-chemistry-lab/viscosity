import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('22.jpg')

crop_img = img[550:925,695:1350]

cv2.imshow("crop", crop_img)
cv2.waitKey()