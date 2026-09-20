import os
import sys
import glob
import xarray as xr

inputdir = sys.argv[1]
outputfile = sys.argv[2]

inputfiles = sorted(glob.glob(os.path.join(inputdir, "*")))

if not inputfiles:
    raise FileNotFoundError(f"No files found in: {inputdir}")

print(f"Found {len(inputfiles)} files")
for f in inputfiles:
    print(f)

ds = xr.open_mfdataset(
    inputfiles,
    combine="by_coords"
)

# Convert data variable names to uppercase
ds = ds.rename({
    var: var.upper()
    for var in ds.data_vars
})

ds.to_netcdf(outputfile)

print(f"Output written to: {outputfile}")
##
##
##import os, sys, glob, dask
##import xarray as xr
##
##inputfile = str(sys.argv[1] + '/*')
##outputfile = str(sys.argv[2])
##
##ds = xr.open_mfdataset(input)
##ds = ds.rename({var: var.upper() for var in ds.data_vars})
##ds.to_netcdf(outputfile)
