import os, sys, glob, dask
import xarray as xr


ds = xr.open_mfdataset('./*.nc')
outputfile = ds.time.dt.strftime('GEOS.fp.fcst.inst3_3d_ALL_Nv_validtime_%Y%m%d_%H.nc').item()
ds = ds.rename({var: var.upper() for var in ds.data_vars})
ds.to_netcdf(outputfile)
