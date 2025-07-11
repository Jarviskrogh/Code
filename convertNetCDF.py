import itslive
import xarray as xr
import numpy as np

class convertToNetCDF:
    def __init__(self, points, name):
        self.origPoints = points
        self.nameForFile = name

    def convertFile(self):
        velocities = itslive.velocity_cubes.get_time_series(points=self.origPoints)
        
        # Create a list to store processed datasets
        processedDatasets = []
        
        for i, pointData in enumerate(velocities):
            ds = pointData['time_series'].copy()
            
            # Add point-specific variables as coordinates
            ds.coords['lon'] = pointData['returned_point_geographic_coordinates'][0]
            ds.coords['lat'] = pointData['returned_point_geographic_coordinates'][1]
            ds.coords['x_proj'] = pointData['returned_point_projected_coordinates']['coords'][0]
            ds.coords['y_proj'] = pointData['returned_point_projected_coordinates']['coords'][1]
            
            # Add point ID as a coordinate
            ds.coords['point_id'] = i
            
            # Add metadata
            ds.attrs.update({
                'projection': f"EPSG:{pointData['returned_point_projected_coordinates']['epsg']}",
                'requested_coordinates': str(pointData['requested_point_geographic_coordinates']),
                'returned_coordinates': str(pointData['returned_point_geographic_coordinates']),
                'offset_from_requested_meters': pointData['returned_point_offset_from_requested_in_projection_meters'],
            })
            
            processedDatasets.append(ds)
        
        # Combine datasets ensuring proper point dimension
        combinedDs = xr.concat(processedDatasets, dim='point')
        
        # Add global attributes
        combinedDs.attrs.update({
            'source': 'NASA ITS_LIVE Project',
            'processing': 'Converted to NetCDF format'
        })
        
        # Save to NetCDF
        combinedDs.to_netcdf(self.nameForFile)
        return self.nameForFile