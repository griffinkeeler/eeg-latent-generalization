import mne

from src.scripts.preprocess import _preprocess


def create_tokens(file_path):

    # The preprocessed Raw object
    raw = _preprocess(file_path)

    # Segment data into 30-second samples (19 channels X 6000 time points)
    epochs = mne.make_fixed_length_epochs(raw, duration=30)

    for ep in epochs:
        # Calculate the number of patches (time points / patch length)
        patch_len = 200
        n_channels, n_times = ep.shape
        n_patches = n_times // patch_len

        # Reshape the data into n-patch segments
        patches = ep.reshape(n_channels, n_patches, patch_len)

        # TODO: Implement channel masking

        # Flatten the patches into tokens
        tokens = patches.reshape(n_channels * n_patches, patch_len)
