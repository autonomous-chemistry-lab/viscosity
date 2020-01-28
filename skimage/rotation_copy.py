import cv2

# read image as grey scale
im = cv2.imread('1_min20.jpg')
img = im[100:1450,345:1600]

# get image height, width
(h, w) = img.shape[:2
         ]
# calculate the center of the image
center = (w / 2, h / 2)

angle90 = 316
angle180 = 180
angle270 = 270

scale = 1

# Perform the counter clockwise rotation holding at the center
# 90 degrees
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

cv2.imshow('Original Image', img)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('Image rotated by 90 degrees', rotated90)
cv2.waitKey(0)  # waits until a key is pressed

cv2.imwrite('1_min20_R.jpg', rotated90, None)
cv2.destroyAllWindows()  # destroys the window showing image