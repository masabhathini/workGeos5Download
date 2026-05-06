import os, sys, glob, dask
import pandas as pd
import xarray as xr

url = sys.argv[1]
datestamp = pd.to_datetime(sys.argv[2], format= "%Y%m%d_%H%M%S")
#url = 'https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/fcast/inst3_3d_aer_Nv/inst3_3d_aer_Nv.20260503_00?airdens[0][0:71][380:520][640:800],time[0],lev[0:71],lat[380:520],lon[640:800]'

ds = xr.open_dataset(url, engine="netcdf4")
print(ds.time.dt.strftime('Actual Timestamp: %Y%m%d_%H').item())
var = list(ds.data_vars)[0]
ds_out = ds.assign_coords(time=[datestamp])
output = ds_out.time.dt.strftime(var + '_%Y%m%d_%H.nc').item()
ds_out.to_netcdf(output)

