import os, sys, glob
import xarray as xr
import dask

aerfile = sys.argv[1]
asmfile = sys.argv[2]
chmfile = sys.argv[3]

outputfile = sys.argv[4]

aer = xr.open_dataset(aerfile.split('/')[-1])
asm = xr.open_dataset(asmfile.split('/')[-1])
chm = xr.open_dataset(chmfile.split('/')[-1])

df_merge = xr.merge([asm, aer, chm], compat='override').sel(lat=slice(5,40), lon=slice(20,70))

df_merge.to_netcdf(outputfile)
