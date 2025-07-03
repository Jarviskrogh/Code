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
        self.xrds['v'].plot()
        plt.show()

point = [(19.4, 78.8)]
name = 'glacierVel.nc'
graph = graphing(point, name)
# graph.xrds['v'].plot()
# plt.show()
#print(graph.xrds)
#print(graph.xrds.data_vars) #Data vars: date_dt, v, vx_error, vy, vy_error, v_error, vx, mission_img1, satellite_img1,
#   lon, lat, x_proj, y_proj
df = graph.xrds.to_dataframe()
#df.to_csv('C:\\Users\\betha\\Desktop\LaserGlacier\Code\data.csv')
            




