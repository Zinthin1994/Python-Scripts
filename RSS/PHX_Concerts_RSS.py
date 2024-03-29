"""
Username zin1994
password Account94!
Consumer Key: cVkKQ6fKloepGRQ3aXw2ioNUfjTvgykH
Consumer Secret: gD9axKm5FHj42mTj
"""

import requests
import json
import os
from operator import itemgetter

API_KEY = 'cVkKQ6fKloepGRQ3aXw2ioNUfjTvgykH'

X = 0

response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&city=Phoenix&size=200&apikey=" + API_KEY)
output = response.json()
total = len(output['_embedded']['events'])
a = json.dumps(output)

#Open the xml file, delete everything, and write the first few lines for RSS
os.chdir("/var/www/zacharyalbright.com")
f = open("PHXConcert.xml", "w")
f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
f.write("<rss version=\"2.0\">\n")
f.write("<channel>\n")
f.write("<title>PHX Concerts</title>\n")
f.write("<link>https://www.w3schools.com</link>\n")
f.write("<description>This is a description</description>\n")

list = []

for name in a:
    infolist = []
    ConcertName = output['_embedded']['events'][X]['name']
    ConcertDate = output['_embedded']['events'][X]['dates']['start']['localDate']
    Concerturl = output['_embedded']['events'][X]['url']
    ConcertVenue = output['_embedded']['events'][X]['_embedded']['venues'][0]['name']
    infolist.append(ConcertName)
    infolist.append(ConcertDate)
    infolist.append(Concerturl)
    infolist.append(ConcertVenue)
    
    list.append(infolist)
    if X == total - 1:
        break
    X= X + 1

X = 0
listsorted = sorted(list,key=itemgetter(1))

for concerts in listsorted:
    f.write("<item>\n")
    #xml does not play well with &.Check to see if name of resturant has one and then changes it to 'and'
    ConcertName = listsorted[X][0]
    f.write("<title>" + ConcertName.replace("&", "and") + "</title>" + "\n")
    Concerturl = listsorted[X][2]
    f.write("<link>" + Concerturl.replace("&", "&amp;") + "</link>\n")
    ConcertVenue = listsorted[X][3]
    #not sure why this was shoing up as a list, so I needed to join the list intoa string for it to be able to print
    ConcertDate = listsorted[X][1]
    f.write("<description>" + ConcertDate + ' @ ' + ConcertVenue + "</description>" + "\n")
    f.write("</item>\n")
    if X == total - 1:
        break
    X= X + 1

f.write("</channel>\n")
f.write("</rss>\n")

f = open("PHXConcert.xml", "r")
print(f.read())



#print(output['_embedded']['events'][X]['_embedded']['venues'][0]['name']) #Venue
#print(output['_embedded']['events'][X]['priceRanges'][0]['min'],"-",output['_embedded']['events'][X]['priceRanges'][0]['max']) #price


