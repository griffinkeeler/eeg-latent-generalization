# Evaluating How Latent Dimensionality Affects Cross-Subject Generalization in EEG
___

## Overview
Decoding EEG signals across different subjects is challenging due to the variance of neural signals and the noisy nature of EEG. 
Recent machine-learning methods have addressed the challenges of generalization
by encoding latent representations to generate semantic EEG signals. However, evaluating how the dimensionality of the latent 
space affects cross-subject generalization is largely unstudied. In this project, I will study the robustness of
various latent dimensions across subjects. 

## Representation Learning Using EEGDM
I will use the self-supervised EEG Diffusion Model (EEGDM) proposed by Chang et al. [1] to learn latent representations of the EEG signal.

## Method

### Datasets
For pre-training, the 
The TUH EEG Corpus (TUEG), a rich archive of 
26,846 clinical EEG recordings collected at Temple University Hospital (TUH) from 2002 - 2017, will be used.

Read this [journal paper](https://isip.piconepress.com/publications/journals_refereed/2016/frontiers_neuroscience/tuh_eeg/) 
for a more complete description of the corpus.

### Preprocessing


## References
[1] Shaocong Wang, Tong Liu, Yihan Li, Ming Li, Kairui Wen, Pei Yang, Wenqi Ji, Minjing Yu, and Yong-Jin Liu,
"EEGDM: Learning EEG Representation with Latent Diffusion Model"