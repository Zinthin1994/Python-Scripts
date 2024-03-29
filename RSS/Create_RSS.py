#NOTE this runs under sudo only because of where the file is#
import requests
import json
import os

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

#Open the xml file, delete everything, and write the first few lines for RSS
os.chdir("/var/www/zacharyalbright.com")
f = open("NewPHXResturant.xml", "w")
f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
f.write("<rss version=\"2.0\">\n")
f.write("<channel>\n")
f.write("<title>New PHX Resturants</title>\n")
f.write("<link>https://www.w3schools.com</link>\n")
f.write("<description>This is a description</description>\n")


for name in a:
    f.write("<item>\n")
    #xml does not play well with &.Check to see if name of resturant has one and then changes it to 'and'
    Businessname = business_data['businesses'][x]["name"]
    f.write("<title>" + Businessname.replace("&", "and") + "</title>" + "\n")
    Businessurl = business_data['businesses'][x]["url"]
    f.write("<link>" + Businessurl.replace("&", "&amp;") + "</link>\n")
    #not sure why this was shoing up as a list, so I needed to join the list intoa string for it to be able to print
    Address = ' '.join(business_data['businesses'][x]["location"]["display_address"])
    f.write("<description>" + Address.replace("&", "&amp;") + "</description>" + "\n")
    f.write("</item>\n")
    if x == total - 1:
        break
    x= x + 1


f.write("</channel>\n")
f.write("</rss>\n")


#Read out what was written#
f = open("NewPHXResturant.xml", "r")
print(f.read())


