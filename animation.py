"""""""""
This code makes .gif files from the transformed frames just for visualization
"""""""""

import glob
from PIL import Image

# filepaths
fp_in = "Transformed\\*.jpg"
fp_out = "Transformed.gif"


img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=150, loop=0)