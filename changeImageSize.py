#import insightface
import urllib
import urllib.request
import cv2
import numpy as np
import os


def changeSize(img,rowsize=900):
  res=cv2.resize(img,(rowsize,int(rowsize/img.shape[1]*img.shape[0])),interpolation=cv2.INTER_AREA)
  return res

fileName = r'/Users/alex/Desktop/jpg/test.jpg'
img = cv2.imread(fileName)
image = changeSize(img, rowsize = 800)
cv2.imwrite(r'/Users/alex/Desktop/jpg/test1.jpg',image)