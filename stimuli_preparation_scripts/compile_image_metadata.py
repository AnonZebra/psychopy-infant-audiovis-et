"""
Go through folders with visual stimuli and compile a CSV file that holds image file name, width, height, type and sex. 
"""

# imports
import os
from PIL import Image
import pandas as pd
import re

# set paths to root directory and where to save resulting CSV
ROOT_DIR = os.path.abspath('../')
CSV_SAVEPATH = os.path.join(ROOT_DIR, 'stimuli_specifications', 'visual_stimuli_specifications.csv')
# specify names of subdirectories of root directory
ST_DIR = 'stimuli'
VI_DIR = 'visual'
SOC_DIR = 'social'
NSOC_DIR = 'nonsocial'
ATT_DIR = 'attention_grabbers'
FEM_DIR = 'female'
MAL_DIR = 'male'
GEO_DIR = 'geometrical_shapes'
MANM_DIR = 'manmade_objects'
NAT_DIR = 'natural_objects'

# switch to root directory
os.chdir(ROOT_DIR)

# put together regular expression which matches image file names
pic_regex = re.compile('.+\.(jpeg|jpg|png)$')
# initialize data frame that is to be filled with image metadata
pic_df = pd.DataFrame(columns=['file_path', 'width', 'height', 'type', 'sex'])

# put together full paths (from root dir) to stimuli directories
male_dir = os.path.join(ST_DIR, VI_DIR, SOC_DIR, MAL_DIR)
fem_dir = os.path.join(ST_DIR, VI_DIR, SOC_DIR, FEM_DIR)
geo_dir = os.path.join(ST_DIR, VI_DIR, NSOC_DIR, GEO_DIR)
manm_dir = os.path.join(ST_DIR, VI_DIR, NSOC_DIR, MANM_DIR)
nat_dir = os.path.join(ST_DIR, VI_DIR, NSOC_DIR, NAT_DIR)
att_dir = os.path.join(ST_DIR, VI_DIR, ATT_DIR)

# specify 'mappings' of directories, types and sexes
dirs = [male_dir, fem_dir, geo_dir, manm_dir, nat_dir, att_dir]
types = ['social', 'social', 'geometric', 'manmade', 'natural', 'attention']
sexes = ['male', 'female', 'geometric', 'manmade', 'natural', 'attention']

# loop over directories, extracting metadata and putting in
# the data frame
for i, d in enumerate(dirs):
    img_files = [x for x in os.listdir(d) if pic_regex.match(x)]
    img_full_paths = [os.path.join(d, img_file) for img_file in img_files]
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
            'height': img.height, 
            'sex': sexes[i],
            'type': types[i]
        }
        pic_df = pic_df.append(img_dict, ignore_index=True)

# export the metadata to CSV
pic_df.to_csv(CSV_SAVEPATH, index=False)
