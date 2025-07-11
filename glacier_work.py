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
    
    def plotAllPtsNoYear(self, variable='v'):
        plt.figure(figsize=(20, 8))

        vData = self.xrds[variable].dropna('mid_date')
        
        point1 = vData.sel(point=0)
        point2 = vData.sel(point=1)
        point3 = vData.sel(point=2)
        point4 = vData.sel(point=3)

        point1.plot.scatter(label=f'Original point 1 Data ({variable})', color='blue')
        point2.plot.scatter(label=f'Original point 2 Data ({variable})', color='orange')
        point3.plot.scatter(label=f'Original point 3 Data ({variable})', color='black')
        point4.plot.scatter(label=f'Original point 4 Data ({variable})', color='pink')

        plt.xlabel('Time')
        if variable == 'v':
            plt.title('Velocity over Time')
            plt.ylabel('Velocity (m/yr)')
        else:
            plt.title(f'{variable} over Time')
            plt.ylabel(f'{variable} (m/yr)')
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()                       
        plt.show()

    def plotSinglePtNoYear(self, variable='v', pt=0):
        plt.figure(figsize=(20, 8))

        vData = self.xrds[variable].dropna('mid_date')
        
        point = vData.sel(point=pt)

        point.plot.scatter(label=f'Original point {pt} Data ({variable})', color='blue')

        
        plt.xlabel('Time')
        if variable == 'v':
            plt.title('Velocity over Time')
            plt.ylabel('Velocity (m/yr)')
        else:
            plt.title(f'{variable} over Time')
            plt.ylabel(f'{variable} (m/yr)')
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()                       
        plt.show()



    def plotWithYear(self, variable='v', year=2020):

        vData = self.xrds[variable].dropna('mid_date')
        vDataYear = vData.sel(mid_date=str(year))
        

        plt.figure(figsize=(20, 8))

        vDataYear.plot.scatter(label=f'Original data ({variable})', color='blue')
    
        plt.xlabel('Time')
        if variable == 'v':
            plt.title(f'Velocity over Time during {year}')
            plt.ylabel('Velocity (m/yr)')
        else:
            plt.title(f'{variable} over Time during {year}')
            plt.ylabel(f'{variable} (m/yr)')
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()                       
        plt.show()

    def plotNoYearRM(self, variable='v', window_size=30):

        vData = self.xrds[variable].dropna('mid_date')
        
        runningMean = self.calculate_running_mean(variable, window_size)

        plt.figure(figsize=(20, 8))

        vData.plot.scatter(label=f'Original data ({variable})', color='blue')

        runningMean.plot.line(
            color='red', 
            linewidth=2, 
            label=f'Running mean (window={window_size})'
        )

    
        plt.xlabel('Time')
        if variable == 'v':
            plt.title('Velocity over Time with Running Mean')
            plt.ylabel('Velocity (m/yr)')
        else:
            plt.title(f'{variable} over Time')
            plt.ylabel(f'{variable} (m/yr)')
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()                       
        plt.show()

    def plotWithYearRM(self, variable='v', year=2020, window_size=20):

        vData = self.xrds[variable].dropna('mid_date')
        vDataYear = vData.sel(mid_date=str(year))
        
        runningMean = self.calculate_running_mean(variable, window_size)
        runningMeanYear = runningMean.sel(mid_date=str(year))

        plt.figure(figsize=(20, 8))

        vDataYear.plot.scatter(label=f'Original data ({variable})', color='blue')

        runningMeanYear.plot.line(
            color='red', 
            linewidth=2, 
            label=f'Running mean (window={window_size})'
        )

    
        plt.xlabel('Time')
        if variable == 'v':
            plt.title(f'Velocity over Time during {year} with Running Mean')
            plt.ylabel('Velocity (m/yr)')
        else:
            plt.title(f'{variable} over Time during {year}')
            plt.ylabel(f'{variable} (m/yr)')
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()                       
        plt.show()
    
    def calculate_running_mean(self, variable='v', window_size=12):
        """
        Calculate a running mean (moving average) for the specified variable.
        Returns the running mean as a new DataArray.
        """
        # Ensure we have valid data points
        valid_data = self.xrds[variable].where(self.xrds[variable].notnull(), drop=True)
        valid_data = valid_data.sortby('mid_date')

        # Calculate rolling mean with center alignment
        rolling_mean = valid_data.rolling(
            mid_date=window_size, 
        ).mean()
        
        return rolling_mean




points = [(18.5916, 78.6027), (18.7564, 78.5919), (18.9212, 78.5766), (19.0379, 78.5532)]
name = 'glacierDATAs.nc'
graph = graphing(points, name)
graph.plotSinglePtNoYear('v', 2)
#print(graph.xrds.dims)
#print(graph.xrds.data_vars) #Data vars: date_dt, v, vx_error, vy, vy_error, v_error, vx, mission_img1, satellite_img1,
#   lon, lat, x_proj, y_proj
# df = graph.xrds.to_dataframe()
# df.to_csv('C:\\Users\\betha\\Desktop\LaserGlacier\Code\data.csv')