# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:48:29 2021

@author: search
"""
import cv2
import numpy as np

img = cv2.imread('30-legos.jpg', cv2.IMREAD_GRAYSCALE)

#img22=cv2.imread('',cv2.IMREAD_LOAD_GDAL)
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True

print(cv2.__version__)

if cv2.__version__.startswith('2.'):
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# detect the blobs in images
keyPoints = detector.detect(img)

print('Total Lego in image are {}'.format(len(keyPoints)))

imgKeyPoints = cv2.drawKeypoints(img, keyPoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# display keypoints
cv2.imshow('hello image', imgKeyPoints)
cv2.waitKey(0)

cv2.destroyAllWindows()
