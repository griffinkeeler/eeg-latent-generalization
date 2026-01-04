import matplotlib.pyplot as plt
from mne.io import read_raw


# TODO: Update docstring and add Butterworth filter
def preprocess(file_path):
    """

    Args:
        file_path (str): The path to the EDF file.
        sfreq (float): The sampling rate in Hertz (Hz).

    Returns:
        mne.Raw: An instance of the mne.Raw class.
    """

    # Load the EEG data
    raw = read_raw(file_path)

    # Resample the data to 200Hz
    raw.resample(sfreq=200)

    raw.plot(start=374, duration=20)



file_path1 = '/Users/griffinkeeler/v2.0.1/edf/000/aaaaaaaa/s001_2015/01_tcp_ar/aaaaaaaa_s001_t000.edf'
preprocess(file_path1)

plt.show()



