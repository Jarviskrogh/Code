# import h5py
# import matplotlib.pyplot as plt

# file_path = 'your_data.h5' # Replace with your HDF5 file path
# with h5py.File(file_path, 'r') as f:
#     # Access and plot data inside this block
#     pass

# with h5py.File(file_path, 'r') as f:
#     print("Keys (groups/datasets) in the HDF5 file:")
#     print(list(f.keys()))
#     # If you have nested groups, you might need to navigate them:
#     # group_name = 'your_group'
#     # if group_name in f:
#     #     print(f"Keys in '{group_name}':")
#     #     print(list(f[group_name].keys()))

# with h5py.File(file_path, 'r') as f:
#     data = f['data_to_plot'][:] # The [:] loads the data into memory as a NumPy array

# with h5py.File(file_path, 'r') as f:
#     data = f['my_group/my_dataset'][:]

# with h5py.File(file_path, 'r') as f:
#     data = f['data_to_plot'][:]
#     plt.figure(figsize=(8, 6))
#     plt.plot(data) # Example for a simple 1D plot
#     plt.title('Plot from HDF5 Data')
#     plt.xlabel('X-axis Label')
#     plt.ylabel('Y-axis Label')
#     plt.grid(True)
#     plt.show()
