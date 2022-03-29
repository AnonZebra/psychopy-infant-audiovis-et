"""
Go through attention grabber auditory stimuli dir and compile a CSV file that
holds attention grabber audio sound file names. 
"""

import os
import pandas as pd
import re

# set path to project root directory
ROOT_DIR = '..'
# specify path (relative to root directory) where resulting CSV is to be saved
CSV_SAVEPATH = (
    'stimuli_specifications/'
    'attentiongrabber_audio_specifications.csv'
)
# specify path (relative to root directory) to attention grabber audio directory
ATT_AUDIO_DIR_PATH = 'stimuli/audio/attention_grabbers'

# switch to root directory
os.chdir(ROOT_DIR)
# put together regular expression which matches sound file names
audio_regex = re.compile('.+\.(wav|mp3)$')
# initialize data frame that is to be filled with audio metadata
audio_df = pd.DataFrame(columns=['file_path'])

audio_files = [x for x in os.listdir(ATT_AUDIO_DIR_PATH) if audio_regex.match(x)]
audio_full_paths = [os.path.join(ATT_AUDIO_DIR_PATH, audio_file) for audio_file in audio_files]
for fpath in audio_full_paths:
    audio_dict = {
        'file_path': fpath
    }
    audio_df = audio_df.append(audio_dict, ignore_index=True)

# export the metadata to CSV
audio_df.to_csv(CSV_SAVEPATH, index=False)
