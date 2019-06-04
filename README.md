# Machine Learning in Exoplanet Exploration
## Udacity Machine Learning Engineer Nanodegree
## Capstone Project

### Description

In 2009, NASA launched the Kepler Space Telescope into space. The spacecraft's mission was to detect Earth-sized exoplanets in our galaxy using an approach known as the transit method. The telescope watched a particular area of the sky containing about 150,000 stars for over nine years. It monitored each of the stars and aimed at detecting small dips in the brightness of their light, as planets pass in front of them during their orbit. The data collected by the telescope consists of measurements of the light intensity of a star at regular time intervals. These measurements are known as flux data or flux time-series.

The Kepler mission ended in 2013 due to a severe malfunction of the telescope. However, NASA engineers managed to find a way of restabilising the spacecraft using sunlight pressure. This made it possible for the telescope to continue exploring space, giving birth to a new mission, named K2. K2 has collected flux data from hundreds of thousands of stars so far, many of which have not been classified yet. Moreover, the mission is still active, monitoring more and more stars.

Classifying a star as having exoplanets or not based on the Kepler measurements currently involves a lot of time-consuming, manual analysis of the flux data by astrophysicists. It is therefore believed that machine learning techniques could be utilised to make this process more efficient and aid the exoplanet exploration efforts.

The objective of this project is to develop a machine learning tool that detects exoplanet candidates directly from the raw flux time-series data collected by NASA's Kepler telescope.

### Requirements
The following packages are required: pandas, numpy, sklearn, matplotlib, scipy, imblearn, astropy, statsmodels, patsy, FATS.

IMPORTANT: The feature extraction package, FATS, is not supported in Python 3.x. Therefore, a Python 2.x must be used to run the notebook, IF this package is to be used. 
However, if this is not possible there is no need to run the FATS code, since it has already been ran and the extracted features were saved in a .csv file, which can be directly loaded ('flux_med_features_FATS.csv'). 

The latest version of FATS should be installed from the github repository using:
git clone https://github.com/isadoranun/FATS.git
python setup.py install

### Data
The raw light-curve data from the K2 mission can be downloaded from:
https://archive.stsci.edu/pub/k2/lightcurves/tarfiles/

The dataset used in this project is a collection of flux time-series from Campaigns 1,3 and 5 of the K2 mission.
