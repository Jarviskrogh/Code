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

        #Use if needed
        vData = vData.sel(mid_date=vData['mid_date'] >= np.datetime64('2010-01-01'))
        #vData = vData.sel(mid_date=vData['mid_date'] <= np.datetime64('2020-01-01'))

        point1 = vData.sel(point=0)
        point2 = vData.sel(point=1)
        point3 = vData.sel(point=2)
        point4 = vData.sel(point=3)

        point1.plot.scatter(label=f'Origin Data ({variable})', color='blue')
        point2.plot.scatter(label=f'Upper half Data ({variable})', color='orange')
        point3.plot.scatter(label=f'Lower half Data ({variable})', color='black')
        point4.plot.scatter(label=f'Terminus Data ({variable})', color='pink')

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

        point.plot.scatter(label=f'Original point {pt+1} Data ({variable})', color='blue')

        
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


    def plot2PtsNoYear(self, variable='v', pt1=0, pt2=3):

        plt.figure(figsize=(20, 8))

        vData = self.xrds[variable].dropna('mid_date')

        point1 = vData.sel(point=pt1)
        point2 = vData.sel(point=pt2)

        if pt1 == 0:
            point1.plot.scatter(label=f'Origin Data ({variable})', color='blue')
        else:
            point1.plot.scatter(label=f'Original point {pt1+1} Data ({variable})', color='blue')
        
        if pt2 == 3:
            point2.plot.scatter(label=f'Terminus Data ({variable})', color='pink')
        else:
            point2.plot.scatter(label=f'Original point {pt1+1} Data ({variable})', color='pink')

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


    def plotAllPtsWithYear(self, variable='v', year=2020):

        plt.figure(figsize=(20, 8))

        vData = self.xrds[variable].dropna('mid_date')
        
        point1 = vData.sel(point=0, mid_date=str(year))
        point2 = vData.sel(point=1, mid_date=str(year))
        point3 = vData.sel(point=2, mid_date=str(year))
        point4 = vData.sel(point=3, mid_date=str(year))

        point1.plot.scatter(label=f'Original point 1 Data ({variable})', color='blue')
        point2.plot.scatter(label=f'Original point 2 Data ({variable})', color='orange')
        point3.plot.scatter(label=f'Original point 3 Data ({variable})', color='black')
        point4.plot.scatter(label=f'Original point 4 Data ({variable})', color='pink')
    
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


    def plotSinglePtWithYear(self, variable='v', pt=0, year=2020):
        plt.figure(figsize=(20, 8))

        vData = self.xrds[variable].dropna('mid_date')
        point = vData.sel(point=pt, mid_date=str(year))

        point.plot.scatter(label=f'Original point {pt+1} Data ({variable})', color='blue')

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


    def plot2PtsWithYear(self, variable='v', pt1=0, pt2=3, year=2020):

        plt.figure(figsize=(20, 8))

        vData = self.xrds[variable].dropna('mid_date')

        point1 = vData.sel(point=pt1, mid_date=str(year))
        point2 = vData.sel(point=pt2, mid_date=str(year))

        if pt1 == 0:
            point1.plot.scatter(label=f'Origin Data ({variable})', color='blue')
        else:
            point1.plot.scatter(label=f'Original point {pt1+1} Data ({variable})', color='blue')
        
        if pt2 == 3:
            point2.plot.scatter(label=f'Terminus Data ({variable})', color='pink')
        else:
            point2.plot.scatter(label=f'Original point {pt1+1} Data ({variable})', color='pink')

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

    def plotSinglePtNoYearRM(self, variable='v', pt=0, window_size=20):

        vData = self.xrds[variable].dropna('mid_date')

        point = vData.sel(point=pt)

        runningMean = self.calculate_running_mean(variable, window_size)
        runningMean = runningMean.sel(point=pt)
        runningMean = runningMean.where(runningMean.notnull(), drop=True)

        plt.figure(figsize=(20, 8))

        point.plot.scatter(label=f'Original point {pt+1} Data ({variable})', color='blue')

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


    def plotSinglePtWithYearRM(self, variable='v', pt=0, year=2020, window_size=10):

        plt.figure(figsize=(20, 8))

        vDataYear = self.xrds[variable].dropna('mid_date')
        pointYear = vDataYear.sel(point=pt, mid_date=str(year))

        runningMeanYear = self.calculate_running_mean(variable, window_size)
        runningMeanYear = runningMeanYear.sel(point=pt, mid_date=str(year))
        runningMeanYear = runningMeanYear.where(runningMeanYear.notnull(), drop=True)

        pointYear.plot.scatter(label=f'Original point {pt+1} Data ({variable})', color='blue')

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
    
    def plotAllPtsNoYearRM(self, variable='v', window_size=10):
        plt.figure(figsize=(20, 8))

        vData = self.xrds[variable].dropna('mid_date')

        #Use if needed to set bounds
        vData = vData.sel(mid_date=vData['mid_date'] >= np.datetime64('2010-01-01'))
        #vData = vData.sel(mid_date=vData['mid_date'] <= np.datetime64('2020-01-01'))
        
        point1 = vData.sel(point=0)
        point2 = vData.sel(point=1)
        point3 = vData.sel(point=2)
        point4 = vData.sel(point=3)

        runningMean = self.calculate_running_mean(variable, window_size)

        #Use if previous bounds were set
        runningMean = runningMean.sel(mid_date=runningMean['mid_date'] >= np.datetime64('2010-01-01'))
        #runningMean = runningMean.sel(mid_date=runningMean['mid_date'] <= np.datetime64('2020-01-01'))

        runningMeanOrigin = runningMean.sel(point=0)
        runningMeanOrigin = runningMeanOrigin.where(runningMeanOrigin.notnull(), drop=True)

        runningMeanTerminus = runningMean.sel(point=3)
        runningMeanTerminus = runningMeanTerminus.where(runningMeanTerminus.notnull(), drop=True)

        point1.plot.scatter(label=f'Origin Data ({variable})', color='blue')
        point2.plot.scatter(label=f'Upper half Data ({variable})', color='orange')
        point3.plot.scatter(label=f'Lower half Data ({variable})', color='black')
        point4.plot.scatter(label=f'Terminus Data ({variable})', color='pink')


        runningMeanOrigin.plot.line(
            color='green', 
            linewidth=4, 
            label=f'Origin Running Mean (window={window_size})'
        )

        runningMeanTerminus.plot.line(
            color='red', 
            linewidth=4, 
            label=f'Terminus Running Mean (window={window_size})'
        )

        plt.xlabel('Time', fontsize=24)
        if variable == 'v':
            plt.title('Velocity over Time', fontsize=24)
            plt.ylabel('Velocity (m/yr)', fontsize=24)
        else:
            plt.title(f'{variable} over Time')
            plt.ylabel(f'{variable} (m/yr)')

        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)

        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend(fontsize=14)                       
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



#Neg Points
points = [(18.5916, 78.6027), (18.7564, 78.5919), (18.9212, 78.5766), (19.0379, 78.5532)]
#Wahl Points
#points = [(14.0089, 78.5135), (14.0448, 78.4993), (14.1093, 78.4875), (14.1876, 78.4799)]
name = 'negribeenData.nc'
graph = graphing(points, name)
graph.plotAllPtsNoYearRM('v', 5)
#print(graph.xrds.dims)
#print(graph.xrds.data_vars) #Data vars: date_dt, v, vx_error, vy, vy_error, v_error, vx, mission_img1, satellite_img1,
#   lon, lat, x_proj, y_proj
# df = graph.xrds.to_dataframe()
# df.to_csv('negribeenData.csv')