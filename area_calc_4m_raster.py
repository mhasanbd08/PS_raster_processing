import gd
import numpy as np

# area_per_pixel = 100 #example...you change to suit
#
# rasterfile = "E:\__Archive__\IDSS_Archive\RS\GS-tiff\GS_20190201T000000Z.tif"
#
# r = gdal.Open(rasterfile)
# band = 1
# raster_arr = np.array(r.GetRasterBand(band).ReadAsArray())
#
# for cover in np.unique(raster_arr):
#     tot_num_pixels = np.sum(raster_arr == cover)
#     area = tot_num_pixels * area_per_pixel
#     print cover, area

# from rasterstats import zonal_stats
# import rasterio
# import pandas as pd
#
# with rasterio.open("E:\__Archive__\IDSS_Archive\RS\GS-tiff\BdRiceGrowingStage6d_20190120T000000Z.tif") as src:
#     affine = src.transform
#     array = src.read(1)
#     gdf = "E:\__Archive__\IDSS_Archive\GIS\Admin\BD_2_District.shp"
#     df_zonal_stats = pd.DataFrame(zonal_stats(gdf, array, affine=affine))
#
# # adding statistics back to original GeoDataFrame
# gdf2 = pd.concat([gdf, df_zonal_stats], axis=1)

from rasterstats.main import zonal_stats
print (zonal_stats("E:\__Archive__\IDSS_Archive\GIS\Admin\BD_2_District.shp", "E:\__Archive__\IDSS_Archive\RS\GS-tiff\BdRiceGrowingStage6d_20190120T000000Z.tif",
            stats="count min mean max median"))
