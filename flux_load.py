from astropy.io import fits
from astropy.table import Table
import os, sys
import pandas as pd
import numpy as np
from IPython.display import clear_output

def flux_compiler(campaign_no, cand_names):

# function used to load and compile the flux data from multiple fits files

    #location of fits files
    path = os.getcwd()+'\\Data\\lightcurves_c'+str(campaign_no)+'_long'

    files_list = sorted(os.listdir(path)) #list of fits files to be loaded
    n_files = len(files_list) #number of fits files to be loaded

    #create empty lists to store flux data and labels
    flux = []
    star_names = ['']*(n_files)
    labels = []


    #for loop that reads each of the files in files_list using the astropy package, extracts and saves the flux time-series and determines the labels of each sample
    for i, data_file in enumerate(files_list):
        #load fits file
        file_path = path + '\\' + data_file
        star_info = fits.open(file_path)
        star_name = star_info[0].header['OBJECT'] #get star name
        star_names[i] = star_name
        star_data = fits.getdata(file_path, 1)
        flux_ = (pd.Series(Table(star_data)['PDCSAP_FLUX']).dropna()).values #extract flux data from fits file

        flux.append(flux_) #append extracted flux to list of all fluxes that have been extracted

        #determine label of sample by checking whether it is included in the k2_campaign list of exoplanet candidates
        if cand_names['epic_name'][cand_names['k2_campaign'] == campaign_no].str.contains(star_name).any():
            dict1 = {'label': 1}
        else:
            dict1 = {'label': 0}

        labels.append(dict1) #append label to list of labels

        #display progress
        if i%10 == 0:
            clear_output()
            print('{}/{}'.format(i,n_files))
            sys.stdout.flush()

    #create flux and label DataFrames from lists
    flux = pd.DataFrame.from_records(flux,index=star_names)
    labels = pd.DataFrame(labels,index=star_names)

    #saved extracted flux data and labels in csv files with name indicating the corresponding campaign_no from which the data has been extracted
    save_path_flux = os.getcwd()+'\\Data\\c'+str(campaign_no)+'_lightcurves.csv'
    save_path_labels = os.getcwd()+'\\Data\\c'+str(campaign_no)+'_labels.csv'

    flux.to_csv(save_path_flux)
    labels.to_csv(save_path_labels)


    print('Flux data successfully loaded and saved as csv files.')
