# Evaluating How Latent Dimensionality Affects Cross-Subject Generalization in EEG
___

## Overview
Decoding EEG signals across subjects remains challenging due to high inter-subject variability and noise. 
Recent representation-learning approaches attempt to address this by learning latent spaces that capture 
subject-invariant structure, yet the role of latent dimensionality in cross-subject generalization remains 
underexplored. In this project, I investigate how latent space dimensionality affects robustness and generalization 
across subjects, testing the hypothesis that an optimal bottleneck exists which balances representational capacity
and noise suppression.

## Representation Learning Using EEGDM
I will use the self-supervised EEG Diffusion Model (EEGDM) proposed by Chang et al. [1] to learn latent representations of the EEG signal.

## Method

### Datasets
For pre-training, the Temple University Abnormal EEG Corpus (TUAB),
a corpus of EEGs that have been annotated as normal or abnormal, will be used. 
Read [Silvia Lopez's MS thesis](https://isip.piconepress.com/publications/ms_theses/2017/abnormal/thesis/) 
for a description of the corpus.

### Preprocessing
19 common EEG channels are selected for pre-training [3]. 
All data is resampled to 200Hz and a fifth-order band-pass Butterworth filter is applied (0.3-80Hz) [2]. 


### Data Augmentation
Zero-masking and amplitude scaling is applied, which were shown to be effective for extracting 
useful features in previous studies [2]. 

### Patching and Embedding
EEG data is segmented into 30-second samples (19 channels x 6,000 time points).
Each patch has a temporal length of 1 second. Each sample has 570 patches (19 x 30). 


## References
[1] Shaocong Wang, Tong Liu, Yihan Li, Ming Li, Kairui Wen, Pei Yang, Wenqi Ji, Minjing Yu, and Yong-Jin Liu,
"EEGDM: Learning EEG Representation with Latent Diffusion Model"

[2] Mostafa 'Neo' Mohsenvand, Mohammad Rasool Izadi, "Contrastive Representation Learning for
Electroencephalogram Classification"

[3]: J. Wang, S. Zhao, Z. Luo, Y. Zhou, H. Jiang, S. Li, T. Li, and G. Pan,
“Cbramod: A criss-cross brain foundation model for eeg decoding,”
International conference on learning representations, 2025.
