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
For pre-training, the Temple University Abnormal EEG Corpus (TUAB),
a corpus of EEGs that have been annotated as normal or abnormal, will be used. 
Read [Silvia Lopez's MS thesis](https://isip.piconepress.com/publications/ms_theses/2017/abnormal/thesis/) 
for a description of the corpus.

### Preprocessing
All data is resampled to 200Hz and a fifth-order band-pass Butterworth filter is applied (0.3-80Hz), as done in 
Mohsenvand and Izadi's paper [2]. 

## References
[1] Shaocong Wang, Tong Liu, Yihan Li, Ming Li, Kairui Wen, Pei Yang, Wenqi Ji, Minjing Yu, and Yong-Jin Liu,
"EEGDM: Learning EEG Representation with Latent Diffusion Model"

[2] Mostafa 'Neo' Mohsenvand, Mohammad Rasool Izadi, "Contrastive Representation Learning for
Electroencephalogram Classification"
