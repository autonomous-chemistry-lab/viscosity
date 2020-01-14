import cv2
import matplotlib.pyplot as plt

image = cv2.imread('160.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0, cv2.THRESH_BINARY)

#cv2.imshow('Original image', image)
#cv2.imshow('Gray image', gray)
#cv2.imshow('Threshold image', thresh)

crop_img = thresh[250:700, 795:1250]
#cv2.imshow("cropped", crop_img)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(crop_img, contours, -1, (255,255,255), 3)
cv2.imshow("cropped", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()