import matplotlib.pyplot as plt
#data embedded into code
iot_sensors_data = {
    "data": [
        {
            "lighting": True,
            "temperature": 25.0,
            "humidity": 65,
            "air_quality": True
        },
        {
            "lighting": False,
            "temperature": 24.5,
            "humidity": 68,
            "air_quality": False
        },
        {
            "lighting": True,
            "temperature": 24.8,
            "humidity": 70,
            "air_quality": True
        },
        {
            "lighting": True,
            "temperature": 25.2,
            "humidity": 64,
            "air_quality": False
        },
        {
            "lighting": False,
            "temperature": 24.9,
            "humidity": 67,
            "air_quality": True
        },
        {
            "lighting": True,
            "temperature": 25.1,
            "humidity": 62,
            "air_quality": True
        },
        {
            "lighting": True,
            "temperature": 24.7,
            "humidity": 69,
            "air_quality": True
        },
        {
            "lighting": False,
            "temperature": 25.5,
            "humidity": 66,
            "air_quality": False
        },
        {
            "lighting": True,
            "temperature": 24.4,
            "humidity": 71,
            "air_quality": True
        }
    ]
}

# extract the data for each sensor type
temperatures = [d['temperature'] for d in iot_sensors_data['data']]
humidities = [d['humidity'] for d in iot_sensors_data['data']]
air_qualities = [1 if d['air_quality'] else 0 for d in iot_sensors_data['data']]
lighting = [1 if d['lighting'] else 0 for d in iot_sensors_data['data']]

# create a graph for temperature data
plt.plot(temperatures, 'r')
plt.title('Temperature Data')
plt.xlabel('Sensor Reading')
plt.ylabel('Temperature (C)')
plt.show()

# create a graph for humidity data
plt.plot(humidities, 'r')
plt.title('Humidity Data')
plt.xlabel('Sensor Reading')
plt.ylabel('Humidity (%)')
plt.show()

# create a graph for air quality data
plt.plot(air_qualities, 'r')
plt.title('Air Quality Data')
plt.xlabel('Sensor Reading')
plt.ylabel('Air Quality (1/0)')
plt.show()

# create a bar chart for lighting data
plt.bar(['Off'], [len(lighting) - sum(lighting)], color='r')
plt.bar(['On'], [sum(lighting)], color='blue')
plt.title('Lighting Data')
plt.xlabel('Lighting Status')
plt.ylabel('Number of Occurrences')
plt.show()
