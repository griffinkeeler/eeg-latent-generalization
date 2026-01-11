import mne
import torch

from src.scripts.preprocess import preprocess


def create_tokens(file_path):
    """
    Creates a batch of tokens and boolean masks to be inputted
    to the encoder.

    Args:
        file_path (str): The path to the EDF file.

    Returns:
        tokens_batch (torch.Tensor): A batch of tokens with shape (N, C*P, t) where:
            N = The number of epochs (trials/sample)
            C = The number of channels
            P = The number of patches
            t = The window length

        mask_batch (torch.Tensor): A batch of boolean masks with shape (N, C*P)
    """

    # The preprocessed Raw object
    raw = preprocess(file_path)

    # Segment data into 30-second samples (19 channels X 6000 time points)
    epochs = mne.make_fixed_length_epochs(raw, duration=30)

    # Stores the tokens and masks for each epoch
    total_tokens = []
    total_masks = []

    # Shape (N, C, time points)
    data = epochs.get_data()

    for ep in data:
        # Calculate the number of patches (time points / window length)
        window_length = 200
        n_channels, n_times = ep.shape
        n_patches = n_times // window_length

        # Reshape the data into n-patch segments
        patches = ep.reshape(n_channels, n_patches, window_length)

        # Convert numpy array to tensor and preserve float datatype
        patches = torch.from_numpy(patches).float()

        # Threshold for Bernoulli distribution
        r = 0.5

        # Create boolean mask over (channel, patch) indices
        mask_bool = torch.rand(size=[n_channels, n_patches]) < r

        # Flatten the patches into tokens
        tokens = patches.reshape(n_channels * n_patches, window_length)

        # Add masks and tokens to a list
        total_masks.append(mask_bool)
        total_tokens.append(tokens)

    # Shape: (N, C, P)
    masks_batch = torch.stack(total_masks)
    # Shape: (N, C*P)
    masks_batch = masks_batch.reshape(len(total_masks), -1)
    # Shape: (N, C*P, t)
    tokens_batch = torch.stack(total_tokens)

    return tokens_batch, masks_batch