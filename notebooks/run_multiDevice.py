
from muselsl import stream, list_muses, view, record
from multiprocessing import Process
from mne import Epochs, find_events
from time import time, strftime, gmtime, sleep
import os
from stimulus_presentation import visual_p300_stripes
from utils import utils
from collections import OrderedDict
import warnings

duration = 10

# Set the stream type as:
type_openBCI = 'EEG_OpenBCI'

def main():

    # start a background process that will stream data from the first available Muse
    # muse = list_muses()
    stream_process = Process(target=stream, args=(None, 'auto', None, 'Muse-1C44'))
    stream_process.start()

    sleep(30)

    # Manually launch lsl stream from OpenBCI


    # prepare for data recording
    record_process_Muse = Process(target=record, args=(duration, None, False, "EEG"))
    record_process_OpenBCI = Process(target=record, args=(duration, None, False, type_openBCI))

    # prepare for stimulus presentation
    stimulus = Process(target=visual_p300_stripes.present, args=(duration,))

    # launch all processes
    stimulus.start()
    record_process_Muse.start()
    record_process_OpenBCI.start()
    stream_process.terminate()

if __name__ == '__main__':
    main()
