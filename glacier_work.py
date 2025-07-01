import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import itslive

#glacier_file_ = 'C:\\Users\\betha\\Desktop\LaserGlacier\ITS_LIVE_velocity_120m_RGI07A_2012_v02.nc'
glacier_file = "/home/brjarvis/Documents/LASERGlacier/ITS_LIVE_velocity_120m_RGI07A_2012_v02.nc"
xrds = xr.open_dataset(glacier_file)

#print(xrds)
#for attr, value in xrds.attrs.items():
#    print(f"{attr}: {value} \n")
#print(xrds.data_vars)
#print(xrds.data_vars['v_error'])
#print(xrds.data_vars['v_error'].attrs)
#print(xrds.data_vars['v_error'].values)
#print(xrds.data_vars['landice'])

#xrds['mapping'].plot()
#xrds['count'].plot()
#xrds['landice'].plot()
#xrds['floatingice'].plot()
#xrds['v'].plot()
#xrds['vx'].plot()
#xrds['vy'].plot()
#xrds['v_error'].plot()
#xrds['vx_error'].plot()
#xrds['vy_error'].plot()
#plt.show()

velocity = xrds['v'].to_dataframe()
df = xrds.to_dataframe()
#df.to_csv('C:\\Users\\betha\\Desktop\\LaserGlacier\\allData')
#print(df)

xSlice = xrds.sel(x = 900532.5)
xSliceFrame = xSlice.to_dataframe()
print(xSliceFrame)
#xSliceFrame.to_csv('C:\\Users\\betha\\Desktop\\LaserGlacier\\xSlice')





