import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

glacier_file = "C:\\Users\\betha\Desktop\LaserGlacier\ITS_LIVE_velocity_120m_RGI07A_2012_v02.nc"
#glacier_file = "/home/brjarvis/Documents/LASERGlacier/ITS_LIVE_velocity_120m_RGI07A_2012_v02.nc"
xrds = xr.open_dataset(glacier_file)

print(xrds)
#for attr, value in xrds.attrs.items():
#    print(f"{attr}: {value} \n")
#print(xrds.data_vars)
#print(xrds.data_vars['v_error'])
#print(xrds.data_vars['v_error'].attrs)
#print(xrds.data_vars['v_error'].values)

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



