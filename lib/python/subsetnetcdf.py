import os, sys, glob
import xarray as xr
inputfile = sys.argv[1]
outputfile = 'subset' + glob.glob(sys.argv[1] + '/*')[0].split('/')[-1]
ds = xr.open_dataset(glob.glob(inputfile + '/*')[0])
ds_subset = ds.sel(lat=slice(-20,50), lon=slice(0,110))
ds_subset.to_netcdf(outputfile)    
