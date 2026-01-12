import mne
import torch

from src.scripts.preprocess import preprocess
from src.augmentation.augments import zero_mask, amp_scale

def create_tokens(file_path):
    """
    Creates a batch of tokens to be inputted
    to the encoder.

    Args:
        file_path (str): The path to the EDF file.

    Returns:
        tokens_batch (torch.Tensor): A batch of tokens with shape (N, C*P, t) where:
            N = The number of epochs (trials/sample)
            C = The number of channels
            P = The number of patches
            t = The window length
    """

    # The preprocessed Raw object
    raw = preprocess(file_path)

    # Segment data into 30-second samples (19 channels X 6000 time points)
    epochs = mne.make_fixed_length_epochs(raw, duration=30)

    # Stores the tokens and masks for each epoch
    total_tokens = []

    # Shape (N, C, time points)
    data = epochs.get_data()

    for ep in data:

        # Apply amplitude scaling to each channel
        amp_scale(ep)

        # Apply a zero-mask to random samples (0-150) for each channel
        zero_mask(ep)

        # Calculate the number of patches (time points / window length)
        window_length = 200
        n_channels, n_times = ep.shape
        n_patches = n_times // window_length

        # Reshape the data into n-patch segments
        patches = ep.reshape(n_channels, n_patches, window_length)

        # Convert numpy array to tensor and preserve float datatype
        patches = torch.from_numpy(patches).float()

        # Flatten the patches into tokens
        tokens = patches.reshape(n_channels * n_patches, window_length)

        # Add tokens to a list
        total_tokens.append(tokens)

    # Shape: (N, C*P, t)
    tokens_batch = torch.stack(total_tokens)

    return tokens_batch