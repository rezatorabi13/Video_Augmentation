#"""""""""""""""""
#This module reads contains functions for different color transformations.
#""""""""""""""""

#importing necessry libraries
from paths import Frames_Paths
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import cv2
from PIL import Image, ImageEnhance
import scipy
from random import seed, random, randint


#loding path's information
path= Frames_Paths.TP
F_path= Frames_Paths.OP
###############################################################################

def Gray():
    video_frames = glob(F_path)
    for i in range(len(video_frames)):
        img = Image.open(video_frames[i]).convert('L') #Converting to gray (Removing color channel)
        img.save(path+'\\'+video_frames[i].split('\\')[-1])        
##############################################################################

def Contrast(con):
    video_frames = glob(F_path)
    if random()-0.5>0:
        ber=con
    else:
        ber=-con
    for i in range(len(video_frames)):
        img = Image.open(video_frames[i])
        enhancer = ImageEnhance.Brightness(img)
        imgCr = enhancer.enhance(1+ber)
        imgCr.save(path+'\\'+video_frames[i].split('\\')[-1])
##############################################################################
#invert color
def InvertColor():
    video_frames = glob(F_path)
    for i in range(len(video_frames)):
        img=cv2.imread(video_frames[i])
        imgi=np.invert(img)
        cv2.imwrite(path+'\\'+video_frames[i].split('\\')[-1],imgi)
##############################################################################





