import cv2
import os

def vid_to_frame(video, pathoutputdir):
    vidcap=cv2.VideoCapture(video)
    count=0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(pathoutputdir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

vid_to_frame('/Users/phd19msw/Py_charm/skimage/Video1.mp4', '/Users/phd19msw/Py_charm/skimage/Video1_images')