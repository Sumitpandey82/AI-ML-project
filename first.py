 # Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample Air Quality data for Indian Cities
data = {
    'city': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow'],
    'date': ['2023-01-15'] * 10,
    'pm25': [250, 120, 180, 90, 70, 150, 110, 160, 200, 130],
    'no2': [80, 50, 60, 40, 30, 65, 55, 70, 90, 60],
    'so2': [30, 20, 25, 15, 10, 18, 22, 28, 35, 22]
}
air_quality_df = pd.DataFrame(data)

# Convert date column to datetime format
air_quality_df['date'] = pd.to_datetime(air_quality_df['date'])

# 1. Basic Data Exploration
print(air_quality_df.head())
print("\nData Info:")
print(air_quality_df.info())

# 2. PM2.5 Analysis
average_pm25 = air_quality_df['pm25'].mean()
print("\nAverage PM2.5 across cities:", average_pm25)

# 3. City with Highest NO2 Levels
city_highest_no2 = air_quality_df.loc[air_quality_df['no2'].idxmax(), 'city']
print("City with highest NO2 levels:", city_highest_no2)

# 4. Correlation between Pollutants
correlation_pm25_no2 = air_quality_df['pm25'].corr(air_quality_df['no2'])
print("Correlation between PM2.5 and NO2:", correlation_pm25_no2)

# 5. Bar Chart of PM2.5 Levels by City
plt.figure(figsize=(12, 6))
sns.barplot(x='city', y='pm25', data=air_quality_df)
plt.title('PM2.5 Levels by City')
plt.xlabel('City')
plt.ylabel('PM2.5')
plt.xticks(rotation=45)
plt.show()

# 6. Scatter Plot of PM2.5 vs NO2
plt.figure(figsize=(10, 6))
sns.scatterplot(x='pm25', y='no2', data=air_quality_df, hue='city')
plt.title('PM2.5 vs. NO2 Levels')
plt.xlabel('PM2.5')
plt.ylabel('NO2')
plt.show()