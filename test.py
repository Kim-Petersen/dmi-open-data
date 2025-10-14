from datetime import datetime

from dmi_open_data import DMIOpenDataClient, OceanographicDataParameter

client = DMIOpenDataClient(api_key="b552aa1f-3984-4971-8a14-c6afea3f17c8")

print(client.list_parameters())
print(client.get_parameter("MeanTemp"))
print(client.get_parameter("mean_temp"))
print(client.get_parameter("TempDry"))
print(client.get_parameter("temp_dry"))
print(client.get_parameter("SealevDvr"))
print(client.get_parameter("sealev_dvr"))

# Get oceanographic data
ocean_data = client.get_ocean_data(
    parameter=OceanographicDataParameter.Tw,
    station_id="31061",
    from_time=datetime(2025, 9, 8),
    to_time=datetime(2025, 9, 10),
    # time_resolution="hour",
    limit=1000,
)
print(ocean_data)
# x = client.get_ocean_data()
# print(x)
