import numpy as np
import cv2 as cv
import sys


im = cv.imread('160.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret,thresh= cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(im, contours, -1, (0,255,0), 3)
print(contours)
