from astropy.io import fits
from astropy.table import Table
import os, sys
import pandas as pd
import numpy as np
from IPython.display import clear_output

def flux_compiler(campaign_no, cand_names):
    
    path = os.getcwd()+'\\Data\\lightcurves_c'+str(campaign_no)+'_long'
    
    files_list = sorted(os.listdir(path))
    n_files = len(files_list)

    flux = []
    star_names = ['']*(n_files)
    labels = []


    for i, data_file in enumerate(files_list):
        file_path = path + '\\' + data_file
        star_info = fits.open(file_path)
        star_name = star_info[0].header['OBJECT']
        star_names[i] = star_name
        star_data = fits.getdata(file_path, 1)
        flux_ = (pd.Series(Table(star_data)['PDCSAP_FLUX']).dropna()).values
       
        flux.append(flux_)
    
        if cand_names['epic_name'][cand_names['k2_campaign'] == campaign_no].str.contains(star_name).any():
            dict1 = {'label': 1}
        else:
            dict1 = {'label': 0}
        
        labels.append(dict1)
    
        if i%10 == 0:
            clear_output()
            print('{}/{}'.format(i,n_files))
            sys.stdout.flush()

    flux = pd.DataFrame.from_records(flux,index=star_names)
    labels = pd.DataFrame(labels,index=star_names)

    save_path_flux = os.getcwd()+'\\Data\\c'+str(campaign_no)+'_lightcurves.csv'
    save_path_labels = os.getcwd()+'\\Data\\c'+str(campaign_no)+'_labels.csv'

    flux.to_csv(save_path_flux)
    labels.to_csv(save_path_labels)


    print('Flux data successfully loaded and saved as csv files.')