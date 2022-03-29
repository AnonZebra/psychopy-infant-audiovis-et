"""
# Resample audio files
PsychoPy, when used on Windows, isn't compatible with playing sounds/sound files that have varying sample rates. If one tries to load sounds of varying sample rates, PsychoPy raises an error similar to this: 

> psychopy.exceptions.SoundFormatError: Tried to create audio stream ... but ... already exists and win32 doesn't support multiple portaudio streams

It's probably a good idea either way to make sure that all stimuli have the same sample rate. For this reason, this script goes through and replaces all sound files with 44.1kHz versions, using the [librosa package](https://github.com/librosa/librosa) and the [soundfile package](https://github.com/bastibe/python-soundfile).

NOTE that this script actually replaces the original audio files - you'll
need to modify the last line (.write()) if you want the original files
to be left alone. (but it's recommended that you instead simply
copy the sound files to a separate directory first, and let this
script overwrite the originals to avoid issues with having
both original and resampled versions in the stimuli folders)
"""

# built-in packages/modules
import os
import re 

# 3rd party packages
import librosa
import soundfile

# set path to root directory
ROOT_DIR = '..'

# specify names of subdirectories of root directory
ST_DIR = 'stimuli'
AU_DIR = 'audio'
SOC_DIR = 'social'
NSOC_DIR = 'nonsocial'
FEM_DIR = 'female'
MAL_DIR = 'male'
ATT_AUDIO_DIR_PATH = 'stimuli/audio/attention_grabbers'

# switch to root directory
os.chdir(ROOT_DIR)
# put together regular expression which matches sound file names
audio_regex = re.compile('.+\.(wav|mp3)$')

# put together full paths (from root dir) to stimuli directories
male_dir = os.path.join(ST_DIR, AU_DIR, SOC_DIR, MAL_DIR)
fem_dir = os.path.join(ST_DIR, AU_DIR, SOC_DIR, FEM_DIR)
nsoc_dir = os.path.join(ST_DIR, AU_DIR, NSOC_DIR)

dirs = [male_dir, fem_dir, nsoc_dir, ATT_AUDIO_DIR_PATH]

# loop over directories, finding audio files and resampling them
# to 44.1kHz
for i, d in enumerate(dirs):
    audio_files = [x for x in os.listdir(d) if audio_regex.match(x)]
    audio_full_paths = [os.path.join(d, audio_file) for audio_file in audio_files]
    for fpath in audio_full_paths:
        y, s = librosa.load(fpath, sr=44100) # Resample to 44.1kHz
        soundfile.write(fpath, y, 44100)
