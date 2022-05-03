# Experiment translation
The original experiment was run in Swedish. However, there are only a few things you need to change in order to run the experiment in another language.

## Text messages
There is:
* A 'loading screen' message displayed at the very start of the experiment, which asks the participant (really the participant's parent) to please wait.
* A 'start screen' message displayed after loading finishes, and just before the first trial begins.
* An 'end screen' message.

All messages are specified in a code snippet:
1. Open up the .psyexp file and go to the 'Setup' routine.
2. Click the 'code_setup' code component.
3. Scroll down to the bottom of the 'Before Experiment' tab code and edit the `LOAD_MESSAGE`, `BEGIN_MESSAGE` and `END_MESSAGE` as follows:

```python
## messages to participant ##
# load screen message.
# "Please wait for a bit..."
LOAD_MESSAGE = (
    "Vänligen vänta lite..."
)

# start screen message.
# "It's starting now!"
BEGIN_MESSAGE = (
    "Nu börjar det!"
)

# end screen message.
# "With that, the experiment is finished."
# "Thank you!"
END_MESSAGE = (
    "Nu är experimentet klart.\n"
    "Tack!"
)
```

```python
## messages to participant ##
# load screen message.
# "Please wait for a bit..."
LOAD_MESSAGE = (
    "Please wait for a bit..."
)

# start screen message.
# "It's starting now!"
BEGIN_MESSAGE = (
    "It's starting now!"
)

# end screen message.
# "With that, the experiment is finished."
# "Thank you!"
END_MESSAGE = (
    "With that, the experiment is finished.\n"
    "Thank you!"
)
```
Note that the example is in English, but you can enter whatever you want. Take care not to remove the quotation marks or the `\n` part, as they are necessary for Python/PsychoPy to understand how the text should be formatted.

## Audio recordings
The original experiment's voice/social audio stimuli are stored in 'stimuli/audio/social/female' and 'stimuli/audio/social/male'. The following words/exclamations are used:
* 'Boll' - 'Ball'
* 'Hejsan' - 'Hello'/'Hiya'
* 'Oj' - 'Whoops'/'Whoopsie'

You can replace these audio files with whatever you like. After doing so, you should run the script 'stimuli_preparation_scripts/compile_audio_metadata' with Python. There is more information at the top of the script (can be opened with notepad). If you haven't used Python on its own at all before, you'll need to install it ([https://www.python.org/downloads/](https://www.python.org/downloads/)) and install the [pandas](https://pypi.org/project/pandas/) package. There are many YouTube videos which give beginner-friendly introductions to installing Python and running scripts, so you can try searching there for help.

If you're not very familiar with Python/PsychoPy, it's recommended that you stick to using 3 audio files in each category. This is because if you want to change the number of different audio/image stimuli that are used, you'll need to make some more comprehensive updates to the PsychoPy project.