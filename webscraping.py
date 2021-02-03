import pandas as pd
import requests
from bs4 import BeautifulSoup
import snappy

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999'
)

soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

# print(items[0].find(class_='period-name').get_text())

# print(items[0].find(class_='short-desc').get_text())

# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]

short_description = [item.find(class_='short-desc').get_text()
                     for item in items]

temperatures = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_description)
# print(temperatures, '\n')

print('===========================Data using DataFrame========================================\n')

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_description,
        'temperatures': temperatures
    }
)

print(weather_stuff)

weather_stuff.to_csv('weather.csv')