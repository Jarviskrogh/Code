import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import itslive
from convertNetCDF import convertToNetCDF

class graphing(convertToNetCDF):
    def __init__(self, points, name):
        super().__init__(points, name)
        try:
            self.xrds = xr.open_dataset(self.nameForFile, decode_timedelta=True)
        except:
            convertTime = convertToNetCDF(self.origPoints, self.nameForFile)
            convertTime.convertFile()
            self.xrds = xr.open_dataset(self.nameForFile, decode_timedelta=True)
    
    def plotV(self):
        #self.xrds['v'].plot.scatter()
        #xr.plot.line(self.xrds['v'].dropna('mid_date'))
        date = self.xrds.sel(mid_date='2019')
        date['v'].plot.scatter()
        plt.show()
    
    def plotVX(self):
        #self.xrds['vx'].plot.scatter()
        #xr.plot.line(self.xrds['vx'].dropna('mid_date'))
        date = self.xrds.sel(mid_date='2019')
        date['vx'].plot.scatter()
        plt.show()

    def plotVY(self):
        #self.xrds['vy'].plot.scatter()
        #xr.plot.line(self.xrds['vy'].dropna('mid_date'))
        date = self.xrds.sel(mid_date='2019')
        date['vy'].plot.scatter()
        plt.show()

    def plotV_Error(self):
        #self.xrds['v_error'].plot.scatter()
        #xr.plot.line(self.xrds['v_error'].dropna('mid_date'))
        date = self.xrds.sel(mid_date='2019')
        date['v_error'].plot.scatter()
        plt.show()

    def plotVX_Error(self):
        #self.xrds['vx_error'].plot.scatter()
        #xr.plot.line(self.xrds['vx_error'].dropna('mid_date'))
        date = self.xrds.sel(mid_date='2019')
        date['vx_error'].plot.scatter()
        plt.show()

    def plotVY_Error(self):
        #self.xrds['vy_error'].plot.scatter()
        #xr.plot.line(self.xrds['vy_error'].dropna('mid_date'))
        date = self.xrds.sel(mid_date='2019')
        date['vy_error'].plot.scatter()
        plt.show()




point = [(19.4, 78.8)]
name = 'glacierDATA.nc'
graph = graphing(point, name)
graph.plotV()
#print(graph.xrds['v'].attrs['description'])
#print(graph.xrds.data_vars) #Data vars: date_dt, v, vx_error, vy, vy_error, v_error, vx, mission_img1, satellite_img1,
#   lon, lat, x_proj, y_proj
df = graph.xrds.to_dataframe()
#df.to_csv('C:\\Users\\betha\\Desktop\LaserGlacier\Code\data.csv')
            




