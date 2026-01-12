import torch


def zero_mask(ep):
    """
    Randomly applies a zero-mask to samples (0-150) in each channel.

    Args:
        ep (ndarray): A sequence of time points from each channel.

    Returns:
        None
    """
    for ch in ep:
        # The number of time points in each sample
        T = ch.shape[0]

        # Random sample size (0-150)
        L = int(torch.randint(0, 151, (1,)))

        # Skip masking if the sample size is 0
        if L == 0:
            continue

        # Random starting position (0, T - L)
        s = int(torch.randint(0, T - L + 1, (1,)))

        # Set the zero-mask to the random segment
        ch[s : s + L] = 0