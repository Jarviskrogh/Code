import itslive
import xarray as xr
import matplotlib.pyplot as plt

# Define your point of interest (lon, lat)
point = [(19.4, 78.8)]  # Example point

# Get velocity time series
velocities = itslive.velocity_cubes.get_time_series(points=point)

# Extract the data for our single point
point_data = velocities[0]  # This is a dictionary containing metadata and the xarray Dataset

# The actual time series data is in the 'time_series' key
ds = point_data['time_series']

# Add the geographic coordinates as variables (not just attributes)
ds['lon'] = point_data['returned_point_geographic_coordinates'][0]
ds['lat'] = point_data['returned_point_geographic_coordinates'][1]

# Add the projected coordinates
ds['x_proj'] = point_data['returned_point_projected_coordinates']['coords'][0]
ds['y_proj'] = point_data['returned_point_projected_coordinates']['coords'][1]
ds.attrs['projection'] = f"EPSG:{point_data['returned_point_projected_coordinates']['epsg']}"

# Add additional metadata from the point_data dictionary
ds.attrs.update({
    'requested_coordinates': str(point_data['requested_point_geographic_coordinates']),
    'returned_coordinates': str(point_data['returned_point_geographic_coordinates']),
    'offset_from_requested_meters': point_data['returned_point_offset_from_requested_in_projection_meters'],
    'source': 'NASA ITS_LIVE Project',
    'processing': 'Converted to NetCDF format'
})

# Save to NetCDF
output_file = 'glacier_velocity.nc'
ds.to_netcdf(output_file)
#print(f"Successfully saved to {output_file}")

# Verify by loading back
loaded_ds = xr.open_dataset(output_file)
#print(loaded_ds)
loaded_ds['v'].plot()  # Plot the velocity data
plt.show()

# # For multiple points
# all_datasets = []

# for i, point_data in enumerate(velocities):
#     ds = point_data['time_series'].copy()
    
#     # Add point-specific metadata
#     ds['lon'] = point_data['returned_point_geographic_coordinates'][0]
#     ds['lat'] = point_data['returned_point_geographic_coordinates'][1]
#     ds['point_id'] = i
    
#     all_datasets.append(ds)

# # Combine all points into one dataset
# combined_ds = xr.concat(all_datasets, dim='point')

# # Save multi-point dataset
# combined_ds.to_netcdf('multi_point_velocities.nc')