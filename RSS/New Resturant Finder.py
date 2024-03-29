import requests
import json

# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'
#unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = 'v4b91lD5TiaeEvufCdrX2wJeApSa18ir5_sdorFk22VK7a8kA3gey1f4B9-_LT3ns2p1Tz6KmM6e-Ty_1NhPS4PCwr_f8ssEkm7-jwLWek3uO0Dsrqbbs5IRv8nMYnYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
PARAMETERS = {
             'location': 'Phoenix',
              'attributes': 'hot_and_new'}

# BUSINESS MATCH PARAMETERS - EXAMPLE
#PARAMETERS = {'name': 'Peets Coffee & Tea',
#              'address1': '7845 Highland Village Pl',
#              'city': 'San Diego',
#              'state': 'CA',
#              'country': 'US'}

# Make a request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

business_data = response.json()

a = json.dumps(business_data)

x = 0
total = len(business_data['businesses'])
for name in a:
    print(business_data['businesses'][x]["name"],"-",business_data['businesses'][x]["location"]["display_address"])
    if x == total - 1:
        break
    x= x + 1


