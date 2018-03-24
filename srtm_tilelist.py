#! /usr/bin/env python

"""
Download SRTM tiles for given lat/lon bounds
Pipe this to a file, then wget
"""

import sys

#Hardcoded site
#site = "hma"
#site = "conus"
site = sys.argv[1]

#This is SRTM-GL1
#topurl = "https://cloud.sdsc.edu/v1/AUTH_opentopography/Raster/SRTM_GL1/SRTM_GL1_srtm"
#topurl = "http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11" 

#This is NASADEM provisional
topurl = "https://e4ftl01.cr.usgs.gov/provisional/MEaSUREs/NASADEM"

if site == "hma":
    lon = (65, 106)
    lat = (24, 47)
    ew = "E"
    sitedir = 'Eurasia'
elif site == "conus":
    lon = (104, 125)
    lat = (31, 49)
    ew = "W"
    sitedir = 'NorthAmerica'
else:
    sys.exit("Need to manually specify site bounds")

tile_list = []
for i in range(lon[0], lon[1]+1):
    for j in range(lat[0], lat[1]+1):
        tile_list.append('N%02i%s%03i' % (j, ew, i))

productdir = sys.argv[2]
productdir_dict = {'hgt_srtmOnly_R4':'srtmOnly.hgt', 'hgt_merge':'hgt', 'img_comb':'img', 'err_I2':'err'}
if productdir in productdir_dict.keys():
    ext = productdir_dict[productdir]
else:
    sys.exit("Invalid extension")

for tile in tile_list:
    print("%s/%s/%s/%s.%s.zip" % (topurl, sitedir, productdir, tile.lower(), ext))
