import torch.nn as nn
import torch.nn.functional as F


class TemporalCNN(nn.Module):
    def __init__(self,
                 out_channels=32,
                 kernel_size=20):
        """

        Args:
            out_channels    (int): Number of filters for the convolution layer to learn
            kernel_size     (int): Size of the sliding window
        """
        super().__init__()
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        # out_channels sets the number of filters for the convolution layer to learn
        # The kernal size of 20 allows the model to see neuropsychological related patterns
        self.conv1 = nn.Conv1d(1, out_channels=out_channels, kernel_size=kernel_size)
        self.pool = nn.AdaptiveAvgPool1d(1)

