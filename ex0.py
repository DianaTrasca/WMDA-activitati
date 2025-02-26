### **Exercise 1: Extracting and Cleaning Data from an API**
import requests
import pandas as pd

#cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
#  url = f"https://wttr.in/{city}?format=%C+%t"

import requests
import pandas as pd

# List of cities for which we need to fetch weather data
cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]

# List to store weather information
weather_data = []

# Fetch weather data for each city
for city in cities:
    # API URL to fetch the weather information for each city
    url = f"https://wttr.in/{city}?format=%C+%t"

    # Send GET request to the API
    response = requests.get(url)

    # Split the response into weather condition and temperature
    weather_info = response.text.split(' ')
    condition = weather_info[0]
    temperature = ' '.join(weather_info[1:])

    # Append city and weather data to the list
    weather_data.append({"City": city, "Weather Condition": condition, "Temperature": temperature})

# Create a DataFrame from the weather data list
df = pd.DataFrame(weather_data)

# Clean the data (optional step, for example if the temperature includes unwanted characters)
df['Temperature'] = df['Temperature'].str.strip()  # Strips any leading/trailing whitespace

# Save the cleaned DataFrame to a CSV file
df.to_csv("weather_data.csv", index=False)

# Print the DataFrame to view the result
print(df)