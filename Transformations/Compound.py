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
#Translation and bluring
def TraslateBlur(x_move,y_move,b):
    video_frames = glob(F_path)
    
    if random()-0.5>0:
        x_move = x_move
    else:
        x_move = -x_move
    if random()-0.5>0:
        y_move = y_move
    else:
        y_move = -y_move
        
    for i in range(len(video_frames)):
        img = cv2.imread(video_frames[i])
        img_b = cv2.medianBlur(img,b)
        rows, cols, ch = img.shape
        transform_mat = np.float32([[1, 0, x_move], [0, 1, y_move]])
        imgTr=cv2.warpAffine(img_b, transform_mat, (cols, rows))
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgTr)  
##############################################################################
#Inverse color as well as applying shear transformation
def ICShear(x_shear,y_shear):
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
        imgi=np.invert(img) #invert color
        transform_mat = np.float32([[1, x_shear, 0], [y_shear, 1, 0]])
        imgSr=cv2.warpAffine(imgi, transform_mat, (cols, rows))
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgSr)
##############################################################################
#Applying Rotation as well as contrast simultaneously
def Rotation_Con(teta,con):
    video_frames = glob(F_path)
    if random()-0.5>0:
        ber=con
    else:
        ber=-con
    if random()-0.5>0:
        te=teta
    else:
        te=-teta
    for i in range(len(video_frames)):
        img = Image.open(video_frames[i])
        enhancer = ImageEnhance.Brightness(img)
        imgC = enhancer.enhance(1+ber)
        imgCr = imgC.rotate(te)
        imgCr.save(path+'\\'+video_frames[i].split('\\')[-1])
##############################################################################
def CropBlur(w,h,b):
    video_frames = glob(F_path)
    R=randint(1,4)
    for i in range(len(video_frames)):
        img = cv2.imread(video_frames[i])
        img_b = cv2.medianBlur(img,b)
        if R==1:
            imgc=img_b[h:, w:, :]
        elif R==2:
            imgc=img_b[:-h, w:, :]
        elif R==3:
            imgc=img_b[h:, :-w, :]
        elif R==4:
            imgc=img_b[:-h, :-w, :]
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgc)
###############################################################################
def shearCrop(x_shear,y_shear,h,w):
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
        imgSC=imgSr[h:-h, w:-w, :]
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgSC)
###############################################################################
def RotationCrop(teta,w,h):
    video_frames = glob(F_path)
    if random()-0.5>0:
        angle = teta
    else:
        angle = -teta
    for i in range(len(video_frames)):
        img = Image.open(video_frames[i])
        imr = img.rotate(angle)
        imn=np.array(imr)
        imrc=imn[h:-h, w:-w, :]
        im_rgb = cv2.cvtColor(imrc, cv2.COLOR_BGR2RGB)
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],im_rgb)
###############################################################################
def CropGray(w,h):
    video_frames = glob(F_path)
    R=randint(1,4)
    for i in range(len(video_frames)):
        img = cv2.imread(video_frames[i])
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if R==1:
            imgc=img_g[h:, w:]
        elif R==2:
            imgc=img_g[:-h, w:]
        elif R==3:
            imgc=img_g[h:, :-w]
        elif R==4:
            imgc=img_g[:-h, :-w]
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgc)
##############################################################################
    