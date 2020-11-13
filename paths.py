"""
This script contains information that is needed to be modified for your own data.
You need to create 2 folders. A folder containning  extracted frames from your video files,
and a folder that the transformed frames is saved there. The path for these folders are
OP , and TP, respectively.

OP (Original path) is the path for the folder where the original video frames are located.
TP (Transform path) is the path for the folder where the Transformed video frames are saved. 
"""


     
class Frames_Paths:
    #Paths
    OP = 'Original\\*.jpg' #(Original path) is the path for the folder where the original video frames are located.
    TP = 'Transformed'     #(Transform path) is the path for the folder where the Transformed video frames are saved.