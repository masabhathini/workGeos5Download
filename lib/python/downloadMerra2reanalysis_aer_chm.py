import os, sys, glob, dask
import earthaccess
import xarray as xr
import pandas as pd

auth = earthaccess.login()
days = pd.date_range(start='2015-12-24', end='2015-12-31', freq='D')
coords_first = ["time", "lev", "lat", "lon"]
for day in days:
    print('Processing day: ', day.strftime('%Y-%m-%d'))
    resultsCHM = earthaccess.search_data(short_name="M2I3NVCHM", version='5.12.4',
        temporal=(day.strftime('%Y-%m-%d'), day.strftime('%Y-%m-%d')))
    resultsAER = earthaccess.search_data(short_name="M2I3NVAER", version='5.12.4',
        temporal=(day.strftime('%Y-%m-%d'), day.strftime('%Y-%m-%d')))
    # Download granules to local path
    downloaded_filesAER = earthaccess.download(resultsAER,local_path='/scratch/masabas/tmp/Merra2')
    downloaded_filesCHM = earthaccess.download(resultsCHM,local_path='/scratch/masabas/tmp/Merra2')
    ###########################################
    ###########################################
    ## # OPTIONAL: Open granules using Xarray
    ## downloaded_filesAER = day.strftime('MERRA2_400.inst3_3d_aer_Nv.%Y%m%d.nc4')
    ## downloaded_filesCHM = day.strftime('MERRA2_400.inst3_3d_chm_Nv.%Y%m%d.nc4')
    ## dsAER = xr.open_mfdataset(downloaded_filesAER)
    ## dsCHM = xr.open_mfdataset(downloaded_filesCHM)
    ## ds_subsetAER = dsAER.sel(lat=slice(5,40), lon=slice(20,70))
    ## ds_subsetCHM = dsCHM.sel(lat=slice(5,40), lon=slice(20,70))
    ## print(dsAER, dsCHM)
    ## df_merge = xr.merge([ds_subsetAER, ds_subsetCHM])
    ## var_order = coords_first + [v for v in df_merge.data_vars]
    ## df_merge = df_merge[var_order]
    ## outputfile = day.strftime('subset_Merra2_M2I3NV_AER_CHM_%Y-%m-%d.nc')
    ## print(df_merge.data_vars)
    ## df_merge.to_netcdf(outputfile)

