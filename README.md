__WIP: STIMULI NOT UPLOADED YET__

# Infant audiovisual PsychoPy experiment with eyetracking
This is a [Psychopy](https://psychopy.org/) project consisting of a task where an infant is shown visual stimuli and simultaneously played auditory stimuli, while an eyetracker records their gaze.

In each trial of the experiment, the participant is shown an attention grabbing visual stimulus. Once the participant shifts their gaze towards the middle of the screen, a sound is played and shortly thereafter four images are displayed for a few seconds. Finally, a blank screen is displayed for a short duration until the trial ends.

Every 8th trial is followed by a 'distraction video' whose sole purpose is to keep the infant engaged in the task by making the experiment less monotonous.

## Stimuli
Note that you may wish to replace the stimuli to run your own version of the experiment. In that case especially, read the 'Preparation scripts' section below; you'll probably want to modify the code and compnents in the PsychoPy project as well.

Here, descriptions are given as if you were planning on replicating the original experiment.

### Visual stimuli
The visual stimuli consist of:
* Faces
    - From the [Chicago Face Database](https://www.chicagofaces.org/)(CFD). Note that the actual face images aren't included in this repository, for data sensitivity/copyright reasons. Please visit the CFD site to download their material and use it to replace the placeholder images in the subdirectories of 'stimuli/visual/social' yourself.
* Man-made objects
    - For attributions, see 'stimuli/stimuli_attributions.xlsx'.
* Natural objects
    - For attributions, see 'stimuli/stimuli_attributions.xlsx'.
* Computer-rendered geometrical 3D shapes)
    - These were designed and rendered by designer Amanda Gren, using CAD software.

### Auditory stimuli
The auditory stimuli consist of:
* Swedish spoken words/exclamations
    - These were recorded by research assistants (?) Andrietta Stadin and Oskar ??? at Uppsala University.
    - These include recordings of both male and female voices, and these are categorized separately by the experiment.
* Various objects likely to be in the infant's daily surroundings
    - For attributions, see 'stimuli/stimuli_attributions.xlsx'.

### Distraction videos
The distraction videos that were used in the original experiment depicted three women dancing with balloons in their hands and were provided by ???. If you'd like to reproduce the original experiment as closely as possible, please contact ??? to request the videos.

### Stimuli preparation scripts
In the directory 'stimuli_preparation_scripts' there are a few Python scripts that were used when developing the original task for modifying the stimuli, e.g. cropping the CFD images. You may use these if you wish. There are also scripts for generating stimuli metadata files, which are used by the PsychoPy experiment to figure out e.g. where the stimuli are stored. You're very likely to want to run these metadata scripts (e.g. 'stimuli_preparation_scripts/compile_attention_audio_metadata.py'). For more information, read the docstrings at the top of the scripts. If you don't already know how to run stand-alone Python scripts, you will need to look up e.g. a tutorial on YouTube (or, you can manually modify the 'stimuli_specifications' directory files if you prefer).

## Version/setup information
This experiment was originally developed to be run on a Windows computer, with PsychoPy Standalone version 2020.2.10, and a Tobii eyetracker. It's highly recommended that you do comprehensive pilot testing before running it with actual participants. If you're able to, it's recommended that you try to update the experiment to work as well as possible with the most recent version of PsychoPy. Otherwise, the safest option is to simply use PsychoPy v2020.2.10. The 'stimuli preparation scripts' described above were run with Python3.8.

## PsychoPy code
When you open up the project file ('infant_audiovisual_eyetrack.psyexp') with PsychoPy standalone, you'll find that there is a mix of PsychoPy components added through the GUI, and code snippets which implement special functionality necessary for the experiment, and also handle communication with the eyetracker. For more information about the code, read the embedded comments in the code snippets.

## Eyetracker setup
The latest versions of PsychoPy have seen large changes with regard to how eyetracking is handled. You may wish to update this experiment to be more in line with current changes. At a minimum, you will need to update the 'tobii_config.yaml' file with specifications for your eyetracker.

### Eyetracker calibration
This experiment in itself does not include any eyetracker calibration, so do note that you will need to run a calibration before starting. There are various options for running ET calibration in PsychoPy - in the original study where this experiment was used, a modified version of yh-luo's [psychopy_tobii_infant](https://github.com/yh-luo/psychopy_tobii_infant) project was used.

## Contributions
If you notice any problems with the experiment, please start a GitHub issue detailing them. The experiment is not actively developed and it's unlikely that I'll (Lowe) fix any reported errors, but it will help others who'd like to use the experiment know what to expect.

If you improve the experiment and would like to share your work, you are very welcome to start a GitHub pull request. I'll do my best to review and accept pull requests, though I probably won't have time to add to them myself.

If you create a modified (e.g. new set of stimuli) version of the experiment, you can send an e-mail to datalowe@posteo.de and I'll add a link to your work in this README.

## Attribution
If you use this project, either for a replication study or for creating a modified version of the experiment, please give proper attribution. There is no published study on this experiment yet, but in the meantime we ask you to __please include a link to this repository__ in any published articles or similar writings.

The experiment was programmed by Lowe Wilsson according to instructions from, and after discussions with, Terje Falck-Ytter, Ana Maria Portugal and Johan Lundin Kleberg. Andrietta Stadin provided valuable feedback and suggestions for improvements. Amanda Gren created the geometric shapes stimuli. Andrietta Stadin and Oskar ??? made audio recordings. Wilsson collected and prepared all other stimuli.