#"""""""""""""""""
#This module reads contains functions for different geometric transformations.
#""""""""""""""""

#importing necessry libraries
from paths import Frames_Paths
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import cv2
from PIL import Image, ImageEnhance
import scipy.ndimage
from random import seed, random, randint


#loding path's information
path= Frames_Paths.TP
F_path= Frames_Paths.OP

##############################################################################
#Hrizontal flip

def Horizontal_Flip():
    
    video_frames = glob(F_path)
    for i in range(len(video_frames)):
        img=cv2.imread(video_frames[i])
        imghf=np.fliplr(img)
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imghf)
##############################################################################        
#Shear transformation
def shear(x_shear,y_shear):
    video_frames = glob(F_path)
    
    if random()-0.5>0:
        x_shear = x_shear
    else:
        x_shear = -x_shear
    if random()-0.5>0:
        y_shear = y_shear
    else:
        y_shear = -y_shear
    
    for i in range(len(video_frames)):
        img = cv2.imread(video_frames[i])
        rows, cols, ch = img.shape
        transform_mat = np.float32([[1, x_shear, 0], [y_shear, 1, 0]])
        imgSr=cv2.warpAffine(img, transform_mat, (cols, rows))
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgSr)
##############################################################################
#Median Bluring: default b=25
def Blur(b):
    video_frames = glob(F_path)
    for i in range(len(video_frames)):
        img = cv2.imread(video_frames[i])
        img_b = cv2.medianBlur(img,b)
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],img_b)
###############################################################################
#rotating by angle teta
def Rotation(teta):
    video_frames = glob(F_path)
    if random()-0.5>0:
        angle = teta
    else:
        angle = -teta
    for i in range(len(video_frames)):
        img = Image.open(video_frames[i])
        imr = img.rotate(teta)
        imr.save(path+'\\'+video_frames[i].split('\\')[-1])  
###############################################################################
def Crop(w,h):
    video_frames = glob(F_path)
    R=randint(1,4)
    for i in range(len(video_frames)):
        img = cv2.imread(video_frames[i])
        if R==1:
            imgc=img[h:, w:, :]
        elif R==2:
            imgc=img[:-h, w:, :]
        elif R==3:
            imgc=img[h:, :-w, :]
        elif R==4:
            imgc=img[:-h, :-w, :]
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgc)
###############################################################################




