# EASE experiment data output 

Note: __Avoid__ using Microsoft Excel for handling any data output. Using Excel with CSV files often leads to problems, since Excel tends to ruin the formatting of CSV files. Excel might also do things like not showing all the data (to avoid performance issues) without making this clear, which might lead you to falsely believe there are missing data. If you want a tool similar to Excel, you can try [LibreOffice](https://www.libreoffice.org/), which plays much more nicely with CSV files and is free. 

## Four output files 
For each experiment run, PsychoPy will produce four output files 

* One '.csv' (CSV) file – this is described in more detail further down.
* One '.hdf5' (HDF5) file – this is described in more detail further down.
* One '.log' file – you usually won't use this, as it's not very user-friendly. It's a good idea to save these files though, as they can serve as a backup, allowing you to extract some data you might not have thought to be important earlier. 
* One '.psydat' file – serves a similar purpose to the '.log' file. Just save them in case you eg notice you are interested in something you hadn't (in the .psyexp file) specifically asked PsychoPy to save. If that happens, you'll have to look up the PsychoPy documentation about how to use these files. 

## CSV file 
This file consists of 'core PsychoPy' output. These data are based on a 60Hz refresh rate (i.e. bound to computer screen refreshes) and consists of one row per trial. For this reason, eye tracker data are not included in this raw output CSV file. 

Includes: 
* 'trial_global_start_time' - Time at which trial started, counting from start of experiment. 
* 'att_grab_start_time_intended', 'gaze_to_audio_delay_intended' and similar columns: These describe, counting from trial start time, when PsychoPy was instructed to start the attention grabber, how much delay to include in between gaze capture and audio onset, etc. 
* 'gaze_captured_time' - Time (counting from trial start) at which participant gaze was registered as having been captured, i.e., for 200ms out of last 500ms gaze was directed at attention grabber. 
* 'audio_onset_time', 'visual_offset_time' et c describe when stimuli appeared/disappeared (there is no 'audio_offset_time', as PsychoPy isn't explicitly told to stop playing audio – instead, look at which audio file was played to figure out the audio duration). 
* 'attention_sounds_played' - indicates how many, if any, attention-grabbing sounds the experimenter played during attention grabber phase. 
* 'visual_stimuli_duration_nframes' - number of frames during which visual stimuli were displayed. There are normally 60 frames/second, so if intended duration of visual stimuli was 3s, this should be around 180 frames. (it's normal for this to differ slightly, due to unavoidable technical reasons). 
* 'visual_social_prop', 'visual_geometric_prop' et c – Proportion of time spent by participating looking at the different categories of stimuli. E.g., 0.2 for 'visual_social_prop' means that for 20% of the trial's duration, the participant's gaze was directed at the face stimulus ROI. Note that these values are only for convenient data exploration. They are not as accurate as the raw eye tracker data are, since these values are restricted to a ~60 times/second gaze capture rate. 
* 'visual_social_filepath' et c – Relative (starting from experiment directory) file path to corresponding category's image file. Useful for seeing exactly which image was shown to participant.
* 'visual_social_pos_x'/'visual_social_pos_y' etc – Describes distance of corresponding category's image from center of screen, in degrees. Positive values point in the right/upward direction. E.g. (-2, 8) would mean that the image was centered at 2 visual degrees to the left and 8 degrees up from screen midpoint. 
* 'audio_filepath' - Relative file path to trial sound/audio file. This can be used to figure out what type of audio was played, e.g., the file path 'stimuli/audio/social/female/female_oj.wav' means that a social female recording was played. If a trial was silent, 'silent' is recorded here.
* 'audio_volume': PsychoPy volume setting used for trial. Note that the scale for this goes from 0 to 1, i.e., it cannot be used to figure out physical air pressure/dB values, since this depends on hardware and Windows audio settings. This is used to figure out if a trial was a 'low volume' or 'high volume' trial.
* 'audio_type': Type of played audio stimulus ('social'/'non-social'/'silent').
* 'audio_voice_sex': Sex ('male'/'female') of person whose recorded voice is played, if trial was of type 'social'. For non-social trials, the type name is repeated ('non-social'/'silent') here.
* ‘pause_duration’ - Describes the total duration for which the trial was paused by the experimenter during the ‘attention grabbing phase’. Note that if the experimenter eg paused-unpaused-paused-unpaused, the duration of both pauses will be summed up. If you are interested in looking at attention grabbing phase durations to eg see how alert participants were, you are likely to want to subtract pause durations (since pauses lead to very long attention grabbing phase durations). 
* 'trial_number' - The trial's number (i.e. '1' for first trial, '2' for second...).
* ‘pause_video_fpath’ - Describes the path/file name of video shown during ‘trial intermission’. Note that the column name is potentially misleading – these ‘pause/intermission videos’ are part of the expected experiment sequence and don’t have anything to do with the ‘pause_duration’ (ie breaks from the experiment manually triggered by experimenter) described above.

## HDF5 file
This file holds eye tracker (handled by PsychoPy's 'ioHub' package) output. These data are saved at the resolution used by the eyetracker (as specified in the 'real_eyetracker_config.yaml' file).

The [HDF5 format](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) is very compact and great for storing large amounts of data and helps ensure that experiments won't be sluggish even when collecting high frequency eye tracking data. You can't just open the files in e.g. LibreOffice however. Instead, you need to use specialized software/libraries in e.g. R or Python. For R, you can use the [hdf5r](https://github.com/hhoeflin/hdf5r) package. For Python, you can use the [h5py](https://www.h5py.org/) package (an example of using h5py with PsychoPy output data can be found [here](https://discourse.psychopy.org/t/simulating-eyetrackers/21405/8)).

You can read about the different types of eye tracker data that are included in the data output in the [relevant PsychoPy documentation](https://psychopy.org/api/iohub/device/eyetracker_interface/Tobii_Implementation_Notes.html#supported-event-types) (if the link stops working, Google for 'psychopy iohub tobii implementation notes'). Note that the link/example here is specifically for Tobii eyetrackers - you can search the PsychoPy documentation for corresponding documentation for other eyetrackers.

### R example: access gaze/pupil data
The HDF5 data are organized in a hierarchical fashion. If using the hdf5r package, here's an example of how to access eye tracker data and convert them to an R data frame, then look specifically at left eye gaze horizontal position on computer screen:  

```r
library(hdf5r) 

fpath <- 'path/to/file.hdf5' 

h5f <- H5File$new(fpath, mode="r") 

h5f_eye_events <- h5f[['data_collection']][['events']][['eyetracker']][['BinocularEyeSampleEvent']] 

eyetracker_data_frame <- h5f_eye_events[] 

eyetracker_data_frame$left_gaze_x 

h5f$close_all() 
```

Common types of data (replace `left_gaze_x` in snippet above) you're likely to want to use:

* left_gaze_x, left_gaze_y , right_gaze_x, right_gaze_y to get gaze coordinates in visual angles 
* left_pupil_measure1 and right_pupil_measure1 to get eye pupil diameter in mm


### R example: access 'messages'/event markers
Apart from eye tracker data, the HDF5 files also include 'messages' about trial start etc. These can be accessed (with associated timestamps in the extracted data frame) with 

```r
library(hdf5r) 

fpath <- 'path/to/file.hdf5' 

h5f <- H5File$new(fpath, mode="r") 

h5f_message_events <- h5f[['data_collection']][['events']][['experiment']][['MessageEvent']] 

message_data_frame <- h5f_message_events[] 

message_data_frame$text 

h5f$close_all() 
``` 

These messages include event markers. The most relevant ones are:  

* Start of trial (fixation attention grabber onset) – e.g. "exp1 trial 1 start" 
* End of attention grabber (when gaze was captured) – "exp 1 trial 1 attention grabber end" 
* Sound onset – "exp 1 trial 1 sound onset" 
* Visual onset – "exp 1 trial 1 visual onset" 
* Visual offset – "exp 1 trial 1 visual offset" 

More information about the HDF5 file and ioHub in general can be found here: [https://psychopy.org/api/iohub/](https://psychopy.org/api/iohub/).
 