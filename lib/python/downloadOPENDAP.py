import os, sys, glob, dask
import xarray as xr

url = sys.argv[1]
#url = 'https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/fcast/inst3_3d_aer_Nv/inst3_3d_aer_Nv.20260503_00?airdens[0][0:71][380:520][640:800],time[0],lev[0:71],lat[380:520],lon[640:800]'

ds = xr.open_dataset(url, engine="netcdf4")
var = list(ds.data_vars)[0]
output = ds.time.dt.strftime(var + '_%Y%m%d_%H.nc').item()
ds.to_netcdf(output)

