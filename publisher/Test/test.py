# test_data_packager.py

from source.data_packager import package_data

# Sample temperature value and packet ID
temperature_value = 25.5
packet_id = 123

# Package the data
packaged_data = package_data(temperature_value, packet_id)

# Print the packaged data
print("Packaged Data:")
print(packaged_data)
