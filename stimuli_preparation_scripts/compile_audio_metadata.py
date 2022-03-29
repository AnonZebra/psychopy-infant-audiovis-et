"""
Go through folders with auditory stimuli and
compile a CSV file that holds sound file name, type and sex. 
"""

# built-in packages
import os
import math
import re
import wave

# 3rd party (pip/pip3 install if needed)
import pandas as pd

# define function for exporting duration of .wav file
def get_wavfile_duration(file_path):
    with wave.open(file_path, 'rb') as input_handle:
        orig_framerate = input_handle.getframerate()
        orig_nframes = input_handle.getnframes()
    wave_duration = orig_nframes / orig_framerate
    return wave_duration

# set path to project root directory
ROOT_DIR = '..'
# specify path (relative to root directory) where resulting CSV is to be saved
CSV_SAVEPATH = (
    'stimuli_specifications/'
    'auditory_stimuli_specifications.csv'
)
# specify names of subdirectories of root directory
ST_DIR = 'stimuli'
AU_DIR = 'audio'
SOC_DIR = 'social'
NSOC_DIR = 'nonsocial'
FEM_DIR = 'female'
MAL_DIR = 'male'

# switch to root directory
os.chdir(ROOT_DIR)
# put together regular expression which matches sound file names
audio_regex = re.compile('.+\.(wav|mp3)$')
# initialize data frame that is to be filled with audio metadata
audio_df = pd.DataFrame(columns=['file_path', 'type', 'sex'])

# put together full paths (from root dir) to stimuli directories
male_dir = os.path.join(ST_DIR, AU_DIR, SOC_DIR, MAL_DIR)
fem_dir = os.path.join(ST_DIR, AU_DIR, SOC_DIR, FEM_DIR)
nsoc_dir = os.path.join(ST_DIR, AU_DIR, NSOC_DIR)

# specify 'mappings' of directories, types and sexes
dirs = [male_dir, fem_dir, nsoc_dir]
types = ['social', 'social', 'nonsocial']
sexes = ['male', 'female', 'nonsocial']
# loop over directories, extracting metadata and putting in
# the data frame
for i, d in enumerate(dirs):
    audio_files = [x for x in os.listdir(d) if audio_regex.match(x)]
    audio_full_paths = [os.path.join(d, audio_file) for audio_file in audio_files]
    for fpath in audio_full_paths:
        audio_duration = get_wavfile_duration(fpath)
        audio_dict = {
            'file_path': fpath,
            'sex': sexes[i],
            'type': types[i],
            'duration': round(audio_duration, 6)
        }
        audio_df = audio_df.append(audio_dict, ignore_index=True)

# export the metadata to CSV
audio_df.to_csv(CSV_SAVEPATH, index=False)

