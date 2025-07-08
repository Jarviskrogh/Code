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
        # xr.plot.line(self.xrds['v'].dropna('mid_date'))
        # date = self.xrds.sel(mid_date='2018')
        plt.figure(figsize=(20, 8))
        # date['v'].plot.scatter()
        self.xrds['v'].plot.scatter()
        plt.title('Velocity over Time')
        plt.xlabel('Time')
        plt.ylabel('Velocity (m/yr)')
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()                       
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

    def calculateRunningMean(self, window_size=12):
        """
        Calculate a running mean (moving average) for the specified variable.
        Returns the running mean as a new DataArray.
        """
        # Ensure we have valid data points
        valid_data = self.xrds['v'].where(self.xrds['v'].notnull(), drop=True)
        
        # Calculate rolling mean with center alignment
        rolling_mean = valid_data.rolling(
            mid_date=window_size, 
            center=True, 
            min_periods=1  # Return partial windows
        ).mean()
        
        return rolling_mean




point = [(18.9377, 78.5853)]
name = 'glacierDATA.nc'
graph = graphing(point, name)
graph.plotV()
#print(graph.xrds['v'].attrs['description'])
#print(graph.xrds.data_vars) #Data vars: date_dt, v, vx_error, vy, vy_error, v_error, vx, mission_img1, satellite_img1,
#   lon, lat, x_proj, y_proj
df = graph.xrds.to_dataframe()
#df.to_csv('C:\\Users\\betha\\Desktop\LaserGlacier\Code\data.csv')
            




# import xarray as xr
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import datetime as dt
# import itslive
# from convertNetCDF import convertToNetCDF

# class graphing(convertToNetCDF):
#     def __init__(self, points, name):
#         super().__init__(points, name)
#         try:
#             self.xrds = xr.open_dataset(self.nameForFile, decode_timedelta=True)
#         except:
#             convertTime = convertToNetCDF(self.origPoints, self.nameForFile)
#             convertTime.convertFile()
#             self.xrds = xr.open_dataset(self.nameForFile, decode_timedelta=True)
    
# #     def calculate_running_mean(self, variable='v', window_size=12):
# #         """
# #         Calculate a running mean (moving average) for the specified variable.
# #         Returns the running mean as a new DataArray.
# #         """
# #         # Ensure we have valid data points
# #         valid_data = self.xrds[variable].where(self.xrds[variable].notnull(), drop=True)
        
# #         # Calculate rolling mean with center alignment
# #         rolling_mean = valid_data.rolling(
# #             mid_date=window_size, 
# #             center=True, 
# #             min_periods=1  # Return partial windows
# #         ).mean()
        
# #         return rolling_mean
    
# #     def plot_year_with_running_mean(self, year='2019', variable='v', window_size=12):
# #         """
# #         Plot data for a specific year with running mean.
# #         """
# #         # Select data for the specific year
# #         year_data = self.xrds.sel(mid_date=str(year))
        
# #         # Calculate running mean for the entire dataset first
# #         running_mean = self.calculate_running_mean(variable, window_size)
        
# #         # Then select just the year we want from the running mean
# #         year_running_mean = running_mean.sel(mid_date=str(year))
        
# #         # Create figure
# #         plt.figure(figsize=(12, 6))
        
# #         # Plot original data for the year
# #         year_data[variable].plot.line(
# #             marker='o', 
# #             markersize=6, 
# #             linestyle='None', 
# #             alpha=0.8, 
# #             label=f'Original data ({year})',
# #             color='blue'
# #         )
        
# #         # Plot running mean for the year
# #         year_running_mean.plot.line(
# #             color='red', 
# #             linewidth=1.5, 
# #             label=f'Running mean (window={window_size})'
# #         )
        
# #         plt.title(f'{variable} during {year} with Running Mean')
# #         plt.xlabel('Time')
# #         plt.ylabel(f'{variable} (m/s)')
# #         plt.legend()
# #         plt.grid(True, which='both', linestyle='--', alpha=0.5)
# #         plt.tight_layout()
# #         plt.show()


    
#     def manual_running_mean(self, variable='v', window_size=12):
#         """
#         Calculate running mean manually without using rolling()
#         """
#         # Get the values and dates
#         values = self.xrds[variable].values
#         dates = self.xrds['mid_date'].values
        
#         # Initialize output array
#         running_mean = np.full_like(values, np.nan)
        
#         half_window = window_size // 2
        
#         for i in range(len(values)):
#             # Define window boundaries
#             start = max(0, i - half_window)
#             end = min(len(values), i + half_window + 1)
            
#             # Calculate mean for the window
#             window_values = values[start:end]
#             valid_values = window_values[~np.isnan(window_values)]
            
#             if len(valid_values) > 0:
#                 running_mean[i] = np.mean(valid_values)
        
#         # Create new DataArray with the running mean
#         return xr.DataArray(
#             data=running_mean,
#             dims=['mid_date'],
#             coords={'mid_date': dates},
#             name=f'{variable}_running_mean'
#         )
    
#     def plot_year_manual_running_mean(self, year='2019', variable='v', window_size=6):
#         """
#         Plot data for a specific year with manually calculated running mean
#         """
#         # Calculate running mean for entire dataset
#         running_mean = self.manual_running_mean(variable, window_size)
        
#         # Select data for specific year
#         year_data = self.xrds.sel(mid_date=str(year))
#         year_running_mean = running_mean.sel(mid_date=str(year))
        
#         # Create plot
#         plt.figure(figsize=(12, 6))
        
#         # Plot original data
#         year_data[variable].plot.line(
#             marker='o', 
#             markersize=6,
#             linestyle='None',
#             alpha=0.7,
#             label=f'Original data ({year})',
#             color='blue'
#         )
        
#         # Plot running mean
#         year_running_mean.plot.line(
#             color='red',
#             linewidth=1,
#             label=f'Manual running mean (window={window_size})'
#         )
        
#         plt.title(f'{variable} during {year} with Manual Running Mean')
#         plt.xlabel('Time')
#         plt.ylabel(f'{variable} (m/s)')
#         plt.legend()
#         plt.grid(True, alpha=0.3)
#         plt.tight_layout()
#         plt.show()

# # Example usage
# point = [(19.4, 78.8)]
# name = 'glacierDATA.nc'
# graph = graphing(point, name)
# graph.plot_year_manual_running_mean(year='2019', variable='v', window_size=7000)

# # # Example usage
# # point = [(19.4, 78.8)]
# # name = 'glacierDATA.nc'
# # graph = graphing(point, name)
# # graph.plot_year_with_running_mean(year='2019', variable='v', window_size=2000)