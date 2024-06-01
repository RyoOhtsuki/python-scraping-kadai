import requests
import pprint
from getpass import getpass

api_key = getpass('api_key: ')
station_name = input('station_name: ')
#api_key = 'AIzaSyBrs6xH6W4dmfgTSepOiOCVWguCeuAmz04'
#station_name = '秋葉原'


url_location = 'https://maps.googleapis.com/maps/api/geocode/json'

response = requests.get(
    url_location,
    params={
        'key': api_key,
        'address': station_name
    }
)

json_data = response.json()
location = json_data['results'][0]['geometry']['location']
lat = location['lat']
lng = location['lng']

url_restaurant = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

response = requests.get(
    url_restaurant,
    params={
        'key': api_key,
        'location': f'{lat},{lng}',
        'radius': 500,
        'type': 'restaurant'
    }
)

json_data = response.json()

for place in json_data['results']:
    name = place['name']
    rating = place['rating']
    address = place['vicinity']
    print(f'Name: {name}, Rating: {rating}, Address: {address}')
