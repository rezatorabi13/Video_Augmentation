## Video data Augmentation

Data augmentation is a technique that can be used to artificially expand the size of a training dataset by creating modified versions of the data in the dataset. Training deep learning neural network models on more data can result in more skillful models, and the augmentation techniques can create variations of the data that can improve the ability of the fit models to generalize what they have learned to new data. It acts as a regularizer and helps reduce overfitting when training a machine learning model.

In this package we present different methods for video data augmentation. Video data are used in behavioural analysis, action recognition tasks, humsn and motor behaviour in behavioural neuroscience ad so on. In these area video data augmentation plays an important role in preventing overfitting and generalizing the model to perform well on new data. It is important from two points of view. Firstly, deep learning methods needs lots of data for having a good performance while we may not have enough video data in behavioural analysis. Video data augmentation help us to increase the number of video data in our database and improve network performance. Secondley, in behavioural analysis and action recognition, we are intrested in the behaviour and action itself. Using different geometric and color transformation (or a combination of them as a better option), we prevent the network to accosiate color and background information to the classification or regression result.  

### Requirements
This code requires you have the following libraries installed. 
- PIL
- OpenCV
- numpy
- matplotlib
- glob
- Scipy

### Transformations:
We introduce Geometric transformation, Color Transformation and a Compound transformations (A combination of two or more transformations simoltaneously). This transformation apply to the whole video frames.

#### 1-Geometric Trasformations:
We have introduced different geometric transformation such as:
##### 1-1: Horizontal flip:
It is a horizontal mirror reflection of for all frames in the video data
##### 1-2: Shear:
It make a shear transformation with a shear input value randomly in different directions but the same for all the frames of the video data.
##### 1-3: Blur:
A median Blur
##### 1-4: Rotation:
It make a rotation transformation with an angle input value randomly coockwise or counter-clockwise but the same for all the frames of the video data.
##### 1-5: Crop: 
It crops the frame randomly from different sides but the same for all the frames of the video data.
##### 1-6: Translate:
It shifts the video data randomly up/down and left/right.

#### 2- Color Transformations:
We have introduced different Color transformation such as:
##### 2-1- Invert color:
Which changes the value of color channels 
##### 2-2- Gray
Convert the video data to gray style.
##### 2-3- Contrast:
increse or decrease the brighness of the video data randomly base on a contrast input value.
##### 2-4- Compound Transformation:
Compoud transformation is recommended for data augmentation since in introduce more variation in new added data. They combined transformation in this packages are:
- Combination of translation and bluring
- Combination of shear and invert color
- Combination of roration and contrast
- Combination of croping and bluring
- Combination of shear and crop
- Combination of rotation and crop
- Combination of gray style and crop

### Demo:
As a demo, we illustrate som examples in here:

<p align="center">
    <img src="https://github.com/rezatorabi13/Video_Augmentation/blob/main/docs/Original.gif" alt="Figure1" width="280"/>
    <br>
    <em>Original video data.</em>
</p>


<p align="center">
    <img src="https://github.com/rezatorabi13/Video_Augmentation/blob/main/docs/Shear_InvertColor.gif" alt="Figure2" width="280"/>
    <br>
    <em>Combination of Shear and Invert color.</em>
</p>


<p align="center">
    <img src="https://github.com/rezatorabi13/Video_Augmentation/blob/main/docs/Tanslation_Blur.gif" alt="Figure3" width="280"/>
    <br>
    <em>Combination of Translation and Bluring.</em>
</p>


<p align="center">
    <img src="https://github.com/rezatorabi13/Video_Augmentation/blob/main/docs/Rotation_Contrast.gif" alt="Figure4" width="280"/>
    <br>
    <em>Combination of Rotation and Contrast.</em>
</p>


<p align="center">
    <img src="https://github.com/rezatorabi13/Video_Augmentation/blob/main/docs/Crop_Gray.gif" alt="Figure5" width="280"/>
    <br>
    <em>Combination of Gray style and Cropping.</em>
</p>

## Instructions for using the Package

1. Download the repository to your local drive and unzip it.

2. Since in deep learning you need first to extract frame, Transform it using the above methods and then feed those frames into the network, I have assumed that you have alredy extracted your frame. You can copy them in **Original** folder in the package, and then use <code>Augmentation.ipynb</code> for your desire transformation. The package will save the transformed frames (for the augmentation purpose) in **Transformed** folder that has been created in the package. If you would like to personalize the package for your own data or use it as a part of your toolbox, you can modify the path information in <code>paths.py</code>.


3. If you are willing to create videos or animation from you transformed frames (for visualization purpose and etc.) you can use <code>animation.py</code>.

 For more information, refer to the explanation in each script and modules.

### Author
Reza Torabi
