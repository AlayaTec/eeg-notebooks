# EEG Notebooks


### NOTE:
This is a fork of [https://github.com/amandakeasson/eeg-notebooks.git](https://github.com/amandakeasson/eeg-notebooks.git), with modifications so that multiple other devices (currently OpenBCI Ganglion) can be running together alone with MUSE with signals synchronized.

This repo is a work in progress with the goal of making it easy to perform  experiments (with [PsychoPy](https://www.psychopy.org)) and automatically analyze data.

For a mid-term goal, this tool is to integrated into the repo of [Report-Pipelines](https://github.com/AlayaTec/Reporting-Pipeline).

Currently, a collection of classic EEG experiments implemented in Python and Jupyter notebooks. All experiments are implemented for the EEG devices MUSE and OpenBCI and based on work done by Alexandre Barachant and Hubert Banville for the [muse-lsl](https://github.com/alexandrebarachant/muse-lsl) library.

Please see the [documentation](http://eeg-notebooks.readthedocs.io/) for advanced installation instructions and complete info about the project.


## Getting MUSE prepared

Follow installation instructions [here](http://eeg-notebooks.readthedocs.io/en/latest/setup_instructions_windows.html).

If you are a Mac user, follow the installation instructions [here](https://github.com/AlayaTec/eeg-notebooks/blob/master/mac_multi_devices_instructions_neurobrite.docx).

Make sure your device is turned on and run the following code. It should detect and connect to the device and begin 'Streaming...' If the device is not found or the connection times out, try running this code again

Connect to the desired Muse
`muselsl stream --name [name_of_Muse]`
*Name for Muse 1: Muse-5EAD. Name for Muse 2: Muse-1C44.*

View the streamed data
`muselsl view -v 2`

To stream data from all sensors in a Muse 2 from the command line:
`muselsl stream --ppg --acc --gyro`

For details refer to [here](https://github.com/alexandrebarachant/muse-lsl).

## Getting OpenBCI prepared

Install the OpenBCI GUI [here](https://github.com/OpenBCI/OpenBCI_GUI).

Follow the instructions to connect OpenBCI Ganglion from [here](https://docs.openbci.com/Tutorials/02-Ganglion_Getting%20Started_Guide) and start data stream.

Under the Networking block on OpenBCI GUI, change the Data Type of Stream 1 to 'TimeSeries'. Change the Type of Stream 1 to 'EEG_OpenBCI'.


## Running Experiments
Seat the subject in front of the computer and run the following code to run a single trial of the experiment.
In order to maximize the possibility of success, participants should take the experiment in a quiet environment and do their best to minimize movement that might contaminate the signal. With their jaw and face relaxed, subjects should focus on the stimuli, mentally noting when they perceive the oddball stimulus.
Data will be recorded into CSV files in the eeg-notebooks/data directory

Go to the directory ~/eeg-notebooks/notebooks, run

`python run_multi-devices_stim.py --duration [duration_of_session] --subject [index_of_subject] --run [index_of_block] --experiment [name_of_experiment]`

Currently available experiments:
- N170 (Faces & Houses), name_of_experiment is 'n170'.
- SSVEP, name_of_experiment is 'ssvep'.
- Visual P300, name_of_experiment is 'visual_p300_stripes'.

Visualizing ERPs requires averaging the EEG response over many different rounds of stimulus presentation. Depending on experimental conditions, this may require as little as one two minute trial or as many as 6. We recommend repeating the above experiment 3-6 times before proceeding.
Make sure to take breaks, though! Inattention, fatigue, and distraction will decrease the quality of event-related potentials.


## Analyze the data
You can now open the notebook associated with your experiment (N170, P300, SSVEP).
Run the first cell that imports all the tools you will need, then skip to Step 4.
Replace subject and session with the subject and session you wish to analyze.
