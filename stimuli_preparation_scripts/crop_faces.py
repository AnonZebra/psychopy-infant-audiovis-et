"""
Crop images of faces from the CFD (https://www.chicagofaces.org/).
Here, shoulders and empty space around the faces is removed, to enable the
faces themselves to take up more of the ROI space.

NOTE that this script saves the cropped images in separate folders
(e.g. 'stimuli/visual/social/male/cropped'). You'll have to replace the
images in the 'actual' stimuli directories with the cropped
versions before they'll actually be used by PsychoPy/in
the experiment.
"""

# imports
import os
from PIL import Image
import pandas as pd
import re

# set path to project root directory
ROOT_DIR = '..'
# specify names of subdirectories of root directory
ST_DIR = 'stimuli'
VI_DIR = 'visual'
SOC_DIR = 'social'
FEM_DIR = 'female'
MAL_DIR = 'male'

# switch to root directory
os.chdir(ROOT_DIR)
# put together regular expression which matches image file names
pic_regex = re.compile('.+\.(jpeg|jpg|png)$')

# put together full paths (from root dir) to stimuli directories
male_dir = os.path.join(ST_DIR, VI_DIR, SOC_DIR, MAL_DIR)
fem_dir = os.path.join(ST_DIR, VI_DIR, SOC_DIR, FEM_DIR)

# specify resulting images' width/height, in pixels
end_width = 1200
end_height = 1500

# specify 'mappings' of directories, types and sexes
dirs = [male_dir, fem_dir]
# loop over directories, cropping all contained images
for i, d in enumerate(dirs):
    cropped_dir_path = os.path.join(d, 'cropped')
    if not os.path.isdir(cropped_dir_path):
        os.mkdir(cropped_dir_path)
    img_files = [x for x in os.listdir(d) if pic_regex.match(x)]
    img_full_paths = [os.path.join(d, img_file) for img_file in img_files]
    for fpath in img_full_paths:
        fname = os.path.basename(fpath)
        img = Image.open(fpath)
        width_diff = img.width - end_width
        crop_rect = (width_diff/2, 0, width_diff/2 + end_width, end_height)
        cropped_img = img.crop(crop_rect)
        cropped_img.save(os.path.join(cropped_dir_path, fname))
