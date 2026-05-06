import os, sys, glob, dask
import xarray as xr


ds = xr.open_mfdataset('./*.nc')
outputfile = ds.time.dt.strftime('GEOS.fp.fcst.inst3_3d_ALL_Nv_' + startime + '_validtime_%Y%m%d_%H.nc').item()
ds.to_netcdf(outputfile)
