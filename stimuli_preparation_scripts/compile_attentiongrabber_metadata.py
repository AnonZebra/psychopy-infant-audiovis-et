# imports
import os
from PIL import Image
import pandas as pd
import re

# set path to root directory and where to save resulting CSV
ROOT_DIR = os.path.abspath('../')
CSV_SAVEPATH = os.path.join(ROOT_DIR, 'stimuli_specifications', 'attentiongrabber_images_specifications.csv')
# specify path (relative to root directory) to attention grabber images directory
ATT_IMG_DIR_PATH = 'stimuli/visual/attention_grabbers'

# switch to root directory
os.chdir(ROOT_DIR)
# put together regular expression which matches image file names
pic_regex = re.compile('.+\.(jpeg|jpg|png)$')
# initialize data frame that is to be filled with image metadata
pic_df = pd.DataFrame(columns=['file_path', 'width', 'height'])

# extract image files' metadata and put in
# the data frame
img_files = [x for x in os.listdir(ATT_IMG_DIR_PATH) if pic_regex.match(x)]
img_full_paths = [os.path.join(ATT_IMG_DIR_PATH, img_file) for img_file in img_files]
# replace all back slashes (\) with forward slashes (/) in file path,
# to ensure that paths are formatted the same way regardless of whether
# this script is run on Windows (which uses \ for file paths) or
# Linux/Mac
img_full_paths = [p.replace('\\', '/') for p in img_full_paths]
for fpath in img_full_paths:
    img = Image.open(fpath)
    img_dict = {
        'file_path': fpath,
        'width': img.width,
        'height': img.height
    }
    pic_df = pic_df.append(img_dict, ignore_index=True)

# export the metadata to CSV
pic_df.to_csv(CSV_SAVEPATH, index=False)
