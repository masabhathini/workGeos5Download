import os, sys, glob, dask
import earthaccess
import xarray as xr
import pandas as pd

short_name = "M2I3NV" + sys.argv[1]
startdatestamp = sys.argv[2]
enddatestamp = sys.argv[2]
archive = sys.argv[3]
auth = earthaccess.login()
days = pd.date_range(start = startdatestamp, end = enddatestamp, freq='D')
coords_first = ["time", "lev", "lat", "lon"]
for day in days:
    print('Processing day: ', day.strftime('%Y-%m-%d'))
    results = earthaccess.search_data(short_name = short_name, version='5.12.4',
        temporal=(day.strftime('%Y-%m-%d'), day.strftime('%Y-%m-%d')))
    # Download granules to local path
    downloaded_files = earthaccess.download(results, local_path = archive)
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

