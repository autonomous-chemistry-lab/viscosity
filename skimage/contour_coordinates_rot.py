import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
rot_img = cv2.imread('2_min20_RC.jpg')

#crop_img = img[600:1050,745:1100]
blur = cv2.GaussianBlur(rot_img, (7, 7), 2)
h, w = rot_img.shape[:2]

# Morphological gradient

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
gradient = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Morphological gradient', gradient)
cv2.waitKey()


lowerb = np.array([0, 0, 0])
upperb = np.array([15, 15, 15])
binary = cv2.inRange(gradient, lowerb, upperb)
cv2.imshow('Binarized gradient', binary)
cv2.waitKey()

# Flood fill from the edges to remove edge crystals

for row in range(h):
    if binary[row, 0] == 255:
        cv2.floodFill(binary, None, (0, row), 0)
    if binary[row, w-1] == 255:
        cv2.floodFill(binary, None, (w-1, row), 0)

for col in range(w):
    if binary[0, col] == 255:
        cv2.floodFill(binary, None, (col, 0), 0)
    if binary[h-1, col] == 255:
        cv2.floodFill(binary, None, (col, h-1), 0)

cv2.imshow('Filled binary gradient', binary)
cv2.waitKey()

foreground = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
foreground = cv2.morphologyEx(foreground, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Cleanup up crystal foreground mask', foreground)
cv2.waitKey()


contours, hierarchy = cv2.findContours(foreground, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(foreground, contours, -1, (255,255,255), 3)
cv2.imshow("cropped", foreground)


cv2.waitKey()

all_pixels=[]

for i in range(0, len(contours)):
   for j in range(0,len(contours[i])):
       all_pixels.append(contours[i][j])

f=open("5_min20_RC.csv", "w")
for item in all_pixels:
       f.write("%s\n" % item)
###
