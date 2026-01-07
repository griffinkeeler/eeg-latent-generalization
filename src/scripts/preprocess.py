from mne.io import read_raw


def _preprocess(file_path):
    """
    Downsamples EEG data to 200 Hz and applies a fifth-order
    Butterworth filter (0.3-80Hz).

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

    # Set IIR Filter params
    iir_params = dict(order=5, ftype="butter")

    # Apply the fifth order Butterworth filter (0.3-80 Hz)
    raw.filter(
        l_freq=0.3,
        h_freq=80,
        method="iir",
        iir_params=iir_params,
        verbose=True,
    )