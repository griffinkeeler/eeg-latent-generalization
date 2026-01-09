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

    # 19 common EEG channels that will be used
    ch_names = [
        "EEG FP1-REF",
        "EEG FP2-REF",
        "EEG F7-REF",
        "EEG F3-REF",
        "EEG FZ-REF",
        "EEG F4-REF",
        "EEG F8-REF",
        "EEG T3-REF",
        "EEG C3-REF",
        "EEG CZ-REF",
        "EEG C4-REF",
        "EEG T4-REF",
        "EEG T5-REF",
        "EEG P3-REF",
        "EEG PZ-REF",
        "EEG P4-REF",
        "EEG T6-REF",
        "EEG O1-REF",
        "EEG O2-REF",
    ]

    # Selecting the 19 channels
    raw.pick(picks=ch_names)

    # Resample the data to 200Hz
    raw.resample(sfreq=200)

    # Set IIR Filter params
    iir_params = dict(order=5, ftype="butter")

    # Apply the fifth-order Butterworth filter (0.3-80 Hz)
    raw.filter(
        l_freq=0.3,
        h_freq=80,
        method="iir",
        iir_params=iir_params,
        verbose=True,
    )

    # Return the preprocessed raw object
    return raw